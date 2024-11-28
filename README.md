# Создание своего приложения с подключением к БД

**git clone**

**Отредактировать значения полей в DB_CONFIG: user, password**

**sudo -u <superuser> psql**

**CREATE DATABASE task_management;**

**\q**

**psql -U <superuser> -d task_management -W -f <path>/Creating-an-application-with-a-connection-to-a-databasen/Task/src/setup.sql**

**cd Task/src**

**python3 main.py**
