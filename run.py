import subprocess
import youtube_dl
import os
import urllib.request
import re
import pandas as pd
import time
import platform

def clear_screen():
    command = "cls" if platform.system().lower()=="windows" else "clear"
    os.system(command)

def showWelcome():
    clear_screen()
    print("\033[96m {}\033[00m" .format("""
 WWWWWWWW                           WWWWWWWW                    lllllll
W::::::W                           W::::::W                    l:::::l
W::::::W                           W::::::W                    l:::::l
W::::::W                           W::::::W                    l:::::l
 W:::::W           WWWWW           W:::::W     eeeeeeeeeeee     l::::l     cccccccccccccccc   ooooooooooo      mmmmmmm    mmmmmmm       eeeeeeeeeeee
  W:::::W         W:::::W         W:::::W    ee::::::::::::ee   l::::l   cc:::::::::::::::c oo:::::::::::oo  mm:::::::m  m:::::::mm   ee::::::::::::ee
   W:::::W       W:::::::W       W:::::W    e::::::eeeee:::::ee l::::l  c:::::::::::::::::co:::::::::::::::om::::::::::mm::::::::::m e::::::eeeee:::::ee
    W:::::W     W:::::::::W     W:::::W    e::::::e     e:::::e l::::l c:::::::cccccc:::::co:::::ooooo:::::om::::::::::::::::::::::me::::::e     e:::::e
     W:::::W   W:::::W:::::W   W:::::W     e:::::::eeeee::::::e l::::l c::::::c     ccccccco::::o     o::::om:::::mmm::::::mmm:::::me:::::::eeeee::::::e
      W:::::W W:::::W W:::::W W:::::W      e:::::::::::::::::e  l::::l c:::::c             o::::o     o::::om::::m   m::::m   m::::me:::::::::::::::::e
       W:::::W:::::W   W:::::W:::::W       e::::::eeeeeeeeeee   l::::l c:::::c             o::::o     o::::om::::m   m::::m   m::::me::::::eeeeeeeeeee
        W:::::::::W     W:::::::::W        e:::::::e            l::::l c::::::c     ccccccco::::o     o::::om::::m   m::::m   m::::me:::::::e
         W:::::::W       W:::::::W         e::::::::e          l::::::lc:::::::cccccc:::::co:::::ooooo:::::om::::m   m::::m   m::::me::::::::e
          W:::::W         W:::::W           e::::::::eeeeeeee  l::::::l c:::::::::::::::::co:::::::::::::::om::::m   m::::m   m::::m e::::::::eeeeeeee
           W:::W           W:::W             ee:::::::::::::e  l::::::l  cc:::::::::::::::c oo:::::::::::oo m::::m   m::::m   m::::m  ee:::::::::::::e
            WWW             WWW                eeeeeeeeeeeeee  llllllll    cccccccccccccccc   ooooooooooo   mmmmmm   mmmmmm   mmmmmm    eeeeeeeeeeeeee

    """))

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
    showWelcome()
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
