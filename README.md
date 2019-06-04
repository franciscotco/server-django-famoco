# server-django-famoco
Rest server POST/GET in Django

```
The project run a server write in django and deploy a Rest API on localhost on the port 8000

You have a GET and a POST method available on '/api/applications'

you can access to them on 'http://localhost:8000/api/applications/'
```


Clone the project on your computer with the git command:

`git clone git@github.com:franciscotco/server-django-famoco.git`

How run the server ?

You can use the docker file to deploy the server on docker[^1] or made install by yourself[^2]

### 1 Docker Install

Make sur you have install docker on your computer, if not [install here](https://docs.docker.com/install/linux/docker-ce/ubuntu/) do not forget to select the install for your own system.

Go at the root of the repository where the Dockerfile and build your docker image:

`sudo docker build . -t server-django`

Run your docker:

`sudo docker run -ti -p 8000:8000 server-django:latest`

### 2 Manual Install

For this project I’m using native virtual environment:

`python3 -m venv server-django-famoco`

Once cloned move inside the new folder and activate the environment:

`cd server-django-famoco/ && source bin/activate`

Pull in the dependencies: install Django and Django REST framework by running:

`pip install django djangorestframework`

Go in the folder 'rest-api-django/project':

`cd rest-api-django/project`

Launch the migration of the models in the database:

`python manage.py makemigrations androidPackageManager && python manage.py migrate`

When the installation ends you’re ready to run the server:

`python manage.py runserver`
