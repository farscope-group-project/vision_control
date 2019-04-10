#!/usr/bin/python

import rospy

from std_msgs.msg import Bool, String, Int8
import random
from random import randint

def vision_tmc():
	# set up a publisher
	pub = rospy.Publisher('Vision_System_Status', Int8, queue_size=1)
	# start the node
	rospy.init_node('driver')

	while not rospy.is_shutdown():
		message = randint(0,15) # this should be replaced with the status   
		rospy.loginfo("Vision system status=%d"%message)
		pub.publish(message)
		# update at 1 Hz
		r = rospy.Rate(1)
		# wait for next time
		r.sleep()

 ######### run from here ##############

vision_tmc()
