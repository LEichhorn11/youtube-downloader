import subprocess
import youtube_dl
import urllib.request
import re
import pandas as pd
import time
import design
import os

def select_playlist():
    playlist = input("Please enter the name of the playlist in the folder: (csv format only) ")
    try:
        playlist_pd = pd.read_csv(playlist+'.csv')
        list = playlist_pd['Track Name'] + ' ' + playlist_pd['Artist Name(s)']
        return list
    except :
        print('File does not exist')

def find_url(search_keyword):
    textToSearch = urllib.parse.quote(search_keyword)
    html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + textToSearch)
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    link = "https://www.youtube.com/watch?v=" + video_ids[0]
    print(link)
    return link


def run(video_url = 'empty'):
    # Ask the user for the video they want to download
    if video_url == 'empty':
        video_url = input("Please enter the YouTube Video URL: ")
    # Download and convert to mp3 and store in downloads folder
    video_info = youtube_dl.YoutubeDL().extract_info(
        url=video_url, download=False
    )
    num = video_url.find('=') + 1
    filename1 = f"{video_info['title']+'-'+ video_url[num:]}.mp3"
    filename = f"{video_info['title']}.mp3"
    options ={
    'format': 'bestaudio/best',
    'postprocessors':[{
    'key': 'FFmpegExtractAudio',
    'preferredcodec': 'mp3',
    'preferredquality': '192',
        }],
    }
    ydl = youtube_dl.YoutubeDL(options)
    ydl.download([video_info['webpage_url']])
    time.sleep(10)
    # Open the file once it has been downloaded
    cwd = os.getcwd()

    if not os.path.exists('Music'):
        os.makedirs('Music')
    print(filename1)
    os.rename(cwd+'/'+filename1, cwd+'/Music/'+filename)

def main():
    design.showWelcome()
    choose_option = int(input("Choose one of the following options: \n Enter 1 for Download playlist \n Enter 2 for Download song by youtube search \n Enter 3 for Download song by youtube url \n "))
    try:
        if choose_option == 1:
            playlist = select_playlist()
            for i in playlist:
                try:
                    test = find_url(i)
                    run(test)
                except:
                    print('Could not find this song or it already existed')
        elif choose_option == 2:
            search_keyword = input("Input your search: ")
            test2 = find_url(search_keyword)
            run(test2)
        else:
            run()
    except:
        print('Sorry something went wrong')


if __name__ == '__main__':
    main()
