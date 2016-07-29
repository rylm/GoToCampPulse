import pymongo
import csv
import datetime

client = pymongo.MongoClient()
db = client.main
collection = db.user_stats

records = collection.find()

online_records = []

for record in records:
    time = sorted(list(record.keys()))[0]
    online_counter = 0
    for user in record[time]:
        if user['online'] == 1:
            online_counter += 1
    online_records.append([time, online_counter, datetime.datetime.fromtimestamp(int(time))])

with open('data.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, quotechar='|', quoting=csv.QUOTE_MINIMAL)
    csvwriter.writerow(['time', 'people_online', 'datetime'])
    for online_record in online_records:
        csvwriter.writerow(online_record)
