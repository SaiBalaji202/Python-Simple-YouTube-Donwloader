import pytube
# To install pytube, you have to first download pip package manager from the following link
# https://pip.pypa.io/en/stable/installing/#do-i-need-to-install-pip
# Now you want to install pythube by typing the following command
# python -m pip install pytube -->For Windows OS by opening Cmd Prompt as Admin
# pip install pytube -->For Linux OS

lnk = input("Enter the Youtube Link: ")
yt = pytube.YouTube(lnk) # Collect All Basic details about the URL you have passed and store it in yt object

videos = yt.get_videos() # Get all download links of the URL which is stored in yt object and then store it in videos object

# List File Name to download and list all Download Options to the Users
print(yt.filename)
cnt = 1
for video in videos:
    print(cnt, video)
    cnt += 1
choice = int(input("Enter your Choice: "))

# Get destination folder to store the downloaded video
dest_path = input("Enter your Destination Directory Full Path: ")

# Start downloading the chosen video to the destination directory
videos[choice - 1].download(dest_path) # Here we use choice - 1, because the index value always starts from 0.  But we list the options from 1 and not from 0.  So, we subtract 1 from user choice

# Now the download completed
print(yt.filename, " download completed")

# Getting the details of the downloaded video
str_vid_details = str(videos[choice - 1])

# Importing startfile function from os package
from os import startfile
# Checking whether the last character of our path is "\\" or "/" and then start the downloaded file using startfile("path of file to start") function.  To open this downloaded file using specific process
if dest_path[len(dest_path) - 1] == "\\" or dest_path[len(dest_path) - 1] == "/":
    startfile(dest_path + yt.filename + str_vid_details[str_vid_details.find("(") + 1 : str_vid_details.find(")")]) # startfile(Directory + File Name + File Extension)
else:
    startfile(dest_path + "\\" + yt.filename + str_vid_details[str_vid_details.find("(") + 1 : str_vid_details.find(")")])  # startfile(Directory + File Name + File Extension)

    # To open this downloaded file using specific process, use Popen[Process Name, File to Open using that Process]
#from subprocess import Popen
    ## To Open the downloaded file in VLC Media Player
#Popen(["C:/Program Files (x86)/VideoLAN/VLC/vlc.exe",dest_path + "\\" + yt.filename + str_vid_details[str_vid_details.find("(") + 1 : str_vid_details.find(")")]])
