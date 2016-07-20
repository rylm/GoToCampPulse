import requests
import itertools

url = "https://api.vk.com/method/users.get?fields=online&user_ids="

user_ids = ["1", "2", "3"]
online_counter = 0
i = 0

for user_id in itertools.count(1):
    i += 1
    profile = requests.get(url + str(user_id)).json()
    first_name = profile['response'][0]['first_name']
    last_name = profile['response'][0]['last_name']
    is_online = profile['response'][0]['online']
    if is_online:
        online_counter += 1
    print(first_name + " " + last_name + " " + str(is_online))
    if i > 5:
        break

with open("all_numbers.txt", "a") as all_numbers:
    all_numbers.write(str(online_counter))
    all_numbers.write("\n")
with open("last_number.txt", "w") as last_number:
    last_number.write(str(online_counter))
