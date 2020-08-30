#!/usr/bin/python2
import roslib
roslib.load_manifest('system')
import rospy
import cv2
from sensor_msgs.msg import CompressedImage
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
face_cascade = cv2.CascadeClassifier('/home/amazing/Desktop/PROJECTS_AND_CODES/ROS/Codes/myprojects/roadsmart_ws/src/system/src/haarcascade_frontalface_default.xml')

class image_view_from_msg:
    def __init__(self):
        self.image_pub = rospy.Subscriber("compressed",data_class = CompressedImage,
        callback=self.callback)
        self.bridge = CvBridge()

        



    def callback(self,data):
        try:
            cv_image = self.bridge.compressed_imgmsg_to_cv2(data, "bgr8")
        except CvBridgeError as e:
            print(e)
        img = cv2.resize(src=cv_image, dsize=(500, 320))
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        for (x, y , w ,h) in faces:
            cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0 , 0), 3)
        # Display the output
        cv2.imshow('img', img)
        i = cv2.waitKey(1)


rospy.init_node('view_camera')
view = image_view_from_msg()
while not rospy.is_shutdown():
    pass
cv2.destroyAllWindows()

'''
rosrun image_transport republish h264 in:=/tello/image_raw compressed out:= new_one
'''
