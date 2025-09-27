# Shrimp Backend

## Setup

You can run the backend in **two ways**:

1. **Local FastAPI server + DB Docker container**
2. **Full Docker setup (Backend + DB in containers)**

---

### Environment Variables

Create a `.env` file in the root directory:

```env
POSTGRES_HOST=<localhost|db> # localhost for db-only, db for full docker setup
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

---

## Local FastAPI + DB Docker Container


1. Install Python dependencies:

```bash
pip install -r requirements.txt
```

2. Start only the database container:

```bash
make db-only
```

3. Apply Alembic migrations to set up the database:

```bash
make migrate
```

4. Load data:

```bash
make load-data
```

5. Run the FastAPI server locally:

```bash
make dev
```

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
| `make db-only`                     | Start only the Postgres container for local FastAPI use (local FastAPI + DB container).         |
| `make stop`                   | Stop all running containers.                                     |
| `make reset`                  | Stop containers and remove all volumes, images, and data.        |
| `make migrate`                | Apply Alembic migrations to the DB.               |
| `make revision m="<message>"`       | Generate a new Alembic migration.                 |
| `make dev`       | Run local FastAPI server.                 |


---

API will be available at:

[http://localhost:8000/docs#/](http://localhost:8000/docs#/)
