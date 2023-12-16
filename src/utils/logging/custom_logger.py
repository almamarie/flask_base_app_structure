import logging
from .db_log_handler import DatabaseHandler
from ...database.database import db


class CustomLogger():
    def __init__(self):
        # databaseHandler = DatabaseHandler(db)
        console = logging.StreamHandler()
        fileHandler = logging.FileHandler('log.log')
        logging.basicConfig(
            level=logging.DEBUG,
            format="%(asctime)s : %(levelname)s : %(name)s: %(lineno)s : %(message)s",
            handlers=[console, fileHandler]
        )
        logger = logging.getLogger('global_logger')

        self.logger = logger

    def getLogger(self):
        return self.logger
