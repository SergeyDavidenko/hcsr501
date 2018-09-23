#!/usr/bin/python
# HC-SR501 motion sensor

import requests
import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BOARD)
PIN = 26
GPIO.setup(PIN, GPIO.IN)


try:
	import settings_local.py
except:
	print "No local settings"
	BOT = ""
	CHAT_ID = ""


def send_telegram(text):
    requests.get(
        'https://api.telegram.org/{}/sendMessage?chat_id={}&text={}'.format(BOT, CHAT_ID, str(text)))


print "Start sensor..."
time.sleep(2)
print "Sensor activated..."

while True:
   if GPIO.input(PIN):
      print "Movement detected! " + (time.strftime("%H:%M:%S"))
      send_telegram("Movement detected! " + (time.strftime("%H:%M:%S")))
      time.sleep(5)
   time.sleep(1)