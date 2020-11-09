# Createdb
> CREATE DATABASE ping_service CHARACTER SET utf8 COLLATE utf8_general_ci;

# Migration
> namekox alembic revision --autogenerate -m "init"

> namekox alembic upgrade head

# Running
> namekox run facade
