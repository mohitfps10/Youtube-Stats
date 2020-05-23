# import libraries 
from googleapiclient.discovery import build 
import pprint 

# arguments to be passed to build function 
DEVELOPER_KEY = "AIzaSyDGaWqqiwM6YXAd_ETbsvh_d0OoLHaVvMU"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

# creating youtube resource object 
# for interacting with API 
youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey = DEVELOPER_KEY) 


def video_details(video_id): 

   
    list_videos_byid = youtube.channelSections().list(id = video_id, 
        part = "id, snippet, contentDetails",).execute() 

        
    results = list_videos_byid.get("items", [])
    print(type(results))
    for result in results:
      for data in result:
        print(result[data])
        print()
    print()
      #videos.append("(% s) (% s) (% s) " % (result["snippet"],result['contentDetails'],result["statistics"]))  
      #print("Videos:\n", "\n".join(videos), "\n")
    
if __name__ == "__main__": 

    video_id = "UCIvaYmXn910QMdemBG3v1pQ"
    video_details(video_id) 
