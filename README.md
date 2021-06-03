# Running Docker

##Change Volumes docker
``put in line 9 of docker-compose.yml your path``

##Linux
``docker-compose up -d --build``

#Running the API
## Entering the Python Docker Container
1. Look for your docker id with ``docker ps``
2. Copy your docker id and run ``docker exec -it <your-docker-id> sh``
## Another method
1. docker-compose run tarea

## Creating the database tables
1. Move to ``/usr/src/api/``
2. Run 
 ```
 python manage.py makemigrations Tareas
 python manage.py migrate Tareas
 ```

##Running the API
1. Move to ``/usr/src/api``
2. Run `` python3 manage.py runserver 0.0.0.0:8080 ``

Change Prueba/settings.py 
----ALLOWED_HOSTS = ['172.21.0.2']
to your docke ip

This creates a development server that runs in ``http://<docker-ip>:8080``