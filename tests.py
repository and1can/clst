import unittest
import json
from pandas.io.json import json_normalize

class TestStringMethods(unittest.TestCase):

	def test_emailFullMatch(self):
		data = []
		test = []
		#emailFullMatch.json written by typing python query.py @gmail.com 
		#must change newTest.json in normalize function to name loading into data
		with open('emailFullMatch.json') as data_file:
			data = json.load(data_file)
		with open('emailFullMatchTest.json') as data_file:
			test = json.load(data_file)
		
		self.assertEqual(data, test)

	def test_emailPartialMatch(self):
		data = []
		test = []
		#emailPartialMatch.json written by typing python query.py @gma
		#must change newTest.json in normalize function to name loading into data
		with open('emailPartialMatch.json') as data_file:
			data = json.load(data_file)
		with open('emailFullMatchTest.json') as data_file:
			test = json.load(data_file)
		
		self.assertEqual(data, test)

	def test_phoneMatch(self):
		data = []
		test = []
		#phoneMatch.json written by typing python query.py 646 
		#must change newTest.json in normalize function to name loading into data
		with open('phoneMatch.json') as data_file:
			data = json.load(data_file)
		with open('phoneMatchTest.json') as data_file:
			test = json.load(data_file)
		
		self.assertEqual(data, test)

	def test_nameLastFullMatch(self):
		data = []
		test = []
		#phoneMatch.json written by typing python query.py Kortina
		#must change newTest.json in normalize function to name loading into data
		with open('nameLastFullMatch.json') as data_file:
			data = json.load(data_file)
		with open('nameLastFullMatchTest.json') as data_file:
			test = json.load(data_file)
		
		self.assertEqual(data, test)

	def test_nameLastPartialMatch(self):
		data = []
		test = []
		#phoneMatch.json written by typing python query.py Kort
		#must change newTest.json in normalize function to name loading into data
		with open('nameLastPartialMatch.json') as data_file:
			data = json.load(data_file)
		with open('nameLastFullMatchTest.json') as data_file:
			test = json.load(data_file)
		
		self.assertEqual(data, test)

	def test_nameFirstPartialMatch(self):
		data = []
		test = []
		#phoneMatch.json written by typing python query.py Je
		#must change newTest.json in normalize function to name loading into data
		with open('nameFirstPartialMatch.json') as data_file:
			data = json.load(data_file)
		with open('nameFirstPartialMatchTest.json') as data_file:
			test = json.load(data_file)
		
		self.assertEqual(data, test)

	def test_nameFirstFullMatch(self):
		data = []
		test = []
		#phoneMatch.json written by typing python query.py Jenny
		#must change newTest.json in normalize function to name loading into data
		with open('nameFirstFullMatch.json') as data_file:
			data = json.load(data_file)
		with open('nameFirstFullMatchTest.json') as data_file:
			test = json.load(data_file)
		
		self.assertEqual(data, test)

if __name__ == '__main__':
	unittest.main()