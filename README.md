# Autorization and Authentication

## **Technologies**

This project was developed using the following technologies:

- [Flask](https://flask.palletsprojects.com/en/2.1.x/)
- [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)
- [Flask-JWT-Extended](https://flask-jwt-extended.readthedocs.io/en/stable/)
- [Flask-HTTPAuth](https://flask-httpauth.readthedocs.io/en/latest/)
- [Environs](https://pypi.org/project/environs/)

## **Starting the project**

Clone into the repository and go into project's folder.

```bash
$ git clone https://github.com/Kenzie-Academy-Brasil-Developers/q3-sprint6-autenticacao-e-autorizacao-lsmescolotto
$ cd q3-sprint6-autenticacao-e-autorizacao-lsmescolotto
```

Follow the steps:

```bash
# Install dependencies
$ pip install -r requirements.txt
# Run flask
$ flask run
```

## **base URL**

http://127.0.0.1:5000/api

## **Endpoints**

This API has 5(five) endpoints to: signup, signin, update user, delete user and get user info.

## Authentication not required routes

<h2 align ='center'> User Sign Up </h2>
<br/>
 
`POST /signup - REQUEST FORMAT`
```json
{
"name": "Jane",
"last_name": "Doe",
"email": "janedoe@email.com",
"password": "123456"
}
```
 
If the request is corret, the user will be signed up:
 
`POST /signup - REPONSE FORMAT - STATUS 201`
```json
{
"email": "janedoe@mail.com",
"last_name": "Doe",
"name": "Jane"
}

````
If the email adress is already in use:

`STATUS 400`

```json

{"message":"Email already exists"}

````

<h2 align ='center'> User Sign In </h2>
<br/>

`POST /signin - REQUEST FORMAT`

```json
{
  "email": "janedoe@email.com",
  "password": "123456"
}
```

If the request is corret, the user will be signed in:
`POST /login - RESPONSE FORMAT - STATUS 201`
Flask-JWT-Extended

```json
{
  "accessToken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImphbmVkb2VAbWFpbC5jb20iLCJpYXQiOjE2NDMyNTAwMDAsImV4cCI6MTY0MzI1MzYwMCwic3ViIjoiMyJ9.z90xWRIE7pfKRsw-YqqqUtRxBZGtBPgSZ63yqW04qSc"
}
```

`POST /login - RESPONSE FORMAT - STATUS 201`
Flask-HTTPAuth

````json
{
  "api_key": "eyJhbGciOiJIUzI"
}

If the user is not signed up, it will not be possible to login:

`STATUS 404`

```json

{"message": "user not found"}

````

Caso a senha estiver incorreta

`STATUS 400`

```json
{ "message": "Unauthorized" }
```

---

<br/>

<h2 align ='center'> Listar produtos </h2>
<br/>

`GET /products - FORMATO DA RESPOSTA - STATUS 200`

```json
[
  {
    "id": 1,
    "name": "Hamburguer",
    "category": "Sanduíches",
    "price": 14,
    "img": "https://i.ibb.co/fpVHnZL/hamburguer.png"
  },
  {
    "id": 2,
    "name": "X-Burguer",
    "category": "Sanduíches",
    "price": 16,
    "img": "https://i.ibb.co/djbw6LV/x-burgue.png"
  },
  {
    "id": 3,
    "name": "Big Kenzie",
    "category": "Sanduíches",
    "price": 18,
    "img": "https://i.ibb.co/FYBKCwn/big-kenzie.png"
  },
  {
    "id": 4,
    "name": "Fanta Guaraná",
    "category": "Bebidas",
    "price": 5,
    "img": "https://i.ibb.co/cCjqmPM/fanta-guarana.png"
  },
  {
    "id": 5,
    "name": "Coca",
    "category": "Bebidas",
    "price": 4.99,
    "img": "https://i.ibb.co/fxCGP7k/coca-cola.png"
  },
  {
    "id": 6,
    "name": "Fanta",
    "category": "Bebidas",
    "price": 4.99,
    "img": "https://i.ibb.co/QNb3DJJ/milkshake-ovomaltine.png"
  }
]
```

<h2 align ='center'> Pesquisar produtos </h2>
<br/>
 
 
`GET /products?Propriedade=NomeDoProduto - FORMATO DA REQUISIÇÃO`
 
`/products?name=Hamburguer`
 
Dando tudo certo, a resposta terá esse formato:
`FORMATO DA RESPOSTA - STATUS 200`
```json
[
{
"id": 1,
"name": "Hamburguer",
"category": "Sanduíches",
"price": 14,
"img": "https://i.ibb.co/fpVHnZL/hamburguer.png"
}
]
```
 
## Rotas que precisam de autorização 🔐
 
Rotas que necessitam de autorização devem ter no cabeçalho da requisição, o token no campo "Authotization":
`Authorization: Bearer {token}`
 
<h2 align ='center'> Adicionar produtos ao carrinho </h2>
<br/>

`POST /cart - FORMATO DA REQUISIÇÃO`
Além do token de autorização e dos dados do produto, é necessário informar a id (userId) do usuário.

```json{
"id": 1,
"name": "Hamburguer",
"category": "Sanduíches",
"price": 14,
"img": "https://i.ibb.co/fpVHnZL/hamburguer.png",
"userId": 2
}

Dando tudo certo, a resposta terá esse formato:
`FORMATO DA RESPOSTA - STATUS 201`
{
"id": 1,
"name": "Hamburguer",
"category": "Sanduíches",
"price": 14,
"img": "https://i.ibb.co/fpVHnZL/hamburguer.png",
"userId": 2
}
```

Caso o id esteja errado ou seja inválido apresentará o seguinte erro:
`STATUS 404`

<h2 align ='center'> Listando produtos do carrinho </h2>
<br/>
 
 
`GET /cart - FORMATO DA RESPOSTA - STATUS 200`
 
```json
[
{
"id": 1,
"name": "Hamburguer",
"category": "Sanduíches",
"price": 14,
"img": "https://i.ibb.co/fpVHnZL/hamburguer.png"
}
]
```
 
<h2 align ='center'> Deletar produtos do carrinho </h2>
<br/>
 
 
`DELETE /cart/IdDoProduto - FORMATO DA REQUISIÇÃO`
 
`/cart/1`
 
Dando tudo certo, a resposta terá esse formato:
`FORMATO DA RESPOSTA - STATUS 200`
```json
{}
```

Feito por [Luiza Schmidt Mescolotto](https://www.linkedin.com/in/luiza-schmidt-mescolotto/)
