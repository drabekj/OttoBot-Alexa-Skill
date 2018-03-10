import unittest

from flask import json

from app import create_app, db
from test.sample_requests import launch_request, test_request


class OttoBotServerTestCase(unittest.TestCase):
    """This class represents the bucketlist test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client
        self.bucketlist = {'name': 'Go to Borabora for vacation'}

        # binds the app to the current context
        with self.app.app_context():
            # create all tables
            db.create_all()

    def test_test_page(self):
        """Test API answers test GET request.
            Usually used to check if server is running.
        """
        res = self.client().get('/')
        self.assertEqual(res.status_code, 200)
        self.assertIn('RUNNING', str(res.data))

    def test_launch_request(self):
        """Test API answers launch request with welcome response."""
        request = json.dumps(test_request())
        res = self.client().post('/api/', data=request, content_type='application/json')
        self.assertEqual(res.status_code, 200)
        self.assertIn('response', str(res.data))

    def tearDown(self):
        """teardown all initialized variables."""
        with self.app.app_context():
            # drop all tables
            db.session.remove()
            db.drop_all()


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
