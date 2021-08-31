#carControl
#

import time
import os
import RPi.GPIO as GPIO
import subprocess
import pigpio
import sys



GPIO.setmode(GPIO.BCM)#set mode to BCM
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#T=0.0015+0.02
#f=1/T
#dc=0.0015/(0.0015+0.02)*100=6.9767---calibriation signal

def  control_servo(ser_num, direction):#Two parameter dicide state of servos

    if ser_num=="Left":
	if direction=="clockwise":
	    print " Left servo, clockwise"
	    dc=6.9767*10000
	    pi_hw.hardware_PWM(13,46.5,dc)
	elif direction=="stop":
	    print " Left servo, stop"
	    pi_hw.hardware_PWM(13,0,0)# complete stop when duty cycle=0, no output
	elif direction=="counter-clockwise":
	    print " Left servo, counter-clockwise"
	    dc=6.9767*10000#duty cycle in %
	    pi_hw.hardware_PWM(13,46.5,dc)
	    
         
    elif ser_num=="Right":# Do the same as for Left servo
	if direction=="clockwise":
	    print " Right servo, clockwise"
	    dc=6.9767*10000#duty cycle in %
	    pi_hw.hardware_PWM(12,46.5,dc)
	elif direction=="stop":
	    print " Right servo, stop"
	    pi_hw.hardware_PWM(12,0,0)
	elif direction=="counter-clockwise":
	    print " Right servo, counter-clockwise"
            dc=6.9767*10000
	    pi_hw.hardware_PWM(12,46.5,dc)
    
  

pi_hw = pigpio.pi()  # connect to pi gpio daemon
resume=0 # stop/ start
flag=1# flag to end while loop


while flag:
     time.sleep(0.2)  # Without sleep, no screen output!
            
     if ( not GPIO.input(17) ):#when button pressed pin connected to ground, GPIO.input(17)=0;
        if(resume==0):
                control_servo("Left", "clockwise")
	    	control_servo("Right", "counter-clockwise")
	    	resume=1

        elif(resume==1):
	    	control_servo("Left", "stop")
		control_servo("Right", "stop")
		resume=0
     
		 
     if ( not GPIO.input(27) ):
         flag=0


pi_hw.stop() #close pi gpio DMA resources
GPIO.cleanup()#aviod conflt when other program running 