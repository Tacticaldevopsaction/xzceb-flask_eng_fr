import unittest

from translator import english_to_french
from translator import french_to_english

class Test_english_to_french(unittest, Testcase):
	def test1(self):
		self.assertEqual('', '') 
		self.assertEqual('Hello', 'Bonjour')
        self.assertNotEqual('Hello', 'Hallo')

class Test_french_to_english(unittest, Testcase):
	def test1(self):
		self.assertEqual('', '') 
		self.assertEqual('Bonjour', 'Hello')
		self.assertNotEqual('Bonjour', 'Hallo')

unittest.main()