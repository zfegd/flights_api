# Flights API
A simple project to create an API delivering data from the OpenFlights Airport Database, leveraging FastAPI and Docker technologies. The database is taken from OpenFlights' [airport database](https://raw.githubusercontent.com/jpatokal/openflights/master/data/airports.dat). No real use case, just a simple exercise. Uses wait-for-it script taken from [here](https://github.com/vishnubob/wait-for-it).

## Building
To get started with this project, you would need to have downloaded and installed Docker. Refer to [Docker's Getting Started Page](https://docs.docker.com/get-started/) for more details.  

Once Docker has been setup, navigate to this folder in terminal/command prompt. Using the Dockerfile, you can build a Docker Image using the command

```
docker build -t testimage .
```

I have tagged the image I just built with the name "testimage" for ease of reference. Once it has been built, you can use this image to create a container, with the following command

```
docker run -d --name appcontainer -p 80:80 testimage
```

This uses the image to run a container, mapping the container's port 80 to your computer's port 80, and this container has a name of "appcontainer". The container is now active and you can hit the endpoints via your browser or curl. For example, if you navigate to [localhost:80/city/london](localhost:80/city/london), you can find all the airports in London.  

When you want to stop the container, you can run the command below

```
docker stop appcontainer
```

In order to delete the container, you can do so with

```
docker rm appcontainer
```

You can do the same with the image, once the container has been deleted with the command

```
docker rmi testimage
```

For live re-deployment, we can leverage the start-reload implementation by the image, as seen [here](https://github.com/tiangolo/uvicorn-gunicorn-docker#development-live-reload). Upon building the image as detailed above, simply run with this command instead

```
docker run -dp 80:80 --name appcontainer -v $(pwd):/app testimage /start-reload.sh
```

If being used on Windows, simply replace "$(pwd)" with the absolute path of the directory in quotation marks. you can obtain this info with the command cd in terminal.
An example would be:

```
docker run -dp 80:80 --name appcontainer -v "C:\Users\zfegd\example\hereitis":/app testimage /start-reload.sh
```

Now, every change you make will be automatically updated in browser without needing to create a new container each time.  

If you wish to view the logs, you can use:

```
docker logs -f appcontainer
```

## Testing

Once you have built the image, you can call on the tests with the following command:

```
docker run -p 80:80 --name appcontainer -v $(pwd):/app testimage pytest
```

Similarly to above, on Windows you have to replace "$(pwd)" with the absolute path of the directory in quotation marks. An example would be:

```
docker run -p 80:80 --name appcontainer -v "C:\Users\zfegd\example\hereitis":/app testimage pytest
```

## Load Testing

We can load test by using locust, which can either be run locally or within a separate docker container in the same network. For the former, you have to run "pip install locust" to setup locust on your local machine. Then, you can "docker-compose up" and run the locust command once your appcontainer is up. To test with locust, navigate to the folder the locustfile.py is located and run:

```
locust -f locustfile.py
```

You can now head to localhost:8089 to interact with the locust web interface. For the second option, all you have to do instead is head to localhost:8089 after running:

```
docker-compose -f docker-compose.loadtest.yml up
```

## Using Docker Compose

With the docker-compose.yml file, we can use docker-compose to handle the processes instead. To faciltate debugging/querying mode vs testing mode, there are 2 docker-compose files included for either purpose. To handle the build and running process, use :

```
docker-compose up -d
```

Remove the "-d" flag to run in non-detached mode. This command above defaults to running docker-compose.yml, which contains the code for debugging/querying mode, as it allows live reload. To run the test instead, which is found in docker-compose.test.yml, run the following command:

```
docker-compose -f docker-compose.test.yml up
```

To remove the container, use the following command:

```
docker-compose down
```

You can use the "--rmi all" or "--rmi local" flag to remove the image as well.
Please remember to fill in the .envtocustomise file with the fields you want to use, as well as renaming it to .env , or calling it with the env-file flag during docker compose

# Monitoring and Debugging

When working with this codebase, you may have to monitor the way the containers are operating. You can monitor if the containers are running and their uptime with the command:

```
docker ps -a
```

When the containers are running, you can access it with the command:

```
docker exec -it <container name> bash
```

This allows you to access the terminal to debug, such as view the directory structure of the container.

When running operations including the mySQL database, it is important to note that schemas can persist across runs if the volume remainds mounted. This may be useful if no changes are made to the database, but not great if changes to the database initialisation have to be made. If you need to clear the volumes that are used to persist database data, you can use the -V flag when running docker down. WARNING: This will delete the data stored/changes made to the database besides the initialisation found in init.sql.

## TO NOTE 

Errors may occur when trying to use containers but programming with a Windows context. If so, remember to change your git config with regards to line endings, and clone the repository afresh.

When changing test cases, it is necessary to remove and build the images from scratch.

Sanitising input is important to note, but is covered within this context by mysql-connector, as stated [here](https://stackoverflow.com/questions/7540803/escaping-strings-with-python-mysql-connector).
