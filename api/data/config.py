from os import getenv

from .singleton import Database


def bind(**kwargs):
    Database().bind(**kwargs)


def exec():
    provider = getenv("DATABASE_PROVIDER")
    if not provider:
        raise AttributeError("DATABASE_PROVIDER not set")

    match provider:
        case "sqlite":
            filename = getenv("DATABASE_FILENAME")
            if not filename:
                filename = ":sharedmemory:"
            bind(provider=provider, filename=filename, create_db=True)
        case "postgres":
            user = getenv("DATABASE_USER")
            password = getenv("DATABASE_PASSWORD")
            host = getenv("DATABASE_HOST")
            database = getenv("DATABASE_NAME")

            if not user:
                raise AttributeError("DATABASE_USER not set")
            if not password:
                raise AttributeError("DATABASE_PASSWORD not set")
            if not host:
                raise AttributeError("DATABASE_HOST not set")
            if not database:
                raise AttributeError("DATABASE_NAME not set")

            bind(
                provider=provider,
                user=user,
                password=password,
                host=host,
                database=database,
            )
        case "mysql":
            host = getenv("DATABASE_HOST")
            user = getenv("DATABASE_USER")
            passwd = getenv("DATABASE_PASSWORD")
            db = getenv("DATABASE_NAME")

            if not host:
                raise AttributeError("DATABASE_HOST not set")
            if not user:
                raise AttributeError("DATABASE_USER not set")
            if not passwd:
                raise AttributeError("DATABASE_PASSWORD not set")
            if not db:
                raise AttributeError("DATABASE_NAME not set")

            bind(provider=provider, host=host, user=user, passwd=passwd, db=db)
        case "oracle":
            user = getenv("DATABASE_USER")
            password = getenv("DATABASE_PASSWORD")
            dsn = getenv("DATABASE_DSN")

            if not user:
                raise AttributeError("DATABASE_USER not set")
            if not password:
                raise AttributeError("DATABASE_PASSWORD not set")
            if not dsn:
                raise AttributeError("DATABASE_DSN not set")

            bind(provider=provider, user=user, password=password, dsn=dsn)
        case "cockroach":
            user = getenv("DATABASE_USER")
            password = getenv("DATABASE_PASSWORD")
            host = getenv("DATABASE_HOST")
            database = getenv("DATABASE_NAME")

            if not user:
                raise AttributeError("DATABASE_USER not set")
            if not password:
                raise AttributeError("DATABASE_PASSWORD not set")
            if not host:
                raise AttributeError("DATABASE_HOST not set")
            if not database:
                raise AttributeError("DATABASE_NAME not set")

            bind(
                provider=provider,
                user=user,
                password=password,
                host=host,
                database=database,
            )
        case _:
            raise AttributeError(f"Unknown database provider: {provider}")

    Database().generate_mapping(create_tables=True)
