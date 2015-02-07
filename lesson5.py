import requests

movie = raw_input("What movie do you want to know about? ")

response = requests.get("http://bechdeltest.com/api/v1/getMoviesByTitle?title=" + movie.lower().strip())

bechdel_results = response.json()

#print bechdel_results

if len(bechdel_results)>1:
	print "More than one movie matched your search. Which did you mean?"
	for result in bechdel_results:
		if result["title"].lower().endswith(", the"):
			print "The " + result["title"].lower().replace(" the","")
		else:
			print result ["title"]
	new_film = raw_input(">").lower()
		if new_film.startswith("the"):
			new_film = new_film.replace("the ","")
			new_response = requests.get("http://bechdeltest.com/api/v1/getMoviesByTitle?title=" + new_film.lower().strip().replace(" ","+"))
			new_result = new_response.json()
			if new_result[0]["title"].endswith():
				new_result[0]["title"].replace(", The","")
		print "The Bechdel Rating for {0} is {1}".format("The " + new_result[0]["title"], new_result[0]["rating"])
		else: 
			print "The Bechdel Rating for {0} is {1}".format(new_result[0]["title"], new_result[0]["rating"])
elif len(bechdel_results)==0:
	print "Sorry, no movies matched your search. Try again?"
else:
	for result in bechdel_results:
		if result["title"].lower().endswith(", the"):
			print "The Bechdel Rating for The {0} is {1}".format(bechdel_results[0]["title"].replace(", The",""), bechdel_results[0]["rating"])
		else:
			print "The Bechdel Rating for {0} is {1}".format(bechdel_results[0]["title"], bechdel_results[0]["rating"])

# import requests
# response=requests.get("http://bechdeltest.com/api/v1/getMoviesByTitle?title=clueless")
# print response.json()
