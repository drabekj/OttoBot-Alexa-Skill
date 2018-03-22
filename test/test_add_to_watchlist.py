import unittest

from flask import json

from app import create_app, db, logger
from app.models import Stock, User, Watchlist
from test.sample_requests import *


class AddToWatchlistTestCase(unittest.TestCase):
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
            User(test_user_id, test_user_name).save()

    def test_intent_add_to_watchlist_dialog(self):
        """Test if the add to watchlist dialog works correctly including confirmation/cancelation."""

        # 1st Step: start dialog "add to watchlist"
        logger.info("1st step: start dialog add to watchlist")
        self.add_to_watchlist_dialog_invoke()

        logger.info("2st step: deny adding stock to watchlist")
        self.add_to_watchlist_dialog_deny()

        logger.info("3st step: confirm adding stock to watchlist")
        self.add_to_watchlist_dialog_invoke()
        self.add_to_watchlist_dialog_confirm()

    def add_to_watchlist_dialog_invoke(self):
        # Setup
        request = json.dumps(intent_add_to_watchlist())

        # Execute
        res = self.client().post('/api/', data=request,
                                 content_type='application/json')

        # Assert
        self.assertEqual(res.status_code, 200)
        self.assertIn(RESPONSE_intent_add_to_watchlist_ask_confirmation,
                      str(res.data))
        # check if stock not in watchlist just yet
        with self.app.app_context():
            watchlist = Watchlist.get_users_tickers(test_user_id)
        for item in watchlist:
            self.assertNotEqual(item, test_add_stock)

    def add_to_watchlist_dialog_deny(self):
        # Setup
        request = json.dumps(intent_add_to_watchlist_deny())

        # Execute
        res = self.client().post('/api/', data=request,
                                 content_type='application/json')

        # Assert 1st step
        self.assertEqual(res.status_code, 200)
        self.assertIn(RESPONSE_intent_add_to_watchlist_denied, str(res.data))
        # check if stock not in watchlist just yet
        with self.app.app_context():
            watchlist = Watchlist.get_users_tickers(test_user_id)
        for item in watchlist:
            self.assertNotEqual(item, test_add_stock)

    def add_to_watchlist_dialog_confirm(self):
        # Setup
        request = json.dumps(intent_add_to_watchlist_confirm())

        # Execute
        res = self.client().post('/api/', data=request,
                                 content_type='application/json')

        # Assert 1st step
        self.assertEqual(res.status_code, 200)
        self.assertIn(
            RESPONSE_intent_add_to_watchlist_confirmed.format(test_add_stock),
            str(res.data))
        # check if stock was added to watchlist
        with self.app.app_context():
            watchlist = Watchlist.get_users_tickers(test_user_id)
        for item in watchlist:
            self.assertEqual(item, test_add_stock)

    def tearDown(self):
        """teardown all initialized variables."""
        with self.app.app_context():
            # drop all tables
            db.session.remove()
            db.drop_all()


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
