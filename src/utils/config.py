import os


class Config:
    DATABASE_CONFIG = {
        'database_type': 'mysql',
        'username': os.getenv('SQL_USERNAME'),
        'password': os.getenv('SQL_PASSWORD'),
        'host': os.getenv('SQL_HOST', 'localhost'),
        # MySQL port, or 'None' for SQLite
        'port': os.getenv('SQL_PORT', '3306'),
        'database_name': os.getenv('SQL_DATABASE')
    }

    if DATABASE_CONFIG['database_type'] == 'mysql':
        SQLALCHEMY_DATABASE_URI = (
            f"mysql://{DATABASE_CONFIG['username']}:{DATABASE_CONFIG['password']}"
            f"@{DATABASE_CONFIG['host']}:{DATABASE_CONFIG['port']}/{DATABASE_CONFIG['database_name']}"
        )
    else:
        raise ValueError("Unsupported database type")

    SQLALCHEMY_TRACK_MODIFICATIONS = False
