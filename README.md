# Apple Store - Cognitivo.AI

Solução para o desafio de Backend Developer da Cognitivo.AI

## Dicionario de Dados

* **id**: Identificação do App
* **track_name**: Nome
* **size_bytes**: Tamanho em Bytes
* **currency**: Moeda
* **price**: Valor na Apple Store
* **rating_count_tot**: Qtde de Avaliações
* **rating_count_ver**: Qtde de Avaliações última versão
* **ser_rating**: Avaliação Média
* **user_rating_ver**: Avaliação Média da última versão
* **ver**: Última Versão
* **cont_rating**: Classificação Indicativa
* **prime_genre**: Gênero do App

## Execução

Instalar dependências

```
$ pip install -r requirements.txt
```

Rodar o script em `src/main.py`

```
$ python src/main.py
```

## Informações Adicionais

* O banco de dados local escolhido foi o SQLite pela facilidade de testar sem necessitar instalar um banco de dados como MySQL, PostgreSQL, MongoDb, etc.
* A API do Twitter tem algumas limitações para buscar Tweets e a quantidade de requisições que podem ser feitas em uma janela de 15 minutos, por esse motivo o script só recupera dados dos ultimos 7 dias e limitados a 500 tweets por pagina.
* Como melhoria poderia-se criar um serviço que ficaria conectado no Twitter via Streamming e capturar os Tweets enquanto são gerados e armazenar em um banco de dados para fazer consultas mais precisas.