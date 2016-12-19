# wordpress-development

Starting point for local Wordpress development.

## Start the Docker bundle

    docker-compose up

Go through the installation at http://localhost:8000/

## Stop the Docker bundle

    docker-compose down

This will destroy the containers, but keeps the data:

```
Stopping wordpressdevelopment_wordpress_1 ... done
Stopping wordpressdevelopment_db_1 ... done
Removing wordpressdevelopment_wordpress_1 ... done
Removing wordpressdevelopment_db_1 ... done
Removing network wordpressdevelopment_default
```

## Import existing database

    docker exec -i db mysql -uwordpress -pwordpress wordpress < dump.sql

## Dump database

    docker exec -i wordpressdevelopment_db_1 sh -c 'exec mysqldump --all-databases -uwordpress -pwordpress'
