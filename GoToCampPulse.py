import requests
import itertools

url = "https://api.vk.com/method/users.get?fields=online&user_ids="

user_ids = ["1", "2", "3"]
i = 0

for user_id in itertools.count(1):
	profile = requests.get(url+str(user_id)).json()
	first_name = profile['response'][0]['first_name']
	last_name = profile['response'][0]['last_name']
	is_online = profile['response'][0]['online']
	print(first_name+ " " + last_name + " " + str(is_online))
	if user_id > 38:
		break
