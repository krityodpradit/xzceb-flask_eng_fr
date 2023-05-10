import unittest

from translator import frenchToEnglish, englishToFrench

class TestF2E(unittest.TestCase): 
    def test1(self):
        self.assertIsNone(frenchToEnglish(None))
    def test2(self):
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')
    def test3(self):
        self.assertNotEqual(frenchToEnglish('Bonjour'), 'Bonjour')
        

class TestE2F(unittest.TestCase): 
    def test1(self):
        self.assertIsNone(englishToFrench(None))
    def test2(self):
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')
    def test3(self):
        self.assertNotEqual(englishToFrench('Hello'), 'Hello')
        
unittest.main()