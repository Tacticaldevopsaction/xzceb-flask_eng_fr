import unittest

from translator import english_to_french
from translator import french_to_english

class TestEnglishToFrench(unittest, Testcase):
	def test1(self):
		self.assertEqual(english_to_french(''), '') # test for the null when null is given as input the output is null 
		self.assertEqual(english_to_french('Hello'), 'Bonjour') # test when hello is given as input the output is bonjour
		self.assertNotEqual(english_to_french('Hello'), 'Bonjour') # test when hello is given as input the output is NOT bonjour

class TestFrenchToEnglish(unittest, Testcase):
	def test1(self):
		self.assertEqual(french_to_english(''), '') # test for the null when null is given as input the output is null 
		self.assertEqual(french_to_english('Bonjour'), 'Hello') # test when bonjour is given as input the output is hello
		self.assertNotEqual(french_to_english('Bonjour'), 'Hello') # test when bonjour is given as input the output is NOT hello

unittest.main()