from alembic import context
from sqlalchemy import create_engine
from src.core.settings import get_settings

from src.db.models import Base

config = context.config

target_metadata = Base.metadata


def run_migrations_online() -> None:
    db_config = get_settings().db
    connectable = create_engine(db_config.dsn)

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


run_migrations_online()
