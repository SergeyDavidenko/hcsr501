#!/usr/bin/python
# HC-SR501 motion sensor
# Raspberry Pi 3+ testing

import requests
import RPi.GPIO as GPIO
import time
import pygame


GPIO.setmode(GPIO.BOARD)
PIN = 26
GPIO.setup(PIN, GPIO.IN)


try:
	from settings_local import *
        print "Local settings import success!"
except:
	print "No local settings!"
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
      pygame.mixer.init()
      pygame.mixer.music.load("sound/Wake-up-sounds.mp3")
      pygame.mixer.music.play()
      time.sleep(60)
   time.sleep(1)
