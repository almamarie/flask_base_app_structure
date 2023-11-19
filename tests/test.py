import sys
import os
import unittest
from test_app_init import AppInitializationTestCase

# current_directory = os.getcwd()
# sys.path.insert(0, current_directory)

# Adjust the path to include the directory containing the flaskr package
current_directory = os.getcwd()
sys.path.insert(0, os.path.join(current_directory, 'flaskr'))


app_initialization_suite = unittest.TestLoader(
).loadTestsFromTestCase(AppInitializationTestCase)

all_tests = unittest.TestSuite([app_initialization_suite])

# remove the path from the package

if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=2).run(all_tests)
