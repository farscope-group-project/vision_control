#!/usr/bin/python
import rospy
from std_msgs.msg import Bool, String, Int8

# 

class vision_control_node():

	def __init__(self):

		self.node_name = "vision_control"
		#start the node
		rospy.init_node(self.node_name, anonymous=True)
		#rate
		self.rate = rospy.Rate(1)
		# initialize vision status variable
		self.vision_status = 0
		# define a publisher
		self.vision_pub_response = rospy.Publisher('/VisionResponse', String, queue_size =10)
		#define a subscriber
		self.vision_control_sub = rospy.Subscriber('/Vision_System_Status', Int8, self.visioncontrolcallback)

	def visioncontrolcallback(self,data):
		# get the status that the main controller is sending 
		self.controller_status = data.data
 		
		if self.controller_status == 0  :
			# initialization process
			self.save_image_stat = exists('/save_images')
			self.pose_estim_stat = exists('/pose_estimation')
			if save_image_stat == False or pose_estim_stat == False:
				print("Services do not exist")
			else:
				print("Initialization completed")
			
		elif self.controller_status > 0 and self.controller_status <= 14:
			# take picture
			print("Taking a picture")
			
			rospy.wait_for_service('/save_images', timeout=None) #can specify a timeout in seconds to wait for the server, if timeout is exceeded ROSException is raised
			save_images = rospy.ServiceProxy('/save_images', srv_save)
			try:
				resp1 = save_images([ObjectNames], frameid, shelfid) # arguments to be passed need to be defined (?)
				except rospy.ServiceException as exc:
					print("Service did not process request: " + str(exc)
	
		else:
			# calculate item pose
			print("Calculating Item pose")
		
		#update the vision status
		self.vision_status = self.controller_status
		self.vision_pub_response.publish(self.vision_status)


if __name__ == "__main__":

	""" Run RosNode """

vcn =  vision_control_node()

while not rospy.is_shutdown():
	rospy.spin()


