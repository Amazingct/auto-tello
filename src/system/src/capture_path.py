#!/usr/bin/python2
import roslib
roslib.load_manifest('system')
import rospy
import cv2, os, pickle
from sensor_msgs.msg import Image
from std_msgs.msg import String
from cv_bridge import CvBridge, CvBridgeError
import time
font = cv2.FONT_HERSHEY_SIMPLEX

categories = ["forward", "stop", "right", "left"]

def capture_data(direction_key, snapshot):
    # sub folder for picture to be stored
    data_dir = "/home/amazing/Desktop/PROJECTS_AND_CODES/ROS/data/" + direction_key
    image_name = str(time.time()) + ".jpg"
    print("--", direction_key)
    os.chdir(data_dir)
    cv2.imwrite(image_name, cv2.resize(src=snapshot, dsize=(500, 320)))


class image_view_from_msg:
    _direction = ""
    
    def __init__(self):
        self.image_pub = rospy.Subscriber("cv2_raw_camera",data_class =  Image, callback=self.callback)
        self.movement_pub = rospy.Subscriber("movement", String, self.movement_cb)
        self.bridge = CvBridge()

    def movement_cb(self, data):
        self._direction = data.data
        


    def callback(self,data):
        try:
            cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
        except CvBridgeError as e:
            print(e)
        
        img = cv_image
        cv2.putText(cv_image,self._direction,(10,200), font, 1,(255,255,255),2)
        cv2.imshow("camera_view", cv_image)
        i = cv2.waitKey(1)
        # capture data
        capture_data(self._direction, img)
        


rospy.init_node('view_camera')
view = image_view_from_msg()
while not rospy.is_shutdown():
    pass
cv2.destroyAllWindows()

