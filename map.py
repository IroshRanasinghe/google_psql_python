# @author iroshana

import requests, json
import psycopg2

api_key = 'AIzaSyAeL5MR2XfxGi28XaBsSH_53nu-7zcjNDM'

# url variable store url
url = "https://maps.googleapis.com/maps/api/place/textsearch/json?"

# The text string on which to search
query = input('Search query: ')

# get method of requests module
# return response object

res = requests.get(url + 'query=' + query + '&key=' + api_key)

# json method of response object convert
# json format data into python format data
dict_place = res.json()

# now results contains list of nested dictionaries
results = dict_place['results']
f = open("place.json", "w")
f.write(json.dumps(dict_place))
f.close()

try:
    conn = psycopg2.connect(database='fidelis', user='postgres', password='iroshana1995', host='localhost', port='5432')

    cur = conn.cursor()
    # keep looping upto lenght of y

    id: int
    for id in range(1, 1000):
        for i in range(len(results)):
            # Print value corresponding to the
            # 'name' key at the ith index of y

            name = results[i]['name']
            description = results[i]['formatted_address']
            dtype = "category"

            sql_query = """INSERT INTO reviewable (id,dtype,name,description) VALUES(%s,%s,%s,%s)"""
            record_insert_data = (id, dtype, name, description)
            cur.execute(sql_query, record_insert_data)
            conn.commit()
            count = cur.rowcount
            print(count, "Record inserted successfully into reviewable table")

except(Exception, psycopg2.Error) as error:
    if (conn):
        print("Failed to insert record into reviewable table", error)
finally:
    if (conn):
        cur.close()
        conn.close()
        print("PostgreSQL connection is closed")
