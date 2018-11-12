import unittest
from app import makeList, selectDifficulty, selectNumQuestions, askQuestion, answerQuestion, calculateScores
import csv
from unittest.mock import patch

from contextlib import contextmanager

@contextmanager
def mockRawInput(mock):
    original_input = __builtins__.input
    __builtins__.input = lambda _: mock
    yield
    __builtins__.input = original_input

class MyTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(makeList([]), makeList([]))

    def test2(self):
        self.assertEqual(calculateScores([1,0]), "win")

    def test3(self):
        self.assertEqual(calculateScores([1,1]), "tie")

    def test4(self):
        self.assertEqual(calculateScores([0,1]), "lose")

    def test5(self):
        with mockRawInput('1'):
            self.assertEqual(selectNumQuestions(), -1)

    def test6(self):
        with mockRawInput('1'):
            self.assertEqual(selectDifficulty(), 1)

    def test7(self):
        with mockRawInput('2'):
            self.assertEqual(selectDifficulty(), 2)

    def test8(self):
        with mockRawInput('3'):
            self.assertEqual(selectDifficulty(), 3)




if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(MyTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
    unittest.main()


# selecting button will return answer choice
# makeList returns a list
