# fibonacci_seq_app
* Note: I did this for a take home coding assignment. 

A Django web app to calculate the fibonacci sequence for all the terms up to the given nth term. 
The ouput sequence is saved in an SQLite database and used to prevent redundant calculations. 

The maximum nth term limit is set 1000 in the html form. 

I chose Django because it comes with a lot of included functionality, like the Django ORM, it's scalable and relatively easy to get started with. 


## Start Up Instructions

```bash
cd cv_fibonacci_seq
python -m venv env
source env/bin/activate
pip install -r requirements.txt
cd fibonacci_seq_project
python manage.py runserver
```


## Run Test:
```bash
python manage.py test
```


## Notes:
When working with sqlite3 and large data such as big fibonacci Sequences
use PRAGMA auto_vacuum = 2; when deleting the fibonacci_seq_app_fibonaccinumber table 

```bash
PRAGMA auto_vacuum; // check status, if 0 set to 2
PRAGMA auto_vacuum = 2;
```
```bash
delete from fibonacci_seq_app_fibonaccinumber;
select * from fibonacci_seq_app_fibonaccinumber;
```

## Folder structure:
```bash
├── README.md
├── fibonacci_seq_project
│   ├── db.sqlite3
│   ├── fibonacci_seq_app
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── calculate_fibonacci.py
│   │   ├── migrations
│   │   │   ├── 0001_initial.py
│   │   │   └── __init__.py
│   │   ├── models.py
│   │   ├── templates
│   │   │   ├── fibonacci_input.html
│   │   │   └── fibonacci_output.html
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── fibonacci_seq_project
│   │   ├── __init__.py
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   └── manage.py
└── requirements.txt
```