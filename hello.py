import sys, unittest, time, datetime
import urllib.request, urllib.error, urllib.parse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import InvalidArgumentException
import os 
os.system("python app.py")
#import the package
from pytube import YouTube

url = sys.argv[1]
channelid = url.split('/')[4]
#driver=webdriver.Firefox()
driver=webdriver.Chrome("C:/chromedriver.exe")
driver.get(url)
time.sleep(5)
dt=datetime.datetime.now().strftime("%Y%m%d%H%M")
height = driver.execute_script("return document.documentElement.scrollHeight")
lastheight = 0
while True:
	if lastheight == height:
		break
	lastheight = height
	driver.execute_script("window.scrollTo(0, " + str(height) + ");")
	time.sleep(2)
	height = driver.execute_script("return document.documentElement.scrollHeight")

user_data = driver.find_elements_by_xpath('//*[@id="video-title"]')
links=[ ]
for i in user_data:
	print(i.get_attribute('href'))
	link = (i.get_attribute('href'))
	f = open(channelid+'-'+dt+'.list', 'a+')
	f.write(link + '\n')
	links.append(link)
	my_video = YouTube(link)

	print("*********************Video Title************************")
	#get Video Title
	print(my_video.title)

	print("********************Tumbnail Image***********************")
	#get Thumbnail Image
	print(my_video.thumbnail_url)

	print("********************Download video*************************")
	#get all the stream resolution for the 
	for stream in my_video.streams:
		print(stream)

	#set stream resolution
	my_video = my_video.streams.get_highest_resolution()

	#or
	#my_video = my_video.streams.first()

	#Download video
	my_video.download()
print(links)
f.close