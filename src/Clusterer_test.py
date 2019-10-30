import unittest
from Clusterer import Clusterer


class TestClusterer(unittest.TestCase):
    def test(self):
        clusterer = Clusterer(k1=1, k2=1, max_dist=0.5, variables=[])
        clusters = clusterer.find([
            'hello 1 y 3',
            'hello 1 x 3',
            'abc m n q',
        ])
        self.assertEqual(
            clusters,
            [
                [['hello', '1', 'y', '3'], 2],
                [['abc', 'm', 'n', 'q'], 1]
            ]
        )

    def test_small_max_dist(self):
        clusterer = Clusterer(k1=1, k2=1, max_dist=0.01, variables=[])
        clusters = clusterer.find([
            'hello 1 y 3 ',
            'hello 1 x 3 ',
            'abc m n q ',
        ])
        self.assertEqual(
            clusters,
            [
                [['hello', '1', 'y', '3'], 1],
                [['hello', '1', 'x', '3'], 1],
                [['abc', 'm', 'n', 'q'], 1]
            ]
        )


if __name__ == '__main__':
    unittest.main()
