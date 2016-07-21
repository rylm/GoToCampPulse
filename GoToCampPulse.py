import requests
import pymongo
import time

from users import users

url = "https://api.vk.com/method/users.get?fields=online&user_ids="

online_counter = 0
i = 0

# client = pymongo.MongoClient()
# db = client.test

print(str(len(users)) + " человек:")

for user_id in users:
    url += user_id + ","

profiles = requests.get(url).json()['response']
print(profiles)

for user in profiles:
    first_name = user['first_name']
    last_name = user['last_name']
    is_online = user['online']
    uid = user['uid']

    if is_online:
        online_counter += 1

    online_message = "не онлайн" if is_online == 0 else "онлайн"

    if 'online_mobile' in user.keys():
        print(first_name + " " + last_name + " " + online_message, end="")
        print(" через мобильную версию сайта или приложение")
    else:
        print(first_name + " " + last_name + " " + online_message)

with open("last_number.txt", "w") as last_record:
    last_record.write(str(online_counter))

# db.user_stats.insert_one(
#     {
#         int(time.time()): profiles
#     }
# )