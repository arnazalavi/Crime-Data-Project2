from flask import Flask, render_template, redirect ,jsonify
from flask_pymongo import PyMongo
import json
import os
import requests 

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/chicago_crime"
mongo = PyMongo(app)

# Or set inline

# default route
# add route
# main page
app.route("/")
def readGeoJson3():
    cursor= mongo.db.events.find()
    # #print(cursor)
    features=[]
    for geojson_feature  in cursor:
       features.append({
           "type": geojson_feature['type'],
          "geometry":  geojson_feature['geometry'],
           "properties" :  geojson_feature['properties']
           }
        )
    # print(features)
    data = { 'features' : features}
    # print(data)
    # data = json.dumps(data)
    #data = 'Hello'
    return render_template('index.html', geojson=data)

@app.route("/read")
def read():
    cursor= mongo.db.events.find()
    #print(cursor)
    result=[]
    for record in cursor:
        property = record["properties"]
        #property = record["Feature"]
        result +=  property
        #print(result)
    return jsonify(result)

   # return render_template("index.html", geoData=geoData)
    #json1 = geoData.to_json(orient='records')
    #jsonfiles = json.loads(geoData)
  
@app.route("/readFeature")
def readGeoJson5():
    cursor= mongo.db.events.find()
    #print(cursor)
    features=[]
    for geojson_feature  in cursor:
        features.append({
            "type": geojson_feature['type'],
            "geometry":  geojson_feature['geometry'],
            "properties" :  geojson_feature['properties']
            }

        )
    return jsonify(features)

#render to index html
@app.route("/getGeojasonData")
def readGeoJson():
    cursor= mongo.db.events.find()
    # #print(cursor)
    features=[]
    for geojson_feature  in cursor:
       features.append({
           "type": geojson_feature['type'],
          "geometry":  geojson_feature['geometry'],
           "properties" :  geojson_feature['properties']
           }
        )
    # print(features)
    data = { 'features' : features}
    # print(data)
    # data = json.dumps(data)
    #data = 'Hello'
    #return render_template('index.html', geojson=data)
    return jsonify(data)

@app.route("/getGeojasonData22")
def readGeoJsonData():
    #Comment 52 -- 63
        cursor= mongo.db.events.find()
    #print(cursor)
   #     features =[]
    #  features_values=[]
    # for geojson_feature  in cursor:
        #    features_values.append({
      #      "type": geojson_feature['type'],
            #"geometry":  geojson_feature['geometry'],
       #     "properties" :  geojson_feature['properties']
        #    }

       # )
        url ="https://data.cityofchicago.org/resource/ijzp-q8t2.geojson?$limit=50000&$offset=0&$order=id&$where=year > 2020"
        crime_response = requests.get(url).json()
        #features["features"] = features_values
        #{features["features"] : ['features_values']}
        #return jsonify(features_values)
        return  jsonify(crime_response)

##crime = collection.find()
if __name__ == "__main__":
   # app.run(host="localhost" , debug=True)
    app.run(debug=True)
