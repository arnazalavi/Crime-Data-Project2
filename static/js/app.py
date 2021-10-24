from flask import Flask, render_template, redirect ,jsonify
from flask_pymongo import PyMongo
import json

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/chicago_crime"
mongo = PyMongo(app)

# Or set inline



@app.route("/")
def index():
    geoData= mongo.db.events.find()
    print(geoData)
   # return render_template("index.html", geoData=geoData)
    #json1 = geoData.to_json(orient='records')
    #jsonfiles = json.loads(geoData)
    return jsonify(geoData.id)



##crime = collection.find()
if __name__ == "__main__":
    app.run(debug=True)
