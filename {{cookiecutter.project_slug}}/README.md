# {{cookiecutter.project_name}}

{{cookiecutter.project_description}}

This is a [Brevia API](https://github.com/brevia-ai/brevia) project.

## Quickstart

[Poetry](https://python-poetry.org/docs/#installation) is required to setup this API. It is also recommended to use virtualenv inside the project folder (you can simply do that with `poetry config virtualenvs.in-project true`) we assume this configuration from now on, but you are free to use your usual virtualenv configuration.

## Setup

* install the dependencies by running `poetry install`, a virtualenv will automatically be created in the `.venv` folder
* activate the virtualenv by running the `poetry shell` command.
* check the `.env` file where environment variables are stored, especially `OPENAI_API_KEY` with the secret key of OpenAI and `PGVECTOR_*` see the [Database](#database) section

## Database

You can run `docker compose --profile admin up` to run postgres+pgvector and pgadmin docker images. With your browser, open `pgadmin` at http://localhost:4000

The `4000` port is configurable with the `PGADMIN_PORT` environment var in the `.env` file.

Launch migrations to create the initial schema with [Alembic](https://alembic.sqlalchemy.org) by using this brevia command

```bash
db_upgrade
```

## Launch

You are now ready to go, simply run

```bash
uvicorn --env-file .env main:app`
```

and your [Brevia API](https://github.com/brevia-ai/brevia) project is ready to accept calls!
