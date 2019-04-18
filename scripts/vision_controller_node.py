#!/usr/bin/python
import rospy
import rosservice
from marvin_convnet.srv import DetectObjects
from vision_control.srv import ProcessImages
from std_msgs.msg import Bool, String, Int8
from geometry_msgs.msg import Pose

# 

class vision_control_node():

	def __init__(self):

		self.node_name = "vision_control"
		#rate
		self.rate = rospy.Rate(1)
		# initialize vision status variable
		self.vision_status = 0
		# define a service
		self.srv = rospy.Service('VisionSystem', ProcessImages, self.visioncontrolcallback) 
		

	def __enter__(self):
		#start the node
		rospy.init_node(self.node_name, anonymous=True)

	def __exit__(self, type, value, tb):
		pass

	def visioncontrolcallback(self, data):
		# get the status that the main controller is sending 
		self.controller_status = data.McStatus
		self.item_name = data.ItemName
		self.shelf_id = data.ShelfId
		self.EE2W = data.InterfaceJoint
		return_packet = ProcessImages();
 		
		if self.controller_status == 0  :
			# initialization process
			service_list = rosservice.get_service_list()
			if (('/save_images') in service_list):
				rospy.loginfo("Initialization completed")
			else:
				rospy.loginfo("Services do not exist")
			self.vision_status = self.controller_status
			return_packet.VisionStatus = self.vision_status
			return_packet.ItemPose = Pose()
			return_packet.ItemBoundingBox = []
			
			
		elif self.controller_status > 0 and self.controller_status < 16:
			# take picture
			rospy.loginfo("Taking a picture")
			curr_frame = self.controller_status - 1
			
			if self.shelf_id < 0 or self.shelf_id >= 12:
				rospy.loginfo("shelf_id out of bounds of assumed 12 bins, defaulting to bin 0/A")
				self.shelf_id = 0
			
			
			#can specify a timeout in seconds to wait for the server, if timeout is exceeded ROSException is raised
			rospy.wait_for_service('/save_images', timeout=None) 
			save_images = rospy.ServiceProxy('/save_images', DetectObjects)
			try:
				# arguments to be passed need to be checked
				# assumed that only one item in a shelf
				resp1 = save_images([self.item_name], self.shelf_id, curr_frame) 
			except rospy.ServiceException as exc:
				rospy.loginfo("Service did not process request: " + str(exc)
	
		else:
			# calculate item pose
			rospy.loginfo("Calculating Item pose")
		
		#update the vision statusexists
		return return_packet

if __name__ == "__main__":

	""" Run RosNode """

with vision_control_node():
	try:
		while not rospy.is_shutdown():
			rospy.spin()
	except KeyboardException:
		ropy.loginfo("Keyboard Exception caught, closing)



