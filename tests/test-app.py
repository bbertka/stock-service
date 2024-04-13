import pytest
from flask_testing import TestCase
from src.app import app

class TestStockService(TestCase):
    def create_app(self):
        # Configure Flask application for testing
        app.config['TESTING'] = True
        return app

    def test_home(self):
        # Test the home endpoint
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Hello GitLab!", response.data)

    def test_stock_price_success(self):
        # Test the stock price endpoint with a known symbol
        response = self.client.get('/stock-price?symbol=AAPL')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"AAPL", response.data)

    def test_stock_price_no_symbol(self):
        # Test the stock price endpoint with no symbol
        response = self.client.get('/stock-price')
        self.assertEqual(response.status_code, 404)
        self.assertIn(b"Failed to retrieve the price.", response.data)

# Allows running the tests via the command line
if __name__ == '__main__':
    pytest.main()
