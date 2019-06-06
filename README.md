# iot-restaurant-backend

## **introduction**

This is a **college assignment** with the objective of make the payments of a restaurant with Internet of Things concepts.

This repo it's the backend that provides a restful api for the other projects to access/create the data.

## **other parts of the project**

1. [NodeMCU configuration and code](https://github.com/andreiox/iot-restaurant-nodemcu)
2. [App made with Ionic 4](https://github.com/andreiox/iot-restaurant-app)

## **app description**

### **endpoints**

- GET /api/clients/ *(queryparams=rfid, cpf)*

- GET /api/transactions/ *(queryparams=client_id)*

- POST /api/clients

```json
{
    "cpf": "00000000000",
    "rfid": "3789384224",
    "name": "Andre Macedo",
}
```

- POST /api/make_transaction

```json
{
    "value": -10,
    "rfid": "3789384224"
}
```

## **development**

### **instalation**

With conda

```shell
conda create --name venv --file requirements.txt
```

### **how to run the server**

First set up your env by copying .env.example to .env and giving the values of the variables

Than create your database and follow the following steps:

```shell
conda activate venv
python manage.py migrate
python manage.py runserver
```

Then access <http://127.0.0.1:8000/api/>
