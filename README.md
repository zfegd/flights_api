# Flights API
A simple project to create an API delivering data from the OpenFlights Airport Database, leveraging FastAPI and Docker technologies. The database is taken from OpenFlights' [airport database](https://raw.githubusercontent.com/jpatokal/openflights/master/data/airports.dat). This project has no real use case, just a simple exercise. Uses wait-for-it script taken from [here](https://github.com/vishnubob/wait-for-it).

## Getting Started

After cloning the dataset, you have to ensure that the project is setup correctly. To get started with this project, you would need to have downloaded and installed Docker. Refer to [Docker's Getting Started Page](https://docs.docker.com/get-started/) for more details.  

To setup the dataset, download the file [here](https://raw.githubusercontent.com/jpatokal/openflights/master/data/airports.dat) and put the .dat file in the app/data folder. Alternatively, navigate to the app/data folder and run "make".  

For privacy reasons, the passwords and usernames in certain areas have been filled with placeholder values. Please fill in the data in .envtocustomise and rename the file to ".env", as well as change the values in "app/data/configtocustomise.py" and rename the fille to "config.py"

## Building

Once Docker has been setup, navigate to this folder in terminal/command prompt. You can instantly get an instance of this API running with the command

```
docker compose up
```

This creates a docker network containing the database which loads the airport dataset data, and the API for you to query from. For example, if you navigate to [localhost:80/city?city_name=london](localhost:80/city?city_name=london), you can find all the airports in London. To see the OpenAPI Documentation, you can navigate to [localhost:80/docs](localhost:80/docs).  

When you want to delete the network and its containers, you can run the command below:

```
docker compose down
```

You can also run it with the -v flag to remove the volume which helps persist the database info. If you want to remove the images as well, you can run:

```
docker compose down --rmi all
```

If you wish to run the API in live debug mode to see your changes in real-time, you can use the debug version of the docker compose file. This can be done by running:

```
docker compose -f docker-compose.debug.yml up
```


## Testing

There is a separate pipeline to use for testing, by using the docker-compose.test.yml file instead.

```
docker compose -f docker-compose.test.yml up
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

# Monitoring and Debugging

When working with this codebase, you may have to monitor the way the containers are operating. You can monitor if the containers are running and their uptime with the command:

```
docker ps -a
```

If you wish to view the logs of a container, you can use:

```
docker logs -f <container name>
```

When the containers are running, you can access it with the command:

```
docker exec -it <container name> bash
```

This allows you to access bash to debug, such as view the directory structure of the container. The container names follow the format of <repo name>_<container>_<number spawned>, such as flights_api_app_1.  

When running operations including the mySQL database, it is important to note that schemas can persist across runs if the volume remainds mounted. This may be useful if no changes are made to the database, but not great if changes to the database initialisation have to be made. If you need to clear the volumes that are used to persist database data, you can use the -V flag when running docker down. WARNING: This will delete the data stored/changes made to the database besides the initialisation found in init.sql.

## TO NOTE

Errors may occur when trying to use containers but programming with a Windows context. If so, remember to change your git config with regards to line endings, and clone the repository afresh.

When changing test cases, it is necessary to remove and build the images from scratch.

Sanitising input is important to note, but is covered within this context by mysql-connector, as stated [here](https://stackoverflow.com/questions/7540803/escaping-strings-with-python-mysql-connector).
