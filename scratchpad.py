
# contacts = {
# 'Andrea': {'phone':'717-799-6492', 'email':'smashleynguyen@gmail.com',},
# 'Ashley':{'phone': '425-269-3308', 'email':'ajdrea.palmiter@gmail.com',},
# 'Lizzie':{'phone': '646-250-7186', 'email':'e.geiger.ellis@gmail.com',},
# 'Hana':{'phone': '576-277-1309', 'email':'elhattabh@gmail.com',},
# 'Lindsay':{'phone': '202-486-2671', 'email':'lindsay@lynsphotos.com',},	
# }


# for contact in contacts.keys():
# 	for keys in contact.keys():
# 		print keys

import requests

movies = requests.get("http://bechdeltest.com/api/v1/getMoviesByTitle?title=matrix").json()

for movie in movies:
	for key, value in movie.items():
		print key, value
	print "\n\n"