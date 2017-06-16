import unittest

import service


class TestLambdaHandler(unittest.TestCase):
    def test_lambda_handler_return_ok(self):
        '''lambda_handler should return something'''
        self.assertIsNotNone(service.lambda_handler(None, None))


if __name__ == '__main__':
    unittest.main()
