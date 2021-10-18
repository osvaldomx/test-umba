# ML TEST UMBA

Machine Learning Test for Umba.

## Instructions to set the development environment from scratch
### Stage 1
Install requirements.txt
```console
pip install requirements.txt
```
run
```console
python scripts/seed.py
```
this command will create a SQLite database and will populate with by default 150 users from GitHub.

Change number of records with flag `-t` or `--total`
```console
python scripts/seed.py -t <amount>
python scripts/seed.py --total <amount>
```

Fot unit test
```console
python scripts/test.py
```

### Stage 2
Run
```console
python app/app.py
```
Set up for the first time. Populate databases with default 150 users from GitHub
```http
localhost:5000/setup
```
Set up for the first time. Populate databases with `total` records
```http
localhost:5000/users?total=<amount>
```
View grid with default 25 records page 1
```http
localhost:5000/users
```
Modify pagination
```http
localhost:5000/users?pagination=<amount>
```
Through pages
```http
localhost:5000/users/<int:page>
```

### Stage 3
Set up for the first time. Populate databases with default 150 users from GitHub
```http
localhost:5000/setup
```
Set up for the first time. Populate databases with `total` records
```http
localhost:5000/setup?total=<amount>
```
View grid with default 25 records page 1
```http
localhost:5000/users
```
Modify pagination
```http
localhost:5000/users?pagination=<amount>
```
Through pages
```http
localhost:5000/users/<int:page>
```
Filter by username or id
```http
localhost:5000/users?<id= | username=>
```
Order by id or type
```http
localhost:5000/users?order_by=<id= | type=>
```

## Deployment instructions
### Stage 4
For deploy Stage 4:
Download docker image code
```console
$ docker pull osvaldomx89/test-umba
```
Download docker image postgres
```console
$ docker pull osvaldomx89/postgres
```
Run
```console
$ docker-compose up
```
#### Endpoints
```http
localhost:5000/api/users/profile/<int:page>
```
