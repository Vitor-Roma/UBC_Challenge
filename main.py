import datetime
from pysolr import Solr
import concurrent.futures
from models import Student
import pandas as pd
import numpy as np
import logging
from dotenv import load_dotenv
import os


load_dotenv()


def main():
    Solr(os.getenv('SOLR_URL'), always_commit=True).delete(q="*:*")
    start = datetime.datetime.now()
    datapath = os.getenv('DATAPATH')
    data = pd.read_csv(datapath, engine='pyarrow').replace([np.nan, -np.inf], None)
    json_data = data.to_dict(orient='records')
    logging.basicConfig(level=logging.INFO)
    with concurrent.futures.ProcessPoolExecutor() as executor:
        [executor.submit(csv_process, item) for item in json_data]
    end = datetime.datetime.now()
    print(end - start)


def without_threads():
    Solr(os.getenv('SOLR_URL'), always_commit=True).delete(q="*:*")
    start = datetime.datetime.now()
    datapath = os.getenv('DATAPATH')
    data = pd.read_csv(datapath, engine='pyarrow').replace([np.nan, -np.inf], None)
    json_data = data.to_dict(orient='records')
    for item in json_data:
        csv_process(item)
    end = datetime.datetime.now()
    print(end - start)


def csv_process(item):
    student_solr_core = Solr(os.getenv('SOLR_URL'), always_commit=True, timeout=999)
    name = item['Nome']
    age = item['Idade']
    year = item['Série']
    grade = item['Nota Média']
    address = item['Endereço']
    father_name = item['Nome do Pai']
    mother_name = item['Nome da Mãe']
    try:
        birthdate = item['Data de Nascimento'].strftime("%Y-%m-%d")
    except AttributeError:
        logging.error('Data de nascimento inválida')
        return None
    data_dict = {
        'name': name,
        'age': age,
        'year': year,
        'grade': grade,
        'address': address,
        'father_name': father_name,
        'mother_name': mother_name,
        'birthdate': birthdate,
    }

    try:
        student = Student(**data_dict)
    except ValueError as err:
        logging.error(f'Erro: {err.json()}')
        return None

    query = f"name:'{student.name}' AND age:{student.age} AND year:{student.year} AND mother_name:'{student.mother_name}'"
    try:
        if student_solr_core.search(query):
            logging.info(f'{student} já existe')
            return None
    except Exception as err:
        logging.error(F'Erro na query do SOLR: {err}')
    try:
        student_solr_core.add(student.model_dump())
        logging.info(student)
    except Exception as err:
        logging.error(f'Erro ao adicionar no SOLR: {err}')


if __name__ == "__main__":
    main()
