# fibonacci_seq_app

A Django web app to calculate the fibonacci sequence for all the terms up to the given nth term. 
The ouput sequence is saved in an SQLite database and used to prevent redundant calculations. 

The maximum nth term that will produce a sequence is set to 900 to help prevent crashing due to max recursion depth limit. 

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

## Folder structure:

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