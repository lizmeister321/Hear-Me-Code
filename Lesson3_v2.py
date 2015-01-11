#
with open("states.txt", "r") as states_file:

##open() is a function to open a states_file
## takes 2 arguments:
##		argument 1: file name
## 		argument 2: how to open file---"R": read-only
##"as" keyword creates a variable out of the file ---- in this case, states_file is more or less the file itself

	states = states_file.read()

## file handler ".read()" will take in the file and save all the data
print states

with open("states.txt", "r") as states_file:
	states=states_file.read().split("\n")
print states

##.split() splitss the list from one long string into a list broken down by specified character (in this case, \n--newline (aka enter) character)

with open("states.csv", "r") as states_file:
	states=states_file.read().split("\n")

	for index, state in enumerate(states):
		states[index]=state.split(",")


##enumerate: for every item in the CSV, call the index # (count) and split it into separate lists on the ","--as specified in state.split(",")
##creates a list of lists---for every item in states.csv, create an item in a list that contains 2 pieces, state abbr. and state name

##EXERCISE: take Lesson 2, states.py and run it using file handling.

contacts = {
'Shannon': {'phone': '202-555-1234', 'twitter': '@svt827', 'github': '@ashannonturner'},
'Anupama': {'phone': '410-333-9876', 'twitter': '@iamtheanupama', 'github': '@apillalamarri'},
'Lizzie': {'phone': '917-111-1111', 'twitter': '@lizmeister321', 'github': '@lizmeister321'}
}

##NESTED DICTIONARIES!
## can now look through keys (names, in this case), values ("phone")

for contact in contacts.keys():
	print contact
## Prints names: Anupama, Shannon
## note that dictionaries don't have any fixed order, so output may be totally random
##dictionaries are fast ways to find information, but may not necessarily have info where you think it is

for contact in sorted(contacts.keys()):
	print contacts[contact]['phone']

## orders on KEY (name, in this case) and then returns phone #--Anupama comes first b/c of alpha order, has nothing to do with phone

for info in contacts.values():
	print info

##.values() shows value for each key

#EXERCISE TIME: Nested dictionary for everyone at the table

contacts = {
'Andrea': {'phone':'717-799-6492', 'email':'smashleynguyen@gmail.com',},
'Ashley':{'phone': '425-269-3308', 'email':'ajdrea.palmiter@gmail.com',},
'Lizzie':{'phone': '646-250-7186', 'email':'e.geiger.ellis@gmail.com',},
'Hana':{'phone': '576-277-1309', 'email':'elhattabh@gmail.com',},
'Lindsay':{'phone': '202-486-2671', 'email':'lindsay@lynsphotos.com',},	
}

for contact in contacts.items():
	print contact

for contact in contacts.values():
	print contact

for contact in contacts.keys():
	print contact

for contact in contacts.keys():
	print contact.upper()

for contact in sorted(contacts.keys()):
	print """{0}'s contact information is:\n\tPhone: {1}\n\tEmail: {2}
		""".format(contact,contacts[contact]['phone'],contacts[contact]['email'])
