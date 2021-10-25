from flask import Flask, render_template, redirect ,jsonify
from flask_pymongo import PyMongo
import json

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/chicago_crime"
mongo = PyMongo(app)

# Or set inline



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
def readGeoJson():
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


##crime = collection.find()
if __name__ == "__main__":
    app.run(debug=True)
