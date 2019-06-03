# server-django-famoco
Rest server POST/GET in Django

Clone the project on your computer with the git command:

`git clone git@github.com:franciscotco/server-django-famoco.git`

For this project I’m using native virtual environment:

`python3 -m venv server-django-famoco`

Once cloned move inside the new folder and activate the environment:

`cd server-django-famoco/ && source bin/activate`

Pull in the dependencies: install Django and Django REST framework by running:

`pip install django djangorestframework`

Launch the migration of the models in the database:

`python manage.py makemigrations androidPackageManager && python manage.py migrate`

When the installation ends you’re ready to run the server.
