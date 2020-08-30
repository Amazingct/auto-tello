#!/usr/bin/python2
import roslib
roslib.load_manifest('system')
import rospy
import cv2
from sensor_msgs.msg import CompressedImage
from sensor_msgs.msg import Image

from cv_bridge import CvBridge, CvBridgeError

class image_view_from_msg:
    def __init__(self):
        self.image_pub = rospy.Subscriber("/tello/cv_image/compressed",data_class = CompressedImage,
        callback=self.callback)
        self.bridge = CvBridge()

    def callback(self,data):
        try:
            cv_image = self.bridge.compressed_imgmsg_to_cv2(data, "bgr8")
        except CvBridgeError as e:
            print(e)
        cv2.imshow("camera_view", cv2.resize(src=cv_image, dsize=(400, 220)))
        i = cv2.waitKey()


rospy.init_node('view_camera')
view = image_view_from_msg()
while not rospy.is_shutdown():
    pass
cv2.destroyAllWindows()

'''
rosrun image_transport republish h264 in:=/tello/image_raw compressed out:= new_one
'''
