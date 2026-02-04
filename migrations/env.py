from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context



#import sys
#from os.path import dirname, abspath
# ===== ДОБАВЛЯЕМ ЭТОТ БЛОК ДЛЯ ПРАВИЛЬНЫХ ИМПОРТОВ =====
# Определяем пути
#current_dir = os.path.dirname(os.path.abspath(__file__))  # .../migrations
#project_root = os.path.dirname(current_dir)               # .../myproject
#src_path = os.path.join(project_root, 'src')              # .../myproject/src

# Добавляем пути в sys.path для импортов
#sys.path.insert(0, src_path)    # сначала src/
#sys.path.insert(0, project_root) # затем корень проекта
#sys.path.insert(0, dirname(dirname(dirname(abspath(__file__)))))    # сначала src/
# Получаем путь к папке migrations
#current_dir = os.path.dirname(os.path.abspath(__file__))  # .../migrations
#project_root = os.path.dirname(current_dir)               # .../base_app

# Добавляем корень проекта в sys.path
#sys.path.insert(0, project_root)





from database import Base
from users.models import User
from configs import DATABASE_URL

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config


config.set_main_option("sqlalchemy.url", f"{DATABASE_URL}?async_fallback=True")

# Interpret the CONFIG file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
target_metadata = Base.metadata

# other values from the CONFIG, defined by the needs of env.py,
# can be acquired:
# my_important_option = CONFIG.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
