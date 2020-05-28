# import libraries 
from googleapiclient.discovery import build 
import pprint 
# arguments to be passed to build function 
DEVELOPER_KEY = "AIzaSyDGaWqqiwM6YXAd_ETbsvh_d0OoLHaVvMU" #My API Key
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey = DEVELOPER_KEY) 


def channel_details(channel_id): 

   
    channel_details_dict = youtube.channels().list(id = channel_id, part="id,snippet,statistics,status").execute() 
    print(channel_details_dict)
    channel_name=channel_details_dict ["items"][0]["statistics"]["subscriberCount"]
    subscriber_count=channel_details_dict ["items"][0]["snippet"]["title"]
    channel_created_date=channel_details_dict ["items"][0]["snippet"]["publishedAt"]
    video_count=channel_details_dict ["items"][0]["statistics"]["videoCount"]
    view_count=channel_details_dict ["items"][0]["statistics"]["viewCount"]



    print(channel_name, subscriber_count,channel_created_date)
    
    
if __name__ == "__main__": 

    channel_id = "youtube_analytics.reports().query(
        dimensions="video",
        ids="channel==MINE",
        maxResults=10,
        metrics="estimatedMinutesWatched,views,likes,subscribersGained",
        sort="-estimatedMinutesWatched"
    )"
    channel_details(channel_id) 
