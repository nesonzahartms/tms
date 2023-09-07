import os

"""
ORM is for Objects Relations Mapping
"""

"""
SQLAlchemy
"""

db_user = "admin"
db_pass = "cp12345"
db_host = "127.0.0.1"
db_port = 5432
db_name = "work"

DB_URL = f"postgresql+asyncpg://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}"
print(DB_URL)


PREFIX = "db_"
DB_CONFIG = {
    f"{PREFIX}url": DB_URL,
    f"{PREFIX}pool_size": int(os.getenv("DATABASE_POOL_SIZE", "1")),
    f"{PREFIX}pool_pre_ping": True,
    f"{PREFIX}pool_recycle": -1,
    f"{PREFIX}future": True,
    f"{PREFIX}echo": True,
}