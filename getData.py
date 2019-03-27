import pyrebase
import json
import pandas as pd

config = { 
    "apiKey": "AIzaSyAAERSrXStyHsU889OZGfrCFe1E2Bit_xs",
    "authDomain": "demos-5e3db.firebaseapp.com",
    "databaseURL": "https://demos-5e3db.firebaseio.com",
    "projectId": "demos-5e3db",
    "storageBucket": "demos-5e3db.appspot.com",
    "messagingSenderId": "329457089013"
}

def toJSON(path, fileName, data):
    extension = path + "/" + fileName + ".json"
    with open(extension, "w") as fp:
        json.dump(data, fp)

firebase = pyrebase.initialize_app(config)
db = firebase.database()

videos = db.child("videos").get()
users = db.child("Users").get()

toJSON("data/json/","videos", videos.val())
toJSON("data/json/","users", users.val())


with open('data/json/users.json') as users:
    usersDict = json.load(users)

users = pd.DataFrame.from_dict(usersDict, orient='index')
users.reset_index(inplace=True)
users.to_csv('data/csv/users.csv')

with open('data/json/videos.json') as videos:
    videosDict = json.load(videos)

videos = pd.DataFrame.from_dict(videosDict, orient='index')
videos.reset_index(inplace=True)
videos.to_csv('data/csv/videos.csv')



