import unittest
from app import makeList, selectDifficulty, selectNumQuestions, askQuestion, answerQuestion, calculateScores
import csv

class MyTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(makeList([]), makeList([]))

    def test2(self):
        self.assertEqual(calculateScores([1,0]), "win")

    def test3(self):
        self.assertEqual(calculateScores([1,1]), "tie")

    def test4(self):
        self.assertEqual(calculateScores([0,1]), "lose")







if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(MyTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
    unittest.main()


# selecting button will return answer choice
# makeList returns a list
