import math
import unittest

from client3 import getDataPoint, getRatio


class ClientTest(unittest.TestCase):
    def test_getDataPoint(self):
        quotes = [
            {'top_ask': {'price': 120.5, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 120.5, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'},
            # Add more quotes here if needed
        ]
        for quote in quotes:
            best_bid, best_ask, timestamp, stock = getDataPoint(quote)
            self.assertEqual((best_bid, best_ask, timestamp, stock), (quote['top_bid']['price'], quote['top_ask']['price'], quote['timestamp'], quote['stock']))

    def test_getRatio(self):
        quote_a = {'top_ask': {'price': 120.5, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'}
        quote_b = {'top_ask': {'price': 120.5, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        _, _, _, price_a = getDataPoint(quote_a)
        _, _, _, price_b = getDataPoint(quote_b)
        ratio = getRatio(price_a, price_b)
        self.assertAlmostEqual(ratio, 1.0)

        # Test case: price B is zero
        quote_b_zero = {'top_ask': {'price': 0, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 0, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        _, _, _, price_b_zero = getDataPoint(quote_b_zero)
        ratio_zero = getRatio(price_a, price_b_zero)
        self.assertTrue(math.isnan(ratio_zero))

        # Additional test case: price A is zero
        quote_a_zero = {'top_ask': {'price': 0, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'}
        _, _, _, price_a_zero = getDataPoint(quote_a_zero)
        ratio_zero = getRatio(price_a_zero, price_b)
        self.assertTrue(math.isnan(ratio_zero))

        # Additional test case: price A and price B are both zero
        quote_a_zero = {'top_ask': {'price': 0, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 0, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'}
        _, _, _, price_a_zero = getDataPoint(quote_a_zero)
        quote_b_zero = {'top_ask': {'price': 0, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 0, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        _, _, _, price_b_zero = getDataPoint(quote_b_zero)
        ratio_zero = getRatio(price_a_zero, price_b_zero)
        self.assertTrue(math.isnan(ratio_zero))

if __name__ == '__main__':
    unittest.main()