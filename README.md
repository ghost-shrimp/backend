# Shrimp Backend

## Setup

### Environment Variables

Create a `.env` file in the root directory:

```env
POSTGRES_HOST=db
POSTGRES_USER=<db-user>
POSTGRES_PASSWORD=<db-password>
POSTGRES_DB=<db-name>
POSTGRES_PORT=<db-port>
```

---

## Full Docker Setup (Backend + DB in Containers)

1. Build and start containers:

```bash
make up
```

2. Apply Alembic migrations to set up the database (first time only):

```bash
make migrate
```

3. Load data:

```bash
make load-data
```

### API will be available at:

[http://localhost:8000/docs#/](http://localhost:8000/docs#/)

---
## Database Migrations 

* Create a new migration:

```bash
make revision m="<message>"
```

* Apply migrations:

```bash
make migrate
```

---

## Makefile

| Command                       | Description                                                      |
| ----------------------------- | ---------------------------------------------------------------- |
| `make up`                     | Build and start Docker containers (Docker setup).          |
| `make stop`                   | Stop all running containers.                                     |
| `make reset`                  | Stop containers and remove all volumes, images, and data. Warning: this will delete everything       |
| `make migrate`                | Apply Alembic migrations to the DB.               |
| `make revision m="<message>"`       | Generate a new Alembic migration.                 |     



