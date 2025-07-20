import unittest
from dataflow_job import EnrichTransaction

class TestEnrichTransaction(unittest.TestCase):
    def test_suspicious_flag(self):
        sample = '{"amount": 15000, "location": "USA"}'
        result = list(EnrichTransaction().process(sample))
        self.assertTrue(result[0]['suspicious'])

    def test_not_suspicious(self):
        sample = '{"amount": 100, "location": "UK"}'
        result = list(EnrichTransaction().process(sample))
        self.assertFalse(result[0]['suspicious'])

if __name__ == '__main__':
    unittest.main()