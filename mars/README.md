# PostgreSQL for Django

1. Создаем виртуальное окружение Django
2. Устанавливаем PostgreSql
3. Далее в терминале нам необходимо установить драйвер для работы с СУБД: pip install psycopg2 
4. python.exe -m pip install --upgrade pip
5. В меню пуск введите в поиске pgAdmin, подключитесь по созданному паролю при установке.
6. Теперь нам необходимо создать базу данных для нашего сайта (нажать левой кнопкой мыши на Базы Данных и создать базу данных):
7. Далее нам необходимо изменить конфигурационный файл settings.py, в нём мы добавим новые настройки для базы данных вместо старых:
***
DATABASES = {

      'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '<dbname>',
        'USER': 'postgres',
        'PASSWORD': '<password>',
        'HOST': 'localhost',
        'PORT': 5432,
    }
}
***
Таким образом мы настроим Django на работу с Postres

8. Далее после установки проводим миграции и создаем суперпользователя:
   1. py manage.py makemigrations
   2. py manage.py migrate  
   3.  py manage.py createsuperuser
        1. user: admin
       2. password: admin123