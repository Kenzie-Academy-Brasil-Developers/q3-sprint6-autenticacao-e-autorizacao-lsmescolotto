# Autorization and Authentication

## **Technologies**

This project was developed using the following technologies:

- [Python](https://docs.python.org/3/)
- [PostgreSQL](https://www.postgresql.org/docs/)
- [Flask](https://flask.palletsprojects.com/en/2.1.x/)
- [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)
- [Flask-JWT-Extended](https://flask-jwt-extended.readthedocs.io/en/stable/)
- [Flask-HTTPAuth](https://flask-httpauth.readthedocs.io/en/latest/)
- [Environs](https://pypi.org/project/environs/)

## **Prerequisites**

<h2 align ='center'> Install: </h2>
- Python 3.9
- Pip library

## **To get started**

### Follow the steps:

<h2 align ='center'> Clone into the repository and go into project's folder: </h2>
```bash
$ git clone https://github.com/Kenzie-Academy-Brasil-Developers/q3-sprint6-autenticacao-e-autorizacao-lsmescolotto
$ cd q3-sprint6-autenticacao-e-autorizacao-lsmescolotto
```

<h2 align ='center'> Create virtual enviroment: </h2> 
  ```bash
  $ python -m venv venv
  ```

<h2 align ='center'> Activate virtual enviroment: </h2>
 ```
  $ source venv/bin/activate
  ```

<h2 align ='center'> Install libraries: </h2>
```bash
$ pip install -r requirements.txt
```

<h2 align ='center'> Run flask: </h2> 
```bash
$ flask run
```

<h2 align ='center'> Start sending requests: </h2>

- Use an API request sending platform like [Insomnia](https://docs.insomnia.rest/#)

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

```

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
`POST /signin - RESPONSE FORMAT - STATUS 201`
Flask-JWT-Extended

```json
{
  "accessToken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImphbmVkb2VAbWFpbC5jb20iLCJpYXQiOjE2NDMyNTAwMDAsImV4cCI6MTY0MzI1MzYwMCwic3ViIjoiMyJ9.z90xWRIE7pfKRsw-YqqqUtRxBZGtBPgSZ63yqW04qSc"
}
```

Flask-HTTPAuth

```json
{
  "api_key": "eyJhbGciOiJIUzI"
}
```

If the user is not signed up, it will not be possible to login:

`STATUS 404`

```json
{"message": "user not found"}
```

If the password is not corret:

`STATUS 400`

```json
{ "message": "Unauthorized" }
```

---

<br/>

## Authorization required routes 🔐

These routes need to have the token in the request Header "Authotization" field:
`Authorization: Bearer {token}`

<h2 align ='center'> Update user </h2>
<br/>

`PUT - REQUEST FORMAT`

```json
{
  "name": "Johana",
  "last_name": "Doe",
  "email": "johanadoe@mail.com",
  "password": "123456"
}
```

If the request is corret, the user will be updated:
`PUT - RESPONSE FORMAT - STATUS 200`

```json
{
  "name": "Johana",
  "last_name": "Doe",
  "email": "johanadoe@mail.com",
  "password": "123456"
}
```

If the user is not found:
`STATUS 404`

```json
{ "message": "user not found" }
```

If the token is not corret:

`STATUS 400`

```json
{ "message": "Unauthorized" }
```

<h2 align ='center'> Get user </h2>
<br/>

`GET - REQUEST FORMAT`
No Body

`GET - REPONSE FORMAT - STATUS 200`

```json
{
  "email": "janedoe@mail.com",
  "last_name": "Doe",
  "name": "Jane"
}
```

If the user is not found:
`STATUS 404`

```json
{ "message": "user not found" }
```

If the token is not corret:

`STATUS 400`

```json
{ "message": "Unauthorized" }
```

<h2 align ='center'> Delete user </h2>
<br/>

`DELETE - REQUEST FORMAT`
No Body

If the request is corret, the user will be deleted:
`RESPONSE FORMAT - STATUS 204`
No Body

If the user is not found:
`STATUS 404`

```json
{ "message": "user not found" }
```

If the token is not corret:

`STATUS 400`

```json
{ "message": "Unauthorized" }
```

Developed by [Luiza Schmidt Mescolotto](https://www.linkedin.com/in/luiza-schmidt-mescolotto/)
````
