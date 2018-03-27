import unittest

from flask import json

from app import create_app
from test.sample_requests import *


class NewsTestCase(unittest.TestCase):
    """This class represents the OttoBot routing test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client

    def test_intent_news_about_company(self):
        """Test that user will be presented with company headlines."""
        # Setup
        request = json.dumps(intent_news_about_company())

        # Execute
        res = self.client().post('/api/', data=request,
                                 content_type='application/json')

        # Assert
        self.assertEqual(res.status_code, 200)
        self.assertIn(RESPONSE_intent_news_about_company, str(res.data))

    def test_intent_news_send_link(self):
        """Test that user will be presented with company headlines."""
        # Setup
        request = json.dumps(intent_news_send_link())

        # Execute
        res = self.client().post('/api/', data=request,
                                 content_type='application/json')

        # Assert
        self.assertEqual(res.status_code, 200)
        self.assertIn(RESPONSE_intent_news_send_link, str(res.data))

    def tearDown(self):
        """teardown all initialized variables."""
        pass


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
