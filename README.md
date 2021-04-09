# Flights API
A simple project to create an API delivering data from the OpenFlights Airport Database, leveraging FastAPI and Docker technologies. The database is taken from OpenFlights' [airport database](https://raw.githubusercontent.com/jpatokal/openflights/master/data/airports.dat). No real use case, just a simple exercise.

## Building
To get started with this project, you would need to have downloaded and installed Docker. Refer to [Docker's Getting Started Page](https://docs.docker.com/get-started/) for more details.  

Once Docker has been setup, navigate to this folder in terminal/command prompt. Using the Dockerfile, you can build a Docker Image using the command 

```
docker build -t testimage .
```

I have tagged the image I just built with the name "testimage" for ease of reference. Once it has been built, you can use this image to create a container, with the following command

```
docker run -d --name testcontainer -p 80:80 testimage
```

This uses the image to run a container, mapping the container's port 80 to your computer's port 80, and this container has a name of "testcontainer". The container is now active and you can hit the endpoints via your browser or curl. For example, if you navigate to [localhost:80/city/london](localhost:80/city/london), you can find all the airports in London.  

When you want to stop the container, you can run the command below

```
docker stop testcontainer
```

In order to delete the container, you can do so with

```
docker rm testcontainer
```

You can do the same with the image, once the container has been deleted with the command 

```
docker rmi testimage
```

For live re-deployment, we can leverage the start-reload implementation by the image, as seen [here](https://github.com/tiangolo/uvicorn-gunicorn-docker#development-live-reload). Upon building the image as detailed above, simply run with this command instead

```
docker run -dp 80:80 --name testcontainer -v $(pwd):/app testimage /start-reload.sh
```

If being used on Windows, simply replace "$(pwd)" with the absolute path of the directory in quotation marks. you can obtain this info with the command cd in terminal.
An example would be:

```
docker run -dp 80:80 --name testcontainer -v "C:\Users\zfegd\example\hereitis":/app testimage /start-reload.sh
```

Now, every change you make will be automatically updated in browser without needing to create a new container each time.  

If you wish to view the logs, you can use:

```
docker logs -f testcontainer
```

## Testing

Once you have built the image, you can call on the tests with the following command:

```
docker run -p 80:80 --name testcontainer -v $(pwd):/app testimage pytest
```

Similarly to above, on Windows you have to replace "$(pwd)" with the absolute path of the directory in quotation marks. An example would be:

```
docker run -p 80:80 --name testcontainer -v "C:\Users\zfegd\example\hereitis":/app testimage pytest
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

When running operations including the mySQL database, it is important to note that schemas can persist across runs if the volume remainds mounted. This may be useful if no changes are made to the database, but not great if changes to the database initialisation have to be made. To replace the volumes with new ones, you can use the -v flag either when running "down" or "up" commands of docker-compose.
