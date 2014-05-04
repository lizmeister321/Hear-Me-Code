attendees=["Shannon", "Jenn", "Grace"]
people_who_didnt_do_pbj=[]

#List Slicing Examples
print attendees [0] #yields "Shannon"
print attendees [1] #prints "Jenn"
print attendees [2] #prints "Grace"
print attendees [0:2] #prints Shannon, Jenn
print attendees [3] #sends error: IndexError: list index out of range
print attendees [:3] #prints all 3 names
print attendees [2:] #prints "Grace"

number_of_attendees= len(attendees)

attendees_ages=[]
attendees_ages.append(28)
print attendees_ages
attendees_ages.append(27)
print attendees_ages #prints "[28, 27]"

attendees_ages[0]= 29 
print attendees_ages #changes 28 to 29 in list position 0

days_of_week = ["Monday", "Tuesday"]
days_of_week.append("Wednesday")
print days_of_week
days_of_week.append("Thursday")
days_of_week.append("Friday")
days_of_week.append("Saturday")
days_of_week.append("Shnursday")
print days_of_week
print len(days_of_week) #len = 7

day=days_of_week.pop()
print day #Shnursday
day=days_of_week.pop(3)
print day #Thursday
print days_of_week #Monday, Tuesday, Wednesday, Friday, Saturday

months = ["January", "February"]
months.extend(["March", "April", "May", "June", "July", "August", "September", "October"])
print months
moremonths = ["November", "December"]
months.extend(moremonths)
print months

#remove the first month, but WILL NOT be saved (no second variable)
months.pop(0)
print months
#add first month back in
months.insert(0, "January")
print months


#split method: only works with strings
address = "1133 19th St NW Washington, DC 20036"
address_as_list= address.split(" ")
print address_as_list
print address


address= raw_input("What is your address? ")
print address


for number in range(10):
    print number

days_of_week=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
for day in days_of_week:
    print day.upper()
    

for week in range(0,5):
    print "Week {0}".format(week)