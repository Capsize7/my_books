# Django 4.0+ My Books

This is my project powered by Django 4.0+ about my read books. Accordingly it, I tried to apply my knowledge and skills. Most points can be improved, which I will do. Some solutions have been added to demonstrate understanding of the work, and to try to better understand the some features of exploring theme. Do not be so strict :)
 
## Features

- Django 4.0+
- Uses [Pipenv](https://github.com/kennethreitz/pipenv) - the officially recommended Python packaging tool from Python.org.
- Development settings with [django-configurations](https://django-configurations.readthedocs.org).
- Get value insight and debug information while on Development with [django-debug-toolbar](https://django-debug-toolbar.readthedocs.org).
- Collection of custom extensions with [django-extensions](http://django-extensions.readthedocs.org).
- PostgreSQL database
- Let`s Encrypt certificate for https protocol
- NGINX
- Gunicorn

## How to install
```
git clone https://github.com/Capsize7/my_books # in the terminal
pip install -r requirements.txt # in the terminal
There is a '.env' file with some keys which you should replace on your correct data
Set up the database (for example postgreSQL with name of db 'books', user 'books' and password '1')
python manage.py makemigrations # in the terminal
python manage.py migrate # in the terminal
python manage.py test books.tests # in the terminal to check that all tests is passing
```

## License

The MIT License (MIT)
