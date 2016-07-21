import requests
# import itertools
# import pymongo
# import time

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
print(len(users))

for user_id in users:
    profile = requests.get(url + str(user_id)).json()['response'][0]
    first_name = profile['first_name']
    last_name = profile['last_name']
    is_online = profile['online']
    if is_online:
        online_counter += 1
    online_message = "не онлайн" if is_online == 0 else "онлайн"
    if 'online_mobile' in profile.keys():
        print(first_name + " " + last_name + " " + online_message, end="")
        print(" через мобильную версию сайта или приложение")
    else:
        print(first_name + " " + last_name + " " + online_message)

# db.onliness.insert_one(
#     {
#         "online_counter": online_counter,
#         "time": int(time.time())
#     }
# )