from pysolr import Solr
import concurrent.futures
from models import Student
import pandas as pd
import numpy as np
import logging
from pprint import pprint


def main():
    student_solr_core = Solr('http://localhost:8983/solr/students/', always_commit=True)
    datapath = './aluno.csv'
    data = pd.read_csv(datapath).replace([np.nan, -np.inf], None)
    json_data = data.to_dict(orient='records')
    logging.basicConfig(level=logging.INFO)

    with concurrent.futures.ProcessPoolExecutor() as executor:
        data_list = [executor.submit(data_treatment, item) for item in json_data]
        for item in concurrent.futures.as_completed(data_list):
            result = item.result()
            if not result:
                continue
            query = f"name:'{result.name}' AND age:{result.age} AND year:{result.year} AND mother_name:'{result.mother_name}'"
            try:
                if student_solr_core.search(query):
                    pprint(f'{result} já existe')
            except Exception as err:
                logging.error('Erro na query do SOLR')
            try:
                student_solr_core.add(result.model_dump())
                logging.info(result)
            except Exception as err:
                logging.error(f'Erro ao adicionar no SOLR: {err}')


def data_treatment(item):
    name = item['Nome']
    age = item['Idade']
    year = item['Série']
    grade = item['Nota Média']
    address = item['Endereço']
    father_name = item['Nome do Pai']
    mother_name = item['Nome da Mãe']
    birthdate = item['Data de Nascimento']
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
        return student
    except ValueError as err:
        logging.error(f'Erro: {err.json()}')
    return None


if __name__ == "__main__":
    main()
