# {{cookiecutter.project_name}}

{{cookiecutter.project_description}}

This is a [Brevia API](https://github.com/brevia-ai/brevia) project.

## Quickstart

[Poetry](https://python-poetry.org/docs/#installation) is required to setup this API. It is also recommended to use virtualenv inside the project folder (you can simply do that with `poetry config virtualenvs.in-project true`) we assume this configuration from now on, but you are free to use your usual virtualenv configuration.

## Setup

* install the dependencies by running `poetry install`, a virtualenv will automatically be created in the `.venv` folder
* activate the virtualenv by running the `poetry shell` command.
* check the `.env` file where environment variables are stored, especially `BREVIA_ENV_SECRETS`, where you cna store LLM providers secrets (like OPENAI_API_KEY, COHERE_API_KEY etc...), and `PGVECTOR_*` for the database connection, see the [Database](#database) section

## Database

If you have a PostgreSQL instance with the `pg_vector` extension available, you are ready to go. Otherwise, you can use the provided Docker Compose file.

Simply run `docker compose up` to start a PostgreSQL database with `pg_vector`.
You can also run the embedded [`pgAdmin`](https://www.pgadmin.org) admin tool by running `docker compose --profile admin up` to start both the postgres+pgvector and pgadmin Docker images.
Open `pgadmin` in your browser at http://localhost:4000

The `4000` port is configurable via the `PGADMIN_PORT` environment variable in the `.env` file.

## Migrations

Before using Brevia, you need to run the migrations script to create or update the initial schema. Use the following command from the virtual environment:

```bash
db_upgrade
```

This will run migrations using [Alembic](https://alembic.sqlalchemy.org/en/latest/) (already installed as a dependency) to create or update the required tables in your database.

## Launch

You are now ready to go, simply run inside the virtual env:

```bash
uvicorn main:app`
```

and your [Brevia API](https://github.com/brevia-ai/brevia) project is ready to accept calls!
