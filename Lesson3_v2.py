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

for state in states:
	print{state}.format()