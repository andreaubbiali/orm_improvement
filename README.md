# orm_improvement

Repository to trace improvements about ORM, second level cache and distributed database.

# use of venv

https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/

create the venv directory in the project
```bash
python3 -m venv .venv
```

activate virtual environment
```bash
source .venv/bin/activate
```

to be sure you are using the virtual environment right, use this command:
```bash
which python
```
and you should see `.venv/bin/python` in the path

# run the server

```bash
python manage.py runserver
```

## create a new app

```bash
python manage.py startapp {appName}
```

## install requirements and dependencies

```bash
pip install -r requirements.txt
```


# Docker

### Create Postgres container

```bash
docker run -d \
  --name orm_postgres_container \
  --network orm \
  -e POSTGRES_USER=postgres \
  -e POSTGRES_PASSWORD=postgres \
  -e POSTGRES_DB=orm \
  -p 5432:5432 \
  postgres
```


### cosa fare

creo un gestionale di un ecommerce super grande
tanti clienti possono guardare i prodotti e vedere le disponibilità