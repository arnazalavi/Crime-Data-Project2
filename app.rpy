from flask import Flask, render_template
from flask_pymongo import pymongo
import json
import os
import requests 

app = Flask(__name__)

#Use flask_pymongo to set up mongo connection
conn = "mongodb://localhost:27017/chicago_crime"
client = pymongo.MongoClient(conn)

db = client.chicago_crime
events = db.events


app.route("/")
def index():
    geojson = list(events.find_one())
    data = { 'features' : geojson}
    print (data)
    return render_template('index.html', geojson=data)
    

if __name__ == "__main__":
   # app.run(host="localhost" , debug=True)
    app.run(debug=True)