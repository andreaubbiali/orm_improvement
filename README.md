# orm_improvement

Repository to trace improvements about ORM, second level cache and distributed database.

# use of venv

https://docs.python.org/3/tutorial/venv.html

create a directory (if doesn't exist) where to place libraries for the project 
```bash
python -m venv {project}
```

```bash
source {project}/bin/activate
```


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