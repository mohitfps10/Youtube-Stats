
from flask import Flask, render_template, request
import pprint 
from googleapiclient.discovery import build 
app = Flask(__name__)



@app.route('/')
def index():
   return render_template("index.html")


DEVELOPER_KEY = "AIzaSyDYhH8IMPzMZF5GmHkxIO19LQzzs7asj3k" #My API Key
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey = DEVELOPER_KEY) 


def channel_details(channel_id): 

   
    channel_details_dict = youtube.channels().list(id = channel_id, part="id,snippet,statistics,status,brandingSettings").execute() 
    print(channel_details_dict)
    subscriber_count=channel_details_dict ["items"][0]["statistics"]["subscriberCount"]
    channel_name=channel_details_dict ["items"][0]["snippet"]["title"]
    channel_created_date=channel_details_dict ["items"][0]["snippet"]["publishedAt"]
    channel_created_date=channel_created_date[0:10]
    video_count=channel_details_dict ["items"][0]["statistics"]["videoCount"]
    view_count=channel_details_dict ["items"][0]["statistics"]["viewCount"]
    comment_count=channel_details_dict ["items"][0]["statistics"]["commentCount"]
    profile_photo_url=channel_details_dict ["items"][0]["snippet"]["thumbnails"]["default"]["url"]
    details=[]

    details.extend((subscriber_count,channel_name,channel_created_date,video_count,view_count,comment_count,profile_photo_url))
    return(details)





@app.route('/result',methods = ['GET','POST'])
def result():
  
    if request.method == 'POST':
      channel_id = request.form["Channel Id"]
      details=[]
      details=channel_details(channel_id)
      
         
      return render_template("pass.html",subscriber_count = details[0],channel_name=details[1], channel_created_date=details[2],video_count=details[3],view_count=details[4],
      comment_count=details[5],profile_photo_url=details[6])
    
if __name__ == "__main__": 

 app.run(debug = True)
  
  
