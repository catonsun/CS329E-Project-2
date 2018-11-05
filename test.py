import unittest
from app import makeList, selectDifficulty, selectNumQuestions, askQuestion, answerQuestion, calculateScores
import csv

class MyTest(unittest.TestCase):
    def test1(self):
        pass
        # self.assertEqual(, makeList("test.csv"))







if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(MyTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
    unittest.main()


# selecting button will return answer choice
# makeList returns a list
