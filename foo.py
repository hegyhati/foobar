def smaller (a, b):
    if isinstance(a,str):
        return a  if float(a) < float(b) else b
    else:
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