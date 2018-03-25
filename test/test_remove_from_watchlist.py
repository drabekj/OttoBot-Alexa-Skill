import unittest

from flask import json

from app import create_app, db
from app.models import Stock, User, Watchlist
from test.sample_requests import *


class RemoveFromWatchlistTestCase(unittest.TestCase):
    """This class represents removing stock from watchlist test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client

        # binds the app to the current context
        with self.app.app_context():
            # create all tables
            db.create_all()

            # Insert testing data
            Stock(test_stock_1_ticker, test_stock_1_date, close=test_stock_1_close).save()
            User(test_user_id, test_user_name).save()
            Watchlist(test_add_stock, test_user_id).save()

    def test_denied(self):
        """Test if the remove from watchlist dialog without confirmation works.
        Flow, there is a stock in users watchlist, user asks to remove it but
        denies it afterwards."""

        # Setup: check if there is stock in users watchlist
        with self.app.app_context():
            watchlist = Watchlist.get_users_tickers(test_user_id)
        self.assertIn(test_add_stock, watchlist)

        # Step 1 ask to remove stock (stock present)
        res = self._remove_from_watchlist(test_add_stock)
        # Assert
        self.assertEqual(res.status_code, 200)
        self.assertIn(RESPONSE_intent_remove_from_watchlist_ask_confirmation,
                      str(res.data))

        # Step 2 deny removing the stock
        # Prepare request
        request = json.dumps(intent_remove_from_watchlist_deny())

        # Execute
        res = self.client().post('/api/', data=request,
                                 content_type='application/json')

        # Assert
        self.assertEqual(res.status_code, 200)
        self.assertIn(RESPONSE_intent_remove_from_watchlist_denied,
                      str(res.data))
        # Check if stock is still in watchlist
        with self.app.app_context():
            watchlist = Watchlist.get_users_tickers(test_user_id)
        self.assertIn(test_add_stock, watchlist)

    def test_confirmed(self):
        """Test if the remove from watchlist dialog confirmed works.
        Flow, there is a stock in users watchlist, user asks to remove it but
        denies it afterwards."""
        # Setup: check if there is stock in users watchlist
        with self.app.app_context():
            watchlist = Watchlist.get_users_tickers(test_user_id)
        self.assertIn(test_add_stock, watchlist)

        # Step 1 ask to remove stock (stock present)
        res = self._remove_from_watchlist(test_add_stock)
        # Assert
        self.assertEqual(res.status_code, 200)
        self.assertIn(RESPONSE_intent_remove_from_watchlist_ask_confirmation,
                      str(res.data))

        # Step 2 Confirm removing the stock
        # Prepare request
        request = json.dumps(intent_remove_from_watchlist_confirm())

        # Execute
        res = self.client().post('/api/', data=request,
                                 content_type='application/json')

        # Assert
        self.assertEqual(res.status_code, 200)
        self.assertIn(RESPONSE_intent_remove_from_watchlist_confirmed
                      .format(test_add_stock),
                      str(res.data))
        # Check if stock was removed from watchlist
        with self.app.app_context():
            watchlist = Watchlist.get_users_tickers(test_user_id)
        self.assertNotIn(test_add_stock, watchlist)

    def test_watchlist_empty(self):
        """Test removing stock from watchlist when watchlist is empty."""

        # Setup: check the target stock is not in users watchlist
        with self.app.app_context():
            watchlist = Watchlist.get_users_tickers(test_user_id)
        self.assertNotIn(test_stock_1_ticker, watchlist)

        # Step 1 ask to remove stock (stock not present)
        res = self._remove_from_watchlist(test_stock_1_ticker)
        # Assert
        self.assertEqual(res.status_code, 200)
        self.assertIn(RESPONSE_intent_remove_from_watchlist_not_there,
                      str(res.data))
        pass

    def _remove_from_watchlist(self, ticker):
        """Test removing stock from watchlist, no assertion.
        :return: response to the request"""
        # Prepare request
        request = json.dumps(intent_remove_from_watchlist(ticker))

        # Execute
        res = self.client().post('/api/', data=request,
                                 content_type='application/json')
        return res

    def tearDown(self):
        """teardown all initialized variables."""
        with self.app.app_context():
            # drop all tables
            db.session.remove()
            db.drop_all()


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
