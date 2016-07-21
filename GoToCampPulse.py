import requests
import pymongo
import time

url = "https://api.vk.com/method/users.get?fields=online&user_ids="

users = [
    "artemyi_03",
    "idengrachev",
    "id63362507",
    "stnastya0801",
    "id106157229",
    "id365401818",
    "gicha1",
    "id151481010",
    "dimafet001",
    "danichl",
    "lemems",
    "ilykuleshov",
    "id97665374",
    "ematreni",
    "serebrova_elena",
    "idiot_shrimp",
    "sonikoronova",
    "egor354",
    "pawka1207",
    "charon",
    "id264820293",
    "step300699",
    "masikintel",
    "galecore",
    "id275581737",
    "flyted",
    "w_h_i_m_s_y",
    "id305146266",
    "nikmeh",
    "glinkz410",
    "leha0401",
    "geonerus",""
    "the_duckbill",
    "maxfer908",
    "id81788584",
    "id181816944",
    "id181816944",
    "alexajax",
    "id2885857",
    "id207802996",
    "ub3aor",
    "relatur",
    "gilevkirill",
    "pavel.gorbunov2000",
    "m.a.bykovsky",
    "barbado",
    "smiru_mir"
]

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