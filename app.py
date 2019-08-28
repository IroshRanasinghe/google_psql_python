import requests
import psycopg2
import json

conn = psycopg2.connect(database='fidelis', user='postgres', password='iroshana1995', host='localhost', port='5432')

url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"

querystring = {
    "location": "6.9148472,79.875588",
    "radius": "1500",
    "type": "restaurant",
    "keyword": "cruise",
    "key": "AIzaSyBzeqyVAgdXLUSB8YGVI2dzYcMgnsgOC2I"}

payload = ""

response = requests.request("GET", url, data=payload, params=querystring)

print(response.json())

# data here is a list of dicts
data = response.json()['results']

print(data)


cur = conn.cursor()
# create a table with one column of type JSON
cur.execute("CREATE TABLE location (data json);")

create_table_query = '''CREATE TABLE map_category
          (id INT PRIMARY KEY     NOT NULL,
          name           TEXT     NOT NULL,
          description    TEXT     NOT NULL); '''

fields = [
    'geometry',
    'icon',
    'id',
    'name',
    'opening_hours',
    'photos',
    'place_id',
    'plus_code',
    'rating',
    'reference',
    'scope',
    'types',
    'user_ratings_total',
    'vicinity'
]

for item in data:
    my_data = {field: item[field] for field in fields}
    cur.execute("INSERT INTO t_skaters VALUES (%s)", (json.dumps(my_data),))
#
#
# # commit changes
# conn.commit()
# # Close the connection
# conn.close()
