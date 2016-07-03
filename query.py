import json
from pandas.io.json import json_normalize
import sys

class norm(object):
	def __init__(self, name, arg):
		self.lst = []				#list with entries of each element of the json file
		self.first = []				#group 1) of the respective sorting type
		self.combined = []			#final list with sorted order and will be fed to normalize function to create json file
		self.other = []				#has same form as query, but does not match
		self.na = []				#does not have query type
		self.me = []				#entry that has nickname me
		with open(name) as data_file:
			data = json.load(data_file)
		self.data = data
		self.norm = json_normalize(data)
		self.arg = arg
		for r in data:
			curr = {}
			me = False
			if 'email' in r:
				curr.update({'email': r['email']})
			if 'phone' in r:
				curr.update({'phone': r['phone']})
			if 'nickname' in r:
				curr.update({'nickname': r['nickname']})
			if 'name' in r:
				curr.update({'name': r['name']})
			if 'nickname' in r:
				if r['nickname'] == "Me":
					me = True
			if (me):
				self.me.append(curr)
			else:
				self.lst.append(curr)

	#email() split the values and only look at what is after @ symbol in argument
	#will put entries that have 'email' values that match entire argument or a substring of value matches argument 
	#into self.first list. 

	def email(self):
		for l in self.lst:
			if 'email' in l:
				curr = l['email'].lower().split("@")
				if (len(curr) == 2):
					if ((curr[1] == self.arg[1:]) or (self.arg[1:] in curr[1])):
						self.first.append(l)
					else:
						self.other.append(l)
				else:
					self.other.append(l)
			else:
				self.combined.append(l)

		self.first = sorted(self.first, key = lambda x: x['email'].split("@")[0])
		self.other = sorted(self.other, key = lambda x : x['email'].split("@")[0])
		self.combined = self.me + self.first + self.other + self.combined
		
	def name(self):
		print "search by name"
		for l in self.lst:
			if 'name' in l:
				curr = l['name'].lower()
				curr = curr.split(" ")
				if (len(curr) > 2):						#to handle cases like "  sam smith" (one where there are spaces before value)
					count = 0
					c = curr[0]
					if (c == ""):
						while (c == ""):
							c = curr[count]
							count += 1
						counter = count - 1
						parsed = curr[counter]
						counter += 1
						while (counter < len(curr)):
							parsed += " " + curr[counter]
							counter += 1
						l['name'] = parsed
						curr = parsed
				blank = False
				if (curr[0] == ""):						#case that we have a blank for a value
					self.na.append(l)
					blank = True
				match = False
				for c in curr:
					if ((c.lower() == self.arg.lower()) or (self.arg.lower() in c.lower())):
						match = True	
				if (not blank):
					if (match):
						self.first.append(l)			#case argument matches value full match or partial match
					else:
						self.other.append(l)			#case argument does not have partial or full match on value, but has correct form 
														#that user is querying
			else:										#case that there is no key for entry that user is querying
				self.na.append(l)

		self.first = sorted(self.first, key = lambda x: x['name'].lower())
		self.other = sorted(self.other, key = lambda x: x['name'].lower())
		self.combined = self.me + self.first + self.other + self.na

	def phone(self):
		for l in self.lst:
			if 'phone' in l:
				num = ""
				for i in l['phone']:
					if (i.isdigit()):
						num += i
				if (len(num) == 11):  # to remove 1 in 1-800-123-4567
					num = num[1:]
				if (num[0:3] == self.arg):
					self.first.append(l)
				else:
					self.other.append(l)
			else:
				self.na.append(l)
		self.combined = self.me + self.first + self.other + self.na

	#sort figures out what column the user will query by

	def sort(self):
		option = self.arg
		print "sort type is", option
		if (option[0] == "@"):			#search by email
			print "search by email"
			return self.email()
		try: 							#search by phone
			val = int(option)
			print "search by phone"
			self.phone()
		except ValueError:  			#search by name
			self.name()

		
	#called after sort and will create the json file with the sorted list 
	#and print out the normalized json file
	def normalize(self):
		with open("newTest.json", "w") as outfile:
			json.dump(self.combined, outfile, indent=4)
		with open("newTest.json") as data_file:
			data = json.load(data_file)
			print json_normalize(data)



n = norm('contacts.json', sys.argv[1])
n.sort()
n.normalize()