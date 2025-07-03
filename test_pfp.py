import unittest
from pfp_algorithm import pfp_search
from map_loader import dummy_neighbors
from predictor import predict_cost

class TestPFP(unittest.TestCase):

    def test_reaches_goal(self):
        result = pfp_search("A", "B", dummy_neighbors, predict_cost)
        self.assertTrue(result)

    def test_handles_congestion(self):
        result = pfp_search("A", "D", dummy_neighbors, predict_cost)
        self.assertTrue(result)

    def test_no_path(self):
        result = pfp_search("E", "A", dummy_neighbors, predict_cost)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
