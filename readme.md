## Simple FastAPI + sync raw SQL project base for beginners

### Prerequisites

- Docker
- Docker Compose

After clonning repository, specify database credentials in ```.env``` file and start the project with ```docker-compose --build```.

Go to ```scripts/db``` and write down your database architecture in ```init.sql```.

To execute ```init.sql``` run the following command:
```docker-compose exec -it db psql -U <your_db_user> -d <your_db_name> -f /var/lib/postgresql/scripts/init.sql```