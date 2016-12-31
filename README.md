# takoyaki-memo

## setup

* install Python 2.7

### install libs

* get Python modules
```bash
$ cd takoyaki_memo
$ mkdir lib
$ pip install -t lib/ -r requirements.txt
```

### create passwords

* create db configs
```bash
$ cd takoyaki_memo
$ vi config.py
====
## FIX_ME
import os

# The secret key is used by Flask to encrypt session cookies.
SECRET_KEY = 'FIX_ME'

DATA_BACKEND = 'FIX_ME'
PROJECT_ID = 'FIX_ME'

CLOUDSQL_USER = 'FIX_ME'
CLOUDSQL_PASSWORD = 'FIX_ME'
CLOUDSQL_DATABASE = 'FIX_ME'

CLOUDSQL_CONNECTION_NAME = 'FIX_ME'
SQLALCHEMY_TRACK_MODIFICATIONS = False

## Local is used cloud_sql_proxy
LOCAL_SQLALCHEMY_DATABASE_URI = (
    'mysql+mysqldb://{user}:{password}@127.0.0.1:3306/{database}').format(
        user=CLOUDSQL_USER, password=CLOUDSQL_PASSWORD,
        database=CLOUDSQL_DATABASE)

# @GAE Instance.
LIVE_SQLALCHEMY_DATABASE_URI = (
    'mysql+mysqldb://{user}:{password}@/{database}?unix_socket=/cloudsql/{connection_name}').format(
        user=CLOUDSQL_USER, password=CLOUDSQL_PASSWORD,
        database=CLOUDSQL_DATABASE, connection_name=CLOUDSQL_CONNECTION_NAME)

if os.environ.get('GAE_INSTANCE'):
    SQLALCHEMY_DATABASE_URI = LIVE_SQLALCHEMY_DATABASE_URI
else:
    SQLALCHEMY_DATABASE_URI = LOCAL_SQLALCHEMY_DATABASE_URI

====
```

## run local

* run app on VM
```bash
$ cloud_sql_proxy -instances=takoyaki-memo:asia-northeast1:takoyaki-memo-db=tcp:3306
$ cd takoyaki_memo
## run local and cloud_sql
$ python main.py
```

## deploy

* Deploy Google App Engine
```bash
$ gcloud app deploy app.yaml
```
