# UBC_Challenge: 

## Desafio Técnico para importação de Dados para o Solr

- Formatar o CSV
  - O script deve ler um arquivo CSV fornecido e realizar a formatação dos dados para garantir consistência e correção.
  - Considere que o arquivo CSV pode conter campos mal formatados, dados ausentes ou outros problemas típicos em conjuntos de dados do mundo real.
   
- Inserir no Solr:
  - Após a formatação, o script deve inserir os dados no Apache Solr.
  - Certifique-se de mapear corretamente os campos do CSV para os campos correspondentes no esquema do Solr.

- Pontos Extras:
  - Lidar com situações de erro durante a formatação e inserção no Solr.
  - Implementar logs adequados para rastrear o progresso e eventuais problemas.
  - Garantir que o script seja eficiente, mesmo para grandes conjuntos de dados.


## Dependências
- Docker
- Docker Compose
- Python 3.10.12

## SOLR
Para iniciar o container do Solr, utilize o comando:
```
docker compose up
```
### Acesse a Interface do Solr Admin

Após subir o container, acesse a Solr Admin Interface em http://localhost:8983/solr.

#### Crie o core
<img src="screenshots/SOLR_admin_core.jpeg">

## Rodar o projeto:

#### Para executar o projeto, siga os passos abaixo:

<h3>Crie e ative seu ambiente virtual com os comandos</h3>

```
python -m venv env
```
<p>Linux:</p>

```
source env/bin/activate
```

<p>Windows:</p>

```
env\Scripts\activate
```

- Renomeie o arquivo ".env_sample" para ".env"


- Instale as dependências utilizando o comando:
```
pip install -r requirements.txt
```

- Utilize o comando para rodar o projeto:
```
python main.py
```

- Para rodar com uma lista mais extensa de dados, mude o valor do DATAPATH da .env para "./dados.csv"

### Caso receba esse erro:
<img src="screenshots/solr_permission_error.jpeg">

```
sudo chmod 777 -R .docker_data
```

### Derrube e suba o docker novamente:

```
docker compose down
docker compose up
```


## Benchmarks

- Para rodar o teste de benchmark, utilize o comando:

```
richbench --repeat 1 --times 1 benchmarks/
```
<img src="screenshots/benchmark.jpeg">
