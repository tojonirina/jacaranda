# jacarandaV0.1

A simple web application to manage stock, staff, absence, computer with Django and MariaDB

## Technos

Framework: Django 2.2
Database: MariaDB 10.4.17

## Features

- Application admin management
- Stock management
- Staff management
- Absences management
- Computers management

## Futures fonctionnalities

- Tchat system
- Password management
- Checking management

## Installation

Make sure that you have python 3.7 or later in you computer or get the python installer here (https://www.python.org/)

- After installing python, create a virtual environement with:

 ```sh
 python3 -m venv myvirtualenv
 ```

- Activate your virtual environement with:

```sh
 . myvirtualenv/bin/activate
```

- Install django 2.2:

```sh
 python3 -m pip install django=2.2
```

- Get source code of project:

```sh
git clone https://github.com/tojonirina/jacaranda.git 
cd jacaranda/
```

- Run django server:

```sh
 python3 manage.py runserver
```

The app will be running on http://localhost:8000
