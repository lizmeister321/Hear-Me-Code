# -*- coding: utf-8-sig -*-
Python 2.7.5 (v2.7.5:ab05e7dd2788, May 13 2013, 13:18:45) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.

>>> newlist = [alpha, beta, gamma]

Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    newlist = [alpha, beta, gamma]
NameError: name 'alpha' is not defined
>>> newlist =
SyntaxError: invalid syntax
>>> newlist = ['alpha', 'beta','gamma']
>>> view newlist
SyntaxError: invalid syntax
>>> newlist
['alpha', 'beta', 'gamma']
>>> newlist.append('moo')
>>> newlist
['alpha', 'beta', 'gamma', 'moo']
>>> newlist.insert('word', 2)

Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    newlist.insert('word', 2)
TypeError: an integer is required
>>> newlist.insert(2,'word')
>>> newlist
['alpha', 'beta', 'word', 'gamma', 'moo']
>>> newlist[1]
'beta'
>>> newlist [1]
'beta'
>>> newlist[1] = 'tree'
>>> newlist[1]
'tree'
>>> newlist
['alpha', 'tree', 'word', 'gamma', 'moo']
>>> name = 'lizzie'
>>> name[-1] = 'z'

Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    name[-1] = 'z'
TypeError: 'str' object does not support item assignment
>>> name[-1] = z

Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    name[-1] = z
NameError: name 'z' is not defined
>>> name[-1] = 'z'

Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    name[-1] = 'z'
TypeError: 'str' object does not support item assignment
>>> replace name[-1] = 'z'
SyntaxError: invalid syntax
>>> SyntaxError: invalid syntax
SyntaxError: invalid syntax
>>> week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
>>> print week
['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
>>> week
['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
>>> for day in week:
	prnt day
	
SyntaxError: invalid syntax
>>> for day in week:
	print day

monday
tuesday
wednesday
thursday
friday
saturday
sunday
>>> for house in week:
	print house

monday
tuesday
wednesday
thursday
friday
saturday
sunday
>>> 
>>> print house
sunday
>>> print house[2]
n
>>> for day in week:
	print day[-1:-3]

	







>>> for day in week:
	print day[0:-3]

	
mon
tues
wednes
thurs
fri
satur
sun
>>> for (index, day) in enumerate(week):
	print 'the {0}th day is {1}".format(index,day)
	
SyntaxError: EOL while scanning string literal
>>> for (index, day) in enumerate(week):
	print 'the {0}th day is {1}'.format(index,day)

	
the 0th day is monday
the 1th day is tuesday
the 2th day is wednesday
the 3th day is thursday
the 4th day is friday
the 5th day is saturday
the 6th day is sunday
>>> π
Unsupported characters in input
π
Unsupported characters in input
snacks = ['banana', 'apple
	  
SyntaxError: EOL while scanning string literal
>>> snacks = ['tacos', 'banana', 'steak', 'chips', 'coffee', 'potato', 'orange']
>>> snacks
['tacos', 'banana', 'steak', 'chips', 'coffee', 'potato', 'orange']
>>> for (day, snacks) in enumerate(week):
	print 'Today is {0} and I am going to eat {1}'.format,(week, snacks)

	
<built-in method format of str object at 0x102592df0> (['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'], 'monday')
<built-in method format of str object at 0x102592df0> (['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'], 'tuesday')
<built-in method format of str object at 0x102592df0> (['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'], 'wednesday')
<built-in method format of str object at 0x102592df0> (['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'], 'thursday')
<built-in method format of str object at 0x102592df0> (['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'], 'friday')
<built-in method format of str object at 0x102592df0> (['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'], 'saturday')
<built-in method format of str object at 0x102592df0> (['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'], 'sunday')
>>> for (index, day) in enumerate(week):
	print 'Today is {0} and I am going to eat {1}'.format,(week, snacks)

	
<built-in method format of str object at 0x102592e90> (['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'], 'sunday')
<built-in method format of str object at 0x102592e90> (['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'], 'sunday')
<built-in method format of str object at 0x102592e90> (['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'], 'sunday')
<built-in method format of str object at 0x102592e90> (['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'], 'sunday')
<built-in method format of str object at 0x102592e90> (['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'], 'sunday')
<built-in method format of str object at 0x102592e90> (['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'], 'sunday')
<built-in method format of str object at 0x102592e90> (['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'], 'sunday')
>>> for (day, snacks) in enumerate(week):
	print 'Today is {0} and I am going to eat {1}'.format(week, snacks)

	
Today is ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'] and I am going to eat monday
Today is ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'] and I am going to eat tuesday
Today is ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'] and I am going to eat wednesday
Today is ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'] and I am going to eat thursday
Today is ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'] and I am going to eat friday
Today is ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'] and I am going to eat saturday
Today is ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'] and I am going to eat sunday
>>> for (day, snacks) in enumerate(week):
	print 'Today is {0} and I am going to eat {1}'.format(day, snacks)

	
Today is 0 and I am going to eat monday
Today is 1 and I am going to eat tuesday
Today is 2 and I am going to eat wednesday
Today is 3 and I am going to eat thursday
Today is 4 and I am going to eat friday
Today is 5 and I am going to eat saturday
Today is 6 and I am going to eat sunday
>>> Today is 6 and I am going to eat sunday
SyntaxError: invalid syntax
>>> enumerate(snacks)
<enumerate object at 0x102434460>
>>> snacks
'sunday'
>>> snacks = ['tacos', 'banana', 'steak', 'chips', 'coffee', 'potato', 'orange']
>>> enumerate(snacks)
<enumerate object at 0x102434460>
>>> for (index, snack) in snacks:
	print (index,snack)

	

Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    for (index, snack) in snacks:
ValueError: too many values to unpack
>>> for (index, snack) in enumerate(snacks):
	print (index,snack)

	
(0, 'tacos')
(1, 'banana')
(2, 'steak')
(3, 'chips')
(4, 'coffee')
(5, 'potato')
(6, 'orange')
>>> for (index, day,snack) in enumerate(week, snacks):
	print 'today is {0} and I am going to eat {1}'.format(day, snack)

	

Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    for (index, day,snack) in enumerate(week, snacks):
TypeError: 'list' object cannot be interpreted as an index
>>> for (snack, day) in zip(snacks,week):
	print snack
	print day

	
tacos
monday
banana
tuesday
steak
wednesday
chips
thursday
coffee
friday
potato
saturday
orange
sunday
>>> for (snack, day) in zip(snacks, week):
	print snack, day

	
tacos monday
banana tuesday
steak wednesday
chips thursday
coffee friday
potato saturday
orange sunday
>>> foods.pop()

Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    foods.pop()
NameError: name 'foods' is not defined

>>> snacks.pop()
'orange'
>>> snacks.pop()
'potato'
>>> snacks.pop()
'coffee'
>>> for (snack, day) in zip(snacks, week):
	print snack, day

	
tacos monday
banana tuesday
steak wednesday
chips thursday
>>> 'august' in week
False
>>> 'saturday' in week
True
>>> range(10)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> snacks.append('coffee', 'potato', 'orange')

Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    snacks.append('coffee', 'potato', 'orange')
TypeError: append() takes exactly one argument (3 given)
>>> snacks.append(['coffee', 'potato', 'orange'])
>>> snacks
['tacos', 'banana', 'steak', 'chips', ['coffee', 'potato', 'orange']]
>>> snacks.pop()
['coffee', 'potato', 'orange']
>>> snacks.extend(['coffee', 'potato', 'orange])
	       
SyntaxError: EOL while scanning string literal
>>> snacks.extend(['coffee', 'potato', 'orange'])
>>> print snacks
['tacos', 'banana', 'steak', 'chips', 'coffee', 'potato', 'orange']
>>> snacks.extend('cheese', 'burger')

Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    snacks.extend('cheese', 'burger')
TypeError: extend() takes exactly one argument (2 given)
>>> lizzieshannonpatty

Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    lizzieshannonpatty
NameError: name 'lizzieshannonpatty' is not defined
>>> 'lizzie, patty, shannon'
'lizzie, patty, shannon'
>>> peopleinroom.split(',')

Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    peopleinroom.split(',')
NameError: name 'peopleinroom' is not defined
>>> peopleinroom = 'lizie, patty, shannon'
>>> peopleinroom.split(',')
['lizie', ' patty', ' shannon']
>>> phone = '555-1234'
>>> phone.replace('1234','5678')
'555-5678'
>>> print global
SyntaxError: invalid syntax
>>> print globals()
{'week': ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'], 'index': 6, 'snack': 'chips', 'peopleinroom': 'lizie, patty, shannon', 'name': 'lizzie', 'snacks': ['tacos', 'banana', 'steak', 'chips', 'coffee', 'potato', 'orange'], '__builtins__': <module '__builtin__' (built-in)>, 'newlist': ['alpha', 'tree', 'word', 'gamma', 'moo'], '__package__': None, 'phone': '555-1234', 'house': 'sunday', '__name__': '__main__', '__doc__': None, 'day': 'thursday'}
>>> print phone
555-1234
>>> print phone.replace('1234','5678')
555-5678
>>> print phone
555-1234
>>> print peopleinroom
lizie, patty, shannon
>>> for people in peopleinroom.split(',')
SyntaxError: invalid syntax
>>> for people in peopleinroom.split(','):
	print 'I am here with', people

	
I am here with lizie
I am here with  patty
I am here with  shannon
>>> week
['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
>>> ','.join(week)
'monday,tuesday,wednesday,thursday,friday,saturday,sunday'
>>> index = 0
>>> while index < len(week):
	print week[index]
	index +=1

	
monday
tuesday
wednesday
thursday
friday
saturday
sunday

#this is for file upload practice
with open ('months.rtf') as monthfile:
    months = monthfile.read().split('\n')
    print months

with open ('faketable.csv') as table:
    newtable = table.read().split('\r')
    for row in newtable:
        print row.split(',')

