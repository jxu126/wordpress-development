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

#### Replace URLs in the database dump

    cat dump.sql | python utils/modify_database_dump.py --old-url <OLD URL> > modified-dump.sql

#### Import from modified dump

    docker exec -i wordpressdevelopment_db_1 mysql -uwordpress -pwordpress wordpress < modified-dump.sql

### Dump database

    docker exec -i wordpressdevelopment_db_1 sh -c 'exec mysqldump --all-databases -uwordpress -pwordpress'

## Deploying to live site

### Deploy new version

If your work is already committed:

    git ftp push

To ignore warning about uncommitted work:

    git ftp push --force

### Set up git-ftp

We are using [`git-ftp`](https://github.com/git-ftp/git-ftp/blob/master/man/git-ftp.1.md) to manage deployments to the live FTP server.

Install `git-ftp` (requires [`homebrew`](http://brew.sh/)):

    brew install git
    brew install curl --with-ssl --with-libssh2
    brew install git-ftp

Configure it using:

    git config git-ftp.user <FTP USER>
    git config git-ftp.url ftpes://<FTP SERVER>/www/wp-content/themes/<THEME NAME>
    git config git-ftp.syncroot wordpress/wp-content/themes/<THEME NAME>
    git config git-ftp.password *******

which should result in the following inside `.git/config`:

    [git-ftp]
	    user = <FTP USER>
	    url = ftpes://<FTP SERVER>/www/wp-content/themes/<THEME NAME>
        syncroot = wordpress/wp-content/themes/<THEME NAME>
	    password = *******

Finally, to activate `git-ftp`, run:

    git ftp init
