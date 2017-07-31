# Python web application running on Docker Compose. The web application uses Flask framework with Redis database.

Prerequisites

1.  OS: Ubuntu

2.  Docker-ce version: Docker version 17.06.0-ce

    -   [https://docs.docker.com/engine/installation/linux/docker-ce/ubuntu/ -
        prerequisites](https://docs.docker.com/engine/installation/linux/docker-ce/ubuntu/#prerequisites)

3.  Docker Compose: docker-compose version 1.15.0

    -   <https://docs.docker.com/compose/install/>

4.  Clone the repository onto project directory

    -   https://github.com/nitish2611/Python-web-application-docker-compose.git

File Information:

1.  App.py: Flask application

    1.  Connects to Redis database

    2.  Checks if Redis is running else 500 exception handled and logged
        in redis.log

    3.  Redis.get reads greeting string and returns the value

    4.  Python logging module handles the error logging.

    5.  Types of errors handled

        1.  500 server error(Redis process stops before request
            is served). Traceback enabled and logged in redis.log

        2.  404 client error: suitable error response message is sent
            to client.

        3.  301 redirection defaults to ‘/’ URL path.

2.  Requirements.txt: Installs application dependencies

    1.  Flask

    2.  Redis

3.  Dockerfile: Builds a docker image

    1.  Build image

    2.  Set working directory

    3.  Install python dependencies

    4.  Set default command for container

4.  Docker-compose.yml: Compose file to define web and redis service and
    run in an isolated environment

    1.  Use image built from Dockerfile

    2.  Configure ports for container

    3.  Defines service web and redis

Build and run application using compose

1.  Docker-compose up
    1.  redis_1  | 1:M 31 Jul 07:01:22.490 * DB loaded from disk: 0.000 seconds
        redis_1  | 1:M 31 Jul 07:01:22.490 * Ready to accept connections
        web_1    |  * Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)
2.  In browser or curl http://127.0.0.1:8080


