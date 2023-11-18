import sys
import os
import unittest
from test_app_init import AppInitializationTestCase

current_directory = os.getcwd()
sys.path.insert(0, current_directory)


app_initialization_suite = unittest.TestLoader().loadTestsFromTestCase(AppInitializationTestCase)

all_tests = unittest.TestSuite([app_initialization_suite])


if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=2).run(all_tests)
