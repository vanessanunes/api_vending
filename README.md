# Criação de API com PostgreSQL
Projeto de API usando o framework Django + Rest Framework e banco de dados PostgreSQL
## primeiros passos
Crie sua virtualenv:

python -m venv nome_virtualenv

Para ativa-lá:

nome_virtualenv\Script\activate

Faça a instalação das dependencias necessárias que estão em requirements com o seguinte comando:

pip install -r requirements.txt

## criação do arquivo .env
Para auxiliar na criação do arquivo .env, deixarei disponível a versão .env-exemple 

## primeira utilização
Rode os seguintes comandos para fazer a atualização e a utilização do banco de dados:

python manage.py makemigrations

python manage.py migrate

python manage.py runserver

## criação de super usuário
Para a criação, digite no terminal:

python manage.py createsuperuser

Apareceram algumas perguntas, importante incluir o nome e a senha do usuário