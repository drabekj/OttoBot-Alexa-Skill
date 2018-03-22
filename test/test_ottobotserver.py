import unittest

from flask import json

from app import create_app, db
from app.models import Stock, User, Watchlist
from static import strings
from test.sample_requests import *


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

            # Insert testing data
            Stock(test_stock_1_ticker, test_stock_1_date, Close=test_stock_1_close).save()
            Stock(test_stock_2_ticker, test_stock_2_date, Close=test_stock_2_close).save()
            User(test_user_id, test_user_name).save()
            Watchlist(test_stock_1_ticker, test_user_id).save()
            Watchlist(test_stock_2_ticker, test_user_id).save()

    def test_test_page(self):
        """Test API answers test GET request.
            Usually used to check if server is running.
        """
        # Execute
        res = self.client().get('/')

        # Assert
        self.assertEqual(res.status_code, 200)
        self.assertIn('RUNNING', str(res.data))

    def test_launch_request(self):
        """Test API answers launch request with welcome response."""
        # Setup
        request = json.dumps(launch_request())

        # Execute
        res = self.client().post('/api/', data=request,
                                 content_type='application/json')

        # Assert
        self.assertEqual(res.status_code, 200)
        escaped_msg = strings.REQUEST_LAUNCH_MSG.translate(
            str.maketrans({"'": r"\'"}))
        self.assertIn(escaped_msg, str(res.data))

    def test_intent_request_stock_price(self):
        """Test API answers intent request get stock price."""
        # Setup
        request = json.dumps(intent_request_get_stock_price())

        # Execute
        res = self.client().post('/api/', data=request,
                                 content_type='application/json')

        # Assert
        self.assertEqual(res.status_code, 200)
        self.assertIn(RESPONSE_intent_request_get_stock_price, str(res.data))

    def test_intent_report_watchlist_not_authenticated(self):
        """Test API handles case where user is not authenticated."""
        # Setup
        request = json.dumps(intent_report_watchlist_not_authenticated())

        # Execute
        res = self.client().post('/api/', data=request,
                                 content_type='application/json')

        # Assert
        self.assertEqual(res.status_code, 200)
        self.assertIn(ERROR_NOT_AUTHENTICATED, str(res.data))

    def test_intent_report_watchlist(self):
        """Test API answers intent request report watchlist."""
        # Setup
        request = json.dumps(intent_report_watchlist())

        # Execute
        res = self.client().post('/api/', data=request,
                                 content_type='application/json')

        # Assert
        self.assertEqual(res.status_code, 200)
        self.assertIn(RESPONSE_intent_report_watchlist, str(res.data))

    def test_intent_report__empty_watchlist(self):
        """Test API answers intent request report watchlist."""
        # Setup
        with self.app.app_context():
            Watchlist.delete_all()
        request = json.dumps(intent_report_watchlist())

        # Execute
        res = self.client().post('/api/', data=request,
                                 content_type='application/json')

        # Assert
        self.assertEqual(res.status_code, 200)
        self.assertIn(RESPONSE_intent_report_empty_watchlist, str(res.data))

    def test_intent_add_to_watchlist(self):
        """Test API answers intent request report watchlist."""
        # Setup
        request = json.dumps(intent_add_to_watchlist())

        # Execute
        res = self.client().post('/api/', data=request,
                                 content_type='application/json')

        # Assert
        self.assertEqual(res.status_code, 200)
        self.assertIn(RESPONSE_intent_add_to_watchlist_ask_confirmation, str(res.data))

    def tearDown(self):
        """teardown all initialized variables."""
        with self.app.app_context():
            # drop all tables
            db.session.remove()
            db.drop_all()


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
