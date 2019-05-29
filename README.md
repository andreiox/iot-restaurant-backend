# iot-restaurant-backend

Back-end logic for the iot project pay-with-rfid

## Instalation

With conda

```shell
conda create --name venv --file requirements.txt
```

## How to run the server

First set up your env by copying .env.example to .env and giving the values of the variables

Than create your database and follow the following steps:

```shell
conda activate venv
python manage.py migrate
python manage.py runserver
```

Then access <http://127.0.0.1:8000/api/>

## TODO

### Entidades

1. **Clients 🗸**
    - id
    - rfid
    - name
    - balance

2. **Transactions 🗸**
    - id
    - date
    - value
    - client_id

### Funcionalidades

1. **Escrever models 🗸**
2. **Migrate models 🗸**
3. **Definir custom endpoints 🗸**
4. **Integrar docker ✕**
5. **Subir AWS 🗸**
