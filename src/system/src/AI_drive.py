#!/usr/bin/python2
import roslib
roslib.load_manifest('system')
import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

class image_view_from_msg:
    def __init__(self):
        self.image_pub = rospy.Subscriber("cv2_raw_camera",data_class =  Image, callback=self.callback)
        self.bridge = CvBridge()

    def callback(self,data):
        try:
            cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
        except CvBridgeError as e:
            print(e)
        cv2.imshow("camera_view", cv_image)
        i = cv2.waitKey(1)


rospy.init_node('view_camera')
view = image_view_from_msg()
while not rospy.is_shutdown():
    pass
cv2.destroyAllWindows()

