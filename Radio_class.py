# -*- coding: utf-8 -*-

"""
Create a Radio class with characteristics and functionality discussed
 in the session/video.
      
Create the object of the Radio class and start the radio and play 
a song.

Hint:

Characteristics    |   Functionality
---------------------------------------
color              |
brand              |
ACPower            |
headphone          |
                   |
power_led          | power_switch  ( ON / OFF)
mode_led           | mode_switch   ( AM / FM )
frequency          | band_tuner    ( 88 - 108 )
volume             | volume_tuner  ( 1 - 10 )
---------------------------------------


Characteristics are mapped into data/variables
Functionality are mapped into methods/functions
Class is a blueprint for creating instances (objects)


How should I be able use Radio class: 

I should be able to 
Go to the market and buy a new Radio
Switch ON the radio
Set the mode to FM
Set the frequency to 102.2
Set the volume to 8
Listen to your song
Switch OFF the radio
Destroy the Radio
"""




#Class
class Radio:
    color = "Brown"
    brand = "Sony"
    ACpower = False
    headphone = False

#Constructor  
    def __init__(self):
        self.power_led = "ON"
        self.mode_led = None
        self.frequency = 0.0
        self.volume = 0
        print("Your Radio is ready to be played")
        
    #Instance Methods
    def power_switch(self,power_status):
        self.power_led = power_status
        print("Your power status is "+str(self.power_led))
        
    def mode_switch(self,switch_status):
        self.mode_led = switch_status
        print("Your Radio mode is set to"+str(self.mode_led))
        
    def band_tuner(self,frequency_val):
        self.frequency = frequency_val
        print("Your Radio frequency is set to"+str(self.frequency))
        
    def volume_tuner(self,volume_status):
        self.volume = volume_status
        print("Your volume is "+str(self.volume))
    
#Instance

my_radio = Radio()

print("Color of my radio is = "+ str(my_radio.color))
print("Brand of my radio is = "+ str(my_radio.brand))

#SET ON
my_radio.power_switch("ON")

#Radio FM
my_radio.mode_switch("FM")

#frequency
my_radio.band_tuner(81.3)

#Volume
my_radio.volume_tuner(15)

#Switch off the radio
my_radio.power_switch("OFF")

#Destroy the radio
my_radio = None