#Goal: Ask user for 3 addresses, and organize in separate lists by quadrant (NW, NE, SW, SE). 
#After 3 address address entries, print the contents of each list

northwest = []
northeast = []
southwest = []
southeast = []

address1 = raw_input("Please tell me your address:")
if "NW" in address1:
    northwest.append(address1)
elif "SW" in address1:
    southwest.append(address1)
elif "SE" in address1:
    southeast.append(address1)
elif "NE" in address1:
    northeast.append(address1)

address2 = raw_input("Please tell me your address:")
if "NW" in address2:
    northwest.append(address2)
elif "SW" in address2:
    southwest.append(address2)
elif "SE" in address2:
    southeast.append(address2)
elif "NE" in address2:
    northeast.append(address2)
    
address3 = raw_input("Please tell me your address:")
if "NW" in address3:
    northwest.append(address3)
elif "SW" in address3:
    southwest.append(address3)
elif "SE" in address3:
    southeast.append(address3)
elif "NE" in address3:
    northeast.append(address3)

print len(northwest)
print northwest
print len(northeast)
print northeast
print len(southwest)
print southwest
print len(southeast)
print southeast

