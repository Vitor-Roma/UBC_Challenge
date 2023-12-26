# UBC_Challenge: Desafio Técnico para importação de Dados para o Solr

## Dependências
- Docker
- Docker Compose
- Python

## SOLR
Para iniciar o container do Solr, utilize o comando:
```
docker compose up
```
### Acesse a Interface do Solr Admin

Após subir o container, acesse a Solr Admin Interface em http://localhost:8983/solr.

#### Crie o core
<img src="SOLR_admin_core.jpeg">

## Rodar o projeto:

#### Para executar o projeto, siga os passos abaixo:

- Instale as dependências utilizando o comando:
```
pip install -r requirements.txt
```

- Utilize o comando para rodar o projeto:
```
python main.py
```