# import requests
import psycopg2
import json

#
# conn = psycopg2.connect(database='fidelis', user='postgres', password='iroshana1995', host='localhost', port='5432')
#
# url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
#
# querystring = {
#     "location": "6.9148472,79.875588",
#     "radius": "1500",
#     "type": "restaurant",
#     "keyword": "cruise",
#     "key": "AIzaSyBzeqyVAgdXLUSB8YGVI2dzYcMgnsgOC2I"}
#
# payload = ""
#
# response = requests.request("GET", url, data=payload, params=querystring)

#
dict = {
           'formatted_phone_number': '0000000',
           'name': 'ABC',
           'description': 'https://www.thekingsburyhotel.com/'
       }, {
           'formatted_phone_number': '0000000',
           'name': 'CDE',
           'description': 'https://www.thekingsburyhotel.com/'
       }

json_obj = json.dumps(dict)

# # f = open("data.json", "w")
# f.write(json_obj + "\n")
# f.close()

dict = {
           'formatted_phone_number': '0000000',
           'name': 'ABC',
           'description': 'https://www.thekingsburyhotel.com/'
       }, {
           'formatted_phone_number': '0000000',
           'name': 'CDE',
           'description': 'https://www.thekingsburyhotel.com/'
       }

with open('data.json') as data_file:
    data = json.load(data_file)

    for details in data["results"]:
        name=details["name"]
        description=details["description"]

        print(name)
        print(description)

# try:
#     conn = psycopg2.connect(database='fidelis', user='postgres', password='iroshana1995', host='localhost', port='5432')
#
#     cur = conn.cursor()
#     # for result in details:
#
#     id = 1
#     dtype = "category"
#     name = "Test Hotel"
#     description = "test Description"
#     sql_query = """INSERT INTO reviewable (id,dtype,name,description) VALUES(%s,%s,%s,%s)"""
#     record_insert_data = (id, dtype, name, description)
#     cur.execute(sql_query, record_insert_data)
#     conn.commit()
#     count = cur.rowcount
#     print(count, "Record inserted successfully into reviewable  table")
#
# except(Exception, psycopg2.Error) as error:
#     if (conn):
#         print("Failed to insert record into reviewable table", error)
# finally:
#     if (conn):
#         cur.close()
#         conn.close()
#         print("PostgreSQL connection is closed")
