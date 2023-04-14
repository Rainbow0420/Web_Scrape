# Image and Data Download

import requests
import urllib3
from urllib.parse import urlparse
import os
import glob
import subprocess
from PIL import Image
from selenium import webdriver
import moviepy.editor as mp

url = "https://sp-ao.shortpixel.ai/client/to_auto,q_lossy,ret_img,w_1080,h_720/https://authoraditiagarwal.com/wp-content/uploads/2022/04/3d-scaled.jpg"

# File name extract
a = urlparse(url)
imgPath = a.path
imgName = os.path.basename(imgPath)
print(imgPath)
print(imgName)

# Image extract
r = requests.get(url) 
with open("ThinkBig.png",'wb') as f:
   f.write(r.content) 

# Image Thumbnail extract
for infile in glob.glob("ThinkBig.png"):
   img = Image.open(infile)
   img.thumbnail((128, 128), Image.ANTIALIAS)
   if infile[0:2] != "Th_":
      img.save("Th_" + infile, "png")

# Screenshot extract
path = r'C:\\Users\\gaurav\\Desktop\\Chromedriver'
browser = webdriver.Chrome(executable_path = path)
browser.get('https://tutorialspoint.com/')
screenshot = browser.save_screenshot('screenshot.png')
browser.quit

# Video extract
m_url = "https://aimyon.get1by1.com/cdn/files2/TV_Series/Bob_Burgers/Season_9/Bobs_Burgers_S09E22_kissTVSeries.com.mp4"
def download_file(url,filename):
    # NOTE the stream=True parameter
    r = requests.get(url, stream=True)
    with open(filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024): 
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)
                #f.flush() commented by recommendation from J.F.Sebastian       
    return filename

download_file(m_url,"download.mp4")

# Audio Clip Extract
clip = mp.VideoFileClip('download.mp4')
clip.audio.write_audiofile("movie_audio.mp3")
