import unittest

from datetime import date
from flask import json

from app import create_app, db
from app.models import Stock
from static import strings
from test.sample_requests import launch_request, intent_request_get_stock_price


class OttoBotServerTestCase(unittest.TestCase):
    """This class represents the OttoBot routing test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client

        # binds the app to the current context
        with self.app.app_context():
            # create all tables
            db.create_all()
            # prepare data
            Stock("TSLA", date(2018, 1, 1), Close=333.33).save()

    def test_test_page(self):
        """Test API answers test GET request.
            Usually used to check if server is running.
        """
        res = self.client().get('/')
        self.assertEqual(res.status_code, 200)
        self.assertIn('RUNNING', str(res.data))

    def test_launch_request(self):
        """Test API answers launch request with welcome response."""
        request = json.dumps(launch_request())
        res = self.client().post('/api/',
                                 data=request,
                                 content_type='application/json')

        self.assertEqual(res.status_code, 200)
        escaped_msg = strings.REQUEST_LAUNCH_MSG.translate(
            str.maketrans({"'": r"\'"}))
        self.assertIn(escaped_msg, str(res.data))

    def test_intent_request_stock_price(self):
        """Test API answers intent request get stock price."""
        request = json.dumps(intent_request_get_stock_price())
        res = self.client().post('/api/',
                                 data=request,
                                 content_type='application/json')

        self.assertEqual(res.status_code, 200)
        self.assertIn("The price of", str(res.data))

    def tearDown(self):
        """teardown all initialized variables."""
        with self.app.app_context():
            # drop all tables
            db.session.remove()
            db.drop_all()


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
