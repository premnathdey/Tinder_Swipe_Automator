import pyautogui
import webbrowser
import time
import random
from random import randint

"""
Free Version: 1000 swipes per 12-hour period.
How to: User must be logged in prior start
        Works best when in full screen mode in browser"""

url = r'https://tinder.com'

# MacOS
chrome_path = 'open -a /Applications/Google\ Chrome.app %s'

# Windows1
# chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

# Linux
# chrome_path = '/usr/bin/google-chrome %s' 
tim= randint(5,10)
webbrowser.get(chrome_path).open(url)
time.sleep(tim)
pyautogui.click(button='right')
time.sleep(tim)


for x in range(0, 1000):
	y = randint(0, 1)
	if y == 0:
		pyautogui.press('left')
		tim1= randint(3,7)
		time.sleep(tim1)
	elif y == 1:
		pyautogui.press('right')
		tim2= randint(3,7)
		time.sleep(tim2)
	elif x == 100:
		print ("EXIT")
		break

	print(x)



