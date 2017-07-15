# Difficulty level: Beginner

# Goal #1: Write a new version of the PB&J program that uses a while loop.  Print "Making sandwich #" and the number of the sandwich until you are out of bread, peanut butter, or jelly.
def pbj_while(bread, pb, jelly):
	sandwich = 0
	while bread/2 > and pb > 1 and jelly > 1:
		sandwich = sandwich + 1	
		print "I am making a sandwich..."
		bread = bread - 2
		print "I have enough bread left for {0} more sandwiches".format(int(bread/2))
	print "Ran out of bread, but I made {0} sandwiches".format(sandwich)

pbj_while(20)


# Output:
# Making sandwich #1
# Making sandwich #2
# All done; only had enough bread for 2 sandwiches.

# Goal #2: Modify that program to say how many sandwiches-worth of each ingredient remains.

# bread = 10
# pb = 10
# jelly = 4
# sandwich = 0
# ran_out = [""]

# while bread >= 2 and pb >= 1 and jelly >= 1:
#     sandwich = sandwich + 1
#     print "I am making sandwich number {0}".format(sandwich)
#     bread = bread - 2
#     pb = pb - 1
#     jelly = jelly - 1
#     print "I have enough bread for {0} sandwiches, enough pb for {0} sandwiches, and enough jelly for {0} sandwiches".format(bread/2,pb,jelly)
# if bread == 0:
#     ran_out.append("bread")
# if pb == 0:
#     ran_out.append("pb")
# if jelly == 0:
#     ran_out.append("jelly")
# print "All done! I made {0} sandwich(es) and ran out of {1}".format(sandwich, ran_out[1:])

# Output:
# Making sandwich #1
# I have enough bread for 4 more sandwiches, enough peanut butter for 9 more, and enough jelly for 3 more.
# Making sandwich #2
# I have enough bread for 3 more sandwiches, enough peanut butter for 8 more, and enough jelly for 2 more.
# Making sandwich #3
# I have enough bread for 2 more sandwiches, enough peanut butter for 7 more, and enough jelly for 1 more.
# Making sandwich #4
# All done; I ran out of jelly.