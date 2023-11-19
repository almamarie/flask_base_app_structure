import sys
import os
import unittest
from test_app_init import AppInitializationTestCase




app_initialization_suite = unittest.TestLoader(
).loadTestsFromTestCase(AppInitializationTestCase)

all_tests = unittest.TestSuite([app_initialization_suite])

# remove the path from the package
# sys.path.pop(0)
# sys.path.pop(0)


if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=2).run(all_tests)
