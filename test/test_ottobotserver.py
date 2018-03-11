import unittest

from datetime import date
from flask import json

from app import create_app, db
from app.models import Stock, User, Watchlist
from static import strings
from test.sample_requests import launch_request,\
    intent_request_get_stock_price, intent_report_watchlist


class OttoBotServerTestCase(unittest.TestCase):
    """This class represents the OttoBot routing test case"""

    test_user_id = "amzn1.ask.account.AE7YEGFRUCUT2J24CYPQUWILRXKBRID4L7ZDK2GRZD6DOHYLKE4X6TFZMNYHYSVOU546M7OS6PQWYX6APXGBKIF4WMRB4YACKZZMB63XNAKOQ35VS7SUPME33JJ7V3EJDZLDARVNRUTVOGMSIDWJHKRYSXT2XDUYVPRD6URE3OOGSFM4MWSFMOPTELRTGBB6E6PKWRCBI3PGDGY"
    StockTest = Stock("TSLA", date(2018, 1, 1), Close=333.33)
    UserTest = User(test_user_id, "Jan Drabek")
    WatchlistTest = Watchlist("TSLA", test_user_id)

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client

        # binds the app to the current context
        with self.app.app_context():
            # create all tables
            db.create_all()

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
        res = self.client().post('/api/',
                                 data=request,
                                 content_type='application/json')

        # Assert
        self.assertEqual(res.status_code, 200)
        escaped_msg = strings.REQUEST_LAUNCH_MSG.translate(
            str.maketrans({"'": r"\'"}))
        self.assertIn(escaped_msg, str(res.data))

    def test_intent_request_stock_price(self):
        """Test API answers intent request get stock price."""
        # Setup
        with self.app.app_context():  # prepare DB entry
            self.StockTest.save()
        request = json.dumps(intent_request_get_stock_price())

        # Execute
        res = self.client().post('/api/',
                                 data=request,
                                 content_type='application/json')

        # Assert
        self.assertEqual(res.status_code, 200)
        self.assertIn("The price of", str(res.data))

    def test_intent_report_watchlist(self):
        """Test API answers intent request report watchlist."""
        # Setup
        with self.app.app_context():  # prepare DB entry
            self.UserTest.save()
            self.WatchlistTest.save()
        request = json.dumps(intent_report_watchlist())

        # Execute
        res = self.client().post('/api/',
                                 data=request,
                                 content_type='application/json')

        # Assert
        self.assertEqual(res.status_code, 200)
        self.assertIn(strings.INTENT_WATCHLIST_REPORT_MSG, str(res.data))

    def tearDown(self):
        """teardown all initialized variables."""
        with self.app.app_context():
            # drop all tables
            db.session.remove()
            db.drop_all()


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
