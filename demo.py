import googlemaps
import json
import pprint
import time
import psycopg2
from random import randint
from time import sleep
import os

API_KEY = 'AIzaSyAeL5MR2XfxGi28XaBsSH_53nu-7zcjNDM'
# API_KEY = 'AIzaSyBzeqyVAgdXLUSB8YGVI2dzYcMgnsgOC2I'

# Define the Client
gmaps = googlemaps.Client(key=API_KEY)

# Do a simple nearby search where we specify the location
# in lat/lon format, along with a radius measured in meters
places_result = gmaps.places_nearby(location='6.9220039,79.7861639', radius=40000, open_now=False, type='restaurant')

time.sleep(60)

place_result = gmaps.places_nearby(page_token=places_result['next_page_token'])

stored_results = []

# loop through each of the places in the results, and get the place details.
for place in places_result['results']:
    # define the place id, needed to get place details. Formatted as a string.
    my_place_id = place['place_id']

    # define the fields you would liked return. Formatted as a list.
    my_fields = ['name', 'website']

    # make a request for the details.
    places_details = gmaps.place(place_id=my_place_id, fields=my_fields)

    # print the results of the details, returned as a dictionary.
    dict_details = places_details['result']

    # create connection psql
try:
    conn = psycopg2.connect(database='fidelis', user='postgres', password='iroshana1995', host='localhost', port='5432')
    cur = conn.cursor()
    id = 1
    dtype = "category"
    name = "Test Hotel"
    description = "test Description"
    sql_query = """INSERT INTO reviewable (id,dtype,name,description) VALUES(%s,%s,%s,%s)"""
    record_insert_data = (name, description)
    cur.execute(sql_query, record_insert_data)
    conn.commit()
    count = cur.rowcount
    print(count, "Record inserted successfully into test table")
except(Exception, psycopg2.Error) as error:
    if (conn):
        print("Failed to insert record into mobile table", error)
finally:
    if (conn):
        cur.close()
        conn.close()
        print("PostgreSQL connection is closed")
