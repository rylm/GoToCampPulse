import requests
import pymongo
import time
import datetime

from users import users

url = "https://api.vk.com/method/users.get?fields=online&user_ids="

online_counter = 0
i = 0

client = pymongo.MongoClient()
db = client.main

while True:
    for second in range(1, 61):
        print(second)
    print("================================================\n")
    datetime_now = datetime.datetime.fromtimestamp(time.time()).strftime('%c')
    print(datetime_now)
    print("\n================================================\n")

    print(str(len(users)) + " people:\n")

    for user_id in users:
        url += user_id + ","

    profiles = requests.get(url).json()['response']

    for user in profiles:
        first_name = user['first_name']
        last_name = user['last_name']
        is_online = user['online']
        uid = user['uid']

        if is_online:
            online_counter += 1

        online_message = "is not online" if is_online == 0 else "is online"

        if 'online_mobile' in user.keys():
            print(first_name + " " + last_name + " " + online_message, end="")
            print(" from mobile site or app")
        else:
            print(first_name + " " + last_name + " " + online_message)

    with open("last_number.txt", "w") as last_record:
        last_record.write(str(online_counter))

    db.user_stats.insert_one(
        {
            str(int(time.time())): profiles
        }
    )
