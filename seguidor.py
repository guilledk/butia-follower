import os
import sys
sys.path.insert(0, '~/Proyecto/code/turtlebots/butia')

from pybot import usb4butia
from time import sleep

robot = usb4butia.USB4Butia()
robot.find_butias()
robot.reconnect()

def clear() :
	os.system('clear')

def getAverage(rt,port1,port2) :
	clear()
	print "Grey Scale Average v1.0"
	go = input("Type 'go' when ready: ")
	if(go == "go") :

		print "Geting white value in ",
		for x in range(5) :
			sleep(1)
			print x, " ",

		white1 = rt.getGray(port1)
		white2 = rt.getGray(port2)

		print "Geting black value in ",
		for x in range(5) :
			sleep(1)
			print x, " ",

		black1 = rt.getGray(port1)
		black2 = rt.getGray(port2)

		return (white1 + black1) / 2, (white2 + black2) / 2

	else :

		return 0, 0

def followLine(rt,values,greySensor1,greySensor2) :

	if(rt.getGray(greySensor1) < values[0] && rt.getGray(greySensor2) < values[1]) :

		rt.set2MotorSpeed(0, 1000, 0, 1000)

	else :

		if(rt.getGray(greySensor1) > values[0] && rt.getGray(greySensor2) < values[1]) :

			rt.set2MotorSpeed(0, 1000, 1, 1000)

		else :

			rt.set2MotorSpeed(1, 1000, 0, 1000)

if(sys.argv[0] == "-gG") :

		result = getAverage(robot, 5, 6)

	else :

		result = 0, 0

while(True) :
	
	followLine(robot,result,5,6)
