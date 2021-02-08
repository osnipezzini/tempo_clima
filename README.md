Projeto feito utilizando Python3

Para rodar o projeto é necessário instalar os pacotes do pip e configurar o banco de dados.

O banco de dados usado será PostgreSQL, portanto deve-se criar o banco de dados a ser utilizado no projeto. Você pode definir na string de conexão ou via váriavel de ambiente. Ex: set PGDATABASE=climatempo

```sh
pip install -r requirements.txt
SET PGUSER=postgres
SET PGPASSWORD=SUA_SENHA
SET FLASK_APP=app.py
flask db migrate
flask db upgrade
python app.py run
```

Junto aos arquivos do projeto, existe uma coleção do PostMan com as requisições de exemplo configuradas.


O motivo escolhido para usar Flask foi simplesmente a simplidade para escrever aplicações web. Pensei no Django, mas faz um tempo que não mexo com ele, então achei melhor simplificar