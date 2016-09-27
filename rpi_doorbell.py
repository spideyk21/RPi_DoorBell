#!/usr/bin/env python3
#title           : rpi_doorbell.py
#description     : Raspberry Pi Doorbell
#author          : spideyk21
#date            : MM/DD/YYYY
#version         : X.X
#usage           : 
#refrence        : https://learn.adafruit.com/usb-audio-cards-with-a-raspberry-pi
#				   https://learn.adafruit.com/playing-sounds-and-using-buttons-with-raspberry-pi
#
#python_version  : 3.0
#notes			 : written using gpiozero (https://gpiozero.readthedocs.org/)
#==============================================================================

# Import required Python libraries
from gpiozero import LED, Button
from datetime import datetime
import time
import os

#Inputs
button1 = Button(#)
button2 = Button(#)
button3 = Button(#)
button4 = Button(#)
button5 = Button(#)
button6 = Button(#)
button7 = Button(#)
button8 = Button(#)

#Outputs
led1 = LED(#)
led2 = LED(#)
led3 = LED(#)
led4 = LED(#)
led5 = LED(#)
led6 = LED(#)
led7 = LED(#)
led8 = LED(#)

While True:
	if button1.is_pressed:
		led1 = led.on
		os.system('mpg123 -q song.mp3 &') #play song1
		led1 = led.off
	
	elif button2.is_pressed:
		led1 = led.on
		#play song1
		led1 = led.off