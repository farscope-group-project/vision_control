	#!/usr/bin/python
import rospy
import rosservice
from marvin_convnet.srv import DetectObjects
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
		self.vision_control_sub = rospy.Subscriber('/MainController', ControllerPacket, self.visioncontrolcallback)

	def visioncontrolcallback(self,data):
		# get the status that the main controller is sending 
		self.controller_status = data.McStatus
		self.item_name = data.ItemName
		self.shelf_id = data.ShelfId
 		
		if self.controller_status == 0  :
			# initialization process
			service_list = rosservice.get_service_list()
			if (('/save_images') in service_list):
				print("Initialization completed")
			else:
				print("Services do not exist")
			
		elif self.controller_status > 0 and self.controller_status <= 15:
			# take picture
			print("Taking a picture")
			
			rospy.wait_for_service('/save_images', timeout=None) #can specify a timeout in seconds to wait for the server, if timeout is exceeded ROSException is raised
			save_images = rospy.ServiceProxy('/save_images', DetectObjects)
			try:
				resp1 = save_images(self.item_name, self.controller_status, self.shelf_id) # arguments to be passed need to be checked
				except rospy.ServiceException as exc:
					print("Service did not process request: " + str(exc)
	
		else:
			# calculate item pose
			print("Calculating Item pose")
		
		#update the vision statusexists
		self.vision_status = self.controller_status
		self.vision_pub_response.publish(self.vision_status)


if __name__ == "__main__":

	""" Run RosNode """

vcn =  vision_control_node()

while not rospy.is_shutdown():
	rospy.spin()


