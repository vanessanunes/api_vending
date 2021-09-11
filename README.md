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

## Gerar Token
Para gerar token e ter acesso a APIs, faça uma requisição POST para URL /api-token-auth/ digitando usuário e senha, te retornará um token.
Esse token habilitará o usuário a usar a API

## Method POST

/clients/

{
    "name": "Nome do Cliente"
}

/sellers/
{
    "name": "Nome do Vendedor"
}


/products/

{
    "name": "Nome do Produto",
    "price": "15.00"
}

/itens/

Lembrando que cada ´itens´ deve ter apenas um produto com a quantidade desejada.

{
    "product": {
        "name": "Telescopio",
        "price": "150.00"
    },
    "quantity": 6
}

/carts/

Cada ´carts´ pode ter N ´itens´

{
    "client": {
        "name": "Nome do Cliente"
    },
    "seller": {
        "name": "Nome de Vendedor"
    },
    "itens": [
        {
            "product": {
                "name": "Nome do Produto",
                "price": "10.00"
            },
            "quantity": 2
        }
    ]
}
