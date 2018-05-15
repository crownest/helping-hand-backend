# Development


## Required Packages

**Pip**
```bash
apt-get update
apt-get python-pip
```

**Virtualenv**
```bash
apt-get update
apt-get virtualenv
```


## Steps for running the project

**Create project and change directory**
```bash
mkdir helping-hand-backend
cd helping-hand-backend
```

**Create virtualenv with python3**
```bash
virtualenv -p python3 env
```

**Make active virtualenv**
```bash
source env/bin/activate
```

**Get source code**
```bash
git clone https://github.com/crownest/helping-hand-backend.git source (Use HTTPS)
git clone git@github.com:crownest/helping-hand-backend.git source     (Use SSH)
```

**Change directory and branch**
```bash
cd source
git checkout staging
```

**Create required files**
```bash
cp helpinghand/settings/local-dist.py helpinghand/settings/local.py
touch helpinghand/settings/secrets.py
```

Note: Please ask secret credentials from admin.

**Install requirements**
```bash
pip install -r requirements/staging.txt
pip install -r requirements/extra.txt
```

**Create database**
```bash
./manage.py migrate
```

**Language**
```bash
./manage.py compilemessages
```

**Run project**
```bash
./manage.py runserver 0.0.0.0:8000 (http://127.0.0.1:8000)
```
