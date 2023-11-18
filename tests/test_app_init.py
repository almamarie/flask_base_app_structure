import os
import sys
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

# Adjust the path to include the directory containing the flaskr package
current_directory = os.getcwd()
sys.path.insert(0, os.path.join(current_directory, 'flaskr'))

from flaskr import create_app
from src.database.database import init_app, db
from src.utils.config import Config

config = Config()


class AppInitializationTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = config.DATABASE_CONFIG.database_name

        # database_name = 'trivia'
        # database_password = 'postgres'
        # database_user = 'postgres'
        # database_host = 'localhost:5432'
        self.database_path = config.SQLALCHEMY_DATABASE_URI

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """

    # ====================================================================================
    # Tests for /categories
    # ====================================================================================
    # successful operation
    def test_get_root_route(self):
        res = self.client().get("/")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["categories"])

    def test_error_get_all_categories(self):
        res = self.client().get("/categorie")
        data = json.loads(res.data)
        # print("\n Categories error: ", data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "resource not found")


if __name__ == "__main__":
    unittest.main()
