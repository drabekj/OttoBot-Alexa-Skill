import unittest

from flask import json

from app import create_app
from test.sample_requests import *


class EducationTestCase(unittest.TestCase):
    """This class represents the OttoBot routing test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client

    def test_intent_education(self):
        """Test if one of the terms (EQUITY) will be explained."""
        # Setup
        request = json.dumps(intent_education_equity())

        # Execute
        res = self.client().post('/api/', data=request,
                                 content_type='application/json')

        # Assert
        self.assertEqual(res.status_code, 200)
        self.assertIn(RESPONSE_intent_education_equity, str(res.data))

    def tearDown(self):
        """teardown all initialized variables."""
        pass


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
