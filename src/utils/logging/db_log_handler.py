import logging
from ...database.models.log_model import LoggerModel
from ..app_error import AppError

# Create a custom logging handler that logs to a database table


class DatabaseHandler(logging.StreamHandler):
    def __init__(self, db):
        super().__init__()
        self.db = db

    def emit(self, record):
        # Format the log message
        print("Logging error")
        # Create a SQL query to insert the log message into the database table
        try:
            new_log = LoggerModel(message=record.getMessage(),
                                  level_name=record.levelname,
                                  timestamp=record.created,
                                  source=record.name,
                                  context=record.exc_info)
            new_log.insert()
        except Exception as exe:
            print(exe)
            raise AppError("Error sending log to database", 500)
