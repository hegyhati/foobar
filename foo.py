def smaller (a, b):
    return a  if a < b else b



import unittest

class SmallerTest(unittest.TestCase):

    def testSmaller(self):
        self.assertEqual(3, smaller(3,5))
        self.assertEqual(3, smaller(3,15))
    
    def testSmallerString(self):
        self.assertEqual("3", smaller("3","5"))
        self.assertEqual("3", smaller("3","15"))

if __name__ == "__main__":
    unittest.main()