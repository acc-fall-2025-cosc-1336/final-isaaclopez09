#write function tests here, don't add input('') statements here!
import unittest

#follow this example to add questions b, c, and d for testing including their functions
from src.question_c.question_c import get_most_likely_ancestor_consensus

class Test_get_most_likely_ancestor_consensus(unittest.TestCase):

    def test_get_most_likely_ancestor_consensus(self):
        pos1, pos2, pos3 = get_most_likely_ancestor_consensus("GATATATGCATATACTT", "ATAT")
        self.assertEqual(pos1, 2)
        self.assertEqual(pos2, 4)
        self.assertEqual(pos3, 10)


