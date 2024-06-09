######### SERVO ########
########################
### IMPORT LIBRARIES ###
########################
#  \      /            #
#   \(oo)/ 	       #
#    |>>|	       #
#   _|__|_             #
#  _|	  |_	       #
########################
from time import *
from adafruit_servokit import ServoKit

### DEFINING INITIAL ANGLES ###
kit.servo[0].angle = 0
kit.servo[1].angle = 0
kit.servo[2].angle = 0
kit.servo[3].angle = 0

kit.servo[4].angle = 0
kit.servo[5].angle = 0
kit.servo[6].angle = 0
kit.servo[7].angle = 0

kit.servo[8].angle = 0
kit.servo[9].angle = 0
kit.servo[10].angle = 0
kit.servo[11].angle = 0

kit.servo[12].angle = 0
kit.servo[13].angle = 0
kit.servo[14].angle = 0
kit.servo[15].angle = 0

### EACH KIT DEFINES A SERVO CHANEL ###
#######################################
## TIME TO SLEEP ###
####################

sleep(2)
###########################
## DEFINES SLEEPING TIME ##
## IN WHICH TIMESTEPS    ##
## THE SERVOS SYNCHRONIES##
###########################

t=.5

while True:
    
    kit.servo[0].angle = 180
    sleep(t)
    kit.servo[0].angle = 0
    sleep(t/2)
    kit.servo[1].angle = 180
    sleep(t)
    kit.servo[1].angle = 0
    sleep(t/2)
    kit.servo[2].angle = 180
    sleep(t)
    kit.servo[2].angle = 0
    sleep(t/2)
    kit.servo[3].angle = 180
    sleep(t)
    kit.servo[3].angle = 0
    sleep(t/2)

    kit.servo[4].angle = 180
    sleep(t)
    kit.servo[4].angle = 0
    sleep(t/2)
    kit.servo[5].angle = 180
    sleep(t)
    kit.servo[5].angle = 0
    sleep(t/2)
    kit.servo[6].angle = 180
    sleep(t)
    kit.servo[6].angle = 0
    sleep(t/2)
    kit.servo[7].angle = 180
    sleep(t)
    kit.servo[7].angle = 0
    sleep(t/2)

    kit.servo[8].angle = 180
    sleep(t)
    kit.servo[8].angle = 0
    sleep(t/2)
    kit.servo[9].angle = 180
    sleep(t)
    kit.servo[9].angle = 0
    sleep(t/2)
    kit.servo[10].angle = 180
    sleep(t)
    kit.servo[10].angle = 0
    sleep(t/2)
    kit.servo[11].angle = 180
    sleep(t)
    kit.servo[11].angle = 0
    sleep(t/2)

    kit.servo[12].angle = 180
    sleep(t)
    kit.servo[12].angle = 0
    sleep(t/2)
    kit.servo[13].angle = 180
    sleep(t)
    kit.servo[13].angle = 0
    sleep(t/2)
    kit.servo[14].angle = 180
    sleep(t)
    kit.servo[14].angle = 0
    sleep(t/2)
    kit.servo[15].angle = 180
    sleep(t)
    kit.servo[15].angle = 0
    sleep(t/2)
    
    
    t = t/1.5


