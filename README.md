# process:

```
virtualenv venv
sudo pac man -S mariadb
sudo systemctl start mysqld
sudo mysql_secure_installation
mysql -u root -p
mysql > CREATE USER 'prv'@'localhost' IDENTIFIED BY 'lala'
mysql > GRANT ALL ON prvdb.* TO 'prv'@'localhost';
mysql > CREATE DATABASE prvdb CHARACTER SET utf8;
mysql > quit
echo '[client]
database = prvdb
user = prv
password = lala
default-character-set = utf8' > prvdb.cnf
./venv/bin/pip install MySQL-python django
```

# dev log
```
./venv/bin/django-admin.py startproject proveit
```

edit settings.py

```
./venv/bin/python ./proveit/manage.py migrate
./venv/bin/python ./proveit/manage.py runserver
./venv/bin/python ./proveit/manage.py startapp app
```

edit models.py

```
./venv/bin/python ./proveit/manage.py makemigrations polls
./venv/bin/python ./proveit/manage.py migrate
```
