from googleapiclient.discovery import build
import os, random

api_key = os.environ.get("API_KEY") # replace with your google API key

youtube = build('youtube', 'v3', developerKey=api_key)

def get_channel_videos(channel_id):
    """
    Given the channel id, return all the videos from that channel.

    Credit: https://github.com/nikhilkumarsingh/YouTubeAPI-Examples/blob/master/4.Channel-Vids.ipynb
    """
    # get Uploads playlist id
    res = youtube.channels().list(id=channel_id, 
                                  part='contentDetails').execute()
    playlist_id = res['items'][0]['contentDetails']['relatedPlaylists']['uploads']
    
    videos = []
    next_page_token = None
    
    while True:
        res = youtube.playlistItems().list(playlistId=playlist_id, 
                                           part='snippet', 
                                           maxResults=50,
                                           pageToken=next_page_token).execute()
        
        videos += res['items']
        next_page_token = res.get('nextPageToken')
        
        if not next_page_token:
            break
    
    return videos



def get_random_video():
    channel_id = 'UCtinbF-Q-fVthA0qrFQTgXQ' # Casey's channel id
    videos = get_channel_videos(channel_id)
    rand_num = random.randint(0, len(videos))
    video = videos[rand_num]

    return video

def get_url(video):
    vid_id = video['snippet']['resourceId']['videoId']
    return "https://www.youtube.com/watch?v=" + vid_id

def get_title(video):
    return video['snippet']['title']

def get_thumbnail(video):
    try:
        thumbnail = video['snippet']['thumbnails']['standard']['url']
    except KeyError: # standard size thumbnail not available
        thumbnail = video['snippet']['thumbnails']['medium']['url']

    return thumbnail

