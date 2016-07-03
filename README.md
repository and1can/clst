# Command line search tool that ranks contacts.

Reads in ‘contacts.json’ as its data source and takes one argument,
a search query, then prints out an ordered list of ‘JSON’ normalized
results, ranked with the most relevant contacts first. 

Program Version:
	python==2.7.10
	pandas==0.18.0
	  ^^ I installed by typing: pip install pandas
	

To test:
    python tests.py

    (Note: I did have to manually make the test files, but I wrote in the next steps what I can do to make this better)

Three ways to sort: 
	Invariant for all sort methods:
		-The entry in list of contacts.json with nickname of Me will always be first
		- ^^ The reason why I chose this feature is that one does not call oneself, so it is more likely to forget one's own number.    (smartphones are slowly making this reasoning less and less valid because generally speaking, no one really knows anyone's number ...)
    a) sort by e-mail:
    	invoked by typing: python query.py @gmail.com (<--- can replace gmail.com with any mailing service. substring of mailing services can also work!)
        1) The entries with substring or matches that are the same as input argument for value of 'email' will go first. Entries within this group will be sorted alphabetically. The reason why this group is first is that they are the most relevant because they have a value in 'email' that has substring or matching string with the user's query (argument). 
        2) Next are the entries that have 'email' value that does not match with user's query (argument) and value is not a blank, Nan, or fireball. These are less relevant than entries with matches because they do not match. They are more relevant than blank, Nan, and fireball because we can at least contact these individuals via email. Entries within this gorup are sorted alphabetically. 
        3) Fireball is after 1) and 2) because we cannot contact a fireball via email. Fireball is better than blank and Nan because at least the user wrote an email and one that is readable, unlike Nan. 
        4) Blank is better than Nan because it is valid in python. Similar reasoning as 3) why this is after 1) and 2). 
        5) Nan is last because it is not a number in python. Similar reasoning as 3) why this is after 1) and 2). 

    b) sort by name:
       invoked by typing: python query.py Andrew (<-- can replace Andrew with any string. substring of first name or last name can work as well as complete matches of first and last name)
       1) The entries with substring or matches that are the same as input argument for value of 'name' will go first. Entries within this group will be sorted alphabetically. The reason why this group is first is that they are the most relevant because they have a value for 'name' that has substring or matching string with the user's query (argument). 
       2) Next are the entries that have 'name' that does not match with user's query (argument) and value is not a blank or Nan. These are less relevant than entries with matches because they do not match. They are more relevant than blank, Nan, and fireball because we can at least we know the individual's name. Entries within this group are sorted alphabetically. 
       3) Blank is better than Nan because it is valid in python. Blanks are after 1) and 2) because we cannot contact blanks.
       4) Nan is last because it is not a number in python. Similar reasoning for 3) why 4) is after 1) and 2). 
    	
    c) sort by phone:
    	invoked by typing: python query.py 415 (<--- can replace 415 with any 3 digit area code that one is querying about)
        1) The entries with 3 digit area code that matches with argument for value of 'phone' will go first. Entries within this group will be sorted alphabetically. The reason why this group is first is that they are the most relevant because they have a value for 'phone' that has area code that matches to the user's query (argument). 
        2) Next are the entries that have 'phone' that does not match with user's query (argument) and value is not a blank or Nan. These are less relevant than entries with matches because they do not match. They are more relevant than blank and Nan because we can at least contact these individuals via phone. Entries in this group maintain the same relative order as the original 'contacts.json' file. 
        3) Blank is better than Nan because it is valid in python. Blanks are after 1) and 2) because we cannot contact blanks.
        4) Nan is last because it is not a number in python. Similar reasoning for 3) why 4) is after 1) and 2). 

Next steps:
    1) Sort phone numbers by area code that is closest to me first for the group that does not match with the area code that user is querying. Web scraping can help determine the area code metric between me and the others in the json file. 

    2) An additional improvement for the phone numbers, is to sort the entries alphabetically for each cluster (a cluster being a group that has the same area code). 

    3) Sam Smith bug: can be shown when type python query.py smith. Output will not put sam smith in priority because sam smith is checked by character. This bug can be fixed by carefully constructing sam smith in line 67-81. Carefully constructing meaning I need to think of a new way to parse sam smith so that it will be checked with sam as one element and smith as another rather than 9 elements (the individual characters)

    4) I need to allow tests.py to run query.py, so that I do not need to manually hardcode the file that will show what my program does. Serializing can solve this problem because if I serialize the norm object in query.py, I can have a counter that counts how many times I ran query.py and use that counter to create files. I can then manually make a file with expected output to compare with that file(s) created when running python tests.py. Currently, I need to manually make a file with expected output and hard code in query.py script and then run query.py. The purpose of this improvement is so that I will no longer need to hardcode the file to create in query.py that shows what my program does. 

    5) For partial matches when querying for a name, I need to make sure entries only go to first as priority when argument matches the first few letters in first name or last name or both. Currently, the argument only needs to be within the first name or last name for an entry to be put in priority self.first list. 

  
    	