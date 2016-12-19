# wordpress-development

Starting point for local Wordpress development.

## Getting started

### Start the Docker bundle

    docker-compose up

Go through the installation at http://localhost:8000/

### Stop the Docker bundle

    docker-compose down

This will destroy the containers, but keeps the data:

```
Stopping wordpressdevelopment_wordpress_1 ... done
Stopping wordpressdevelopment_db_1 ... done
Removing wordpressdevelopment_wordpress_1 ... done
Removing wordpressdevelopment_db_1 ... done
Removing network wordpressdevelopment_default
```

## Importing existing database and assets

In order to perform a database import, find the container name of the MySQL instance (e.g. `wordpressdevelopment_db_1`):

    docker ps

Example output:

```
CONTAINER ID        IMAGE               COMMAND                  CREATED              STATUS              PORTS                  NAMES
17e972a1d193        wordpress:latest    "docker-entrypoint.sh"   About a minute ago   Up About a minute   0.0.0.0:8000->80/tcp   wordpressdevelopment_wordpress_1
06b2337e5e0c        mysql:5.7           "docker-entrypoint.sh"   2 minutes ago        Up About a minute   3306/tcp               wordpressdevelopment_db_1
```

### Import existing database

    docker exec -i wordpressdevelopment_db_1 mysql -uwordpress -pwordpress wordpress < dump.sql

## Dump database

    docker exec -i wordpressdevelopment_db_1 sh -c 'exec mysqldump --all-databases -uwordpress -pwordpress'
