# importing libraries
from flask import Flask, json, request, Response, jsonify
from flask_sqlalchemy import SQLAlchemy
import csv
import requests


# creating an instance of the flask app
app = Flask(__name__)


rows = []
with open('d1.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        rows.append(row)


#csvreader = open('d1.csv')





@app.route('/')
def index():
    return Response(rows)


@app.route('/mostCheckin', methods=['POST'])
def most_check_in():
    request_data = request.get_json()
    start_time= request_data['starttime']
    end_time= request_data['endtime']
    new_rows = []
    for row in rows:
        if  row["utcTimestamp"] >= start_time and row.utcTimestamp<=end_time:
            new_rows.append(row)
    
    #countict= {}

    #for row in new_rows:
     #   countdict[row["venue_id"]]+=1
    

    #temp =0
        # for a in countdict:
        # if a.value>temp
        # ans= a.key
        # temp=a.value

    return Response({"venueID": 1})


@app.route('/address', methods=['POST'])
def address():
    request_data = request.get_json()
    venue_id= request_data["venue_id"]

    for row in rows:
        if row["venueId"]==venue_id:
            latitude= row["latitude"]
            longitude= row["longitude"]
            break
    
    Uri = "https://nominatim.openstreetmap.org/reverse?format=jsonv2"

    Uri = Uri + "&lat=" + latitude
    Uri = Uri + "&lon=" + longitude

    r =  requests.get(url = Uri )
    
    return r.json()



if __name__ == "main":
    app.run()
