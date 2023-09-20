#!/usr/bin/env python3
import sys
import rospy
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

class image_converter:
    def __init__(self):
        rospy.init_node('camera_node', anonymous=True)
        self.camera = cv2.VideoCapture(0)
        #self.ret, self.frame = self.camera.read()
        self.image_pub = rospy.Publisher("camera_image",Image, queue_size=10)
        self.bridge = CvBridge()
        self.rate = rospy.Rate(50)


    
    def run(self):
        while not rospy.is_shutdown():
            ret, frame = self.camera.read()
            crop = frame[0:frame.shape[0], int(frame.shape[1]/2):frame.shape[1]]
            reduced = cv2.resize(crop, (0, 0), fx = 0.1, fy = 0.1)
            self.publish(reduced)
            self.rate.sleep()


    def publish(self, frame):
        try:
            self.image_pub.publish(self.bridge.cv2_to_imgmsg(frame, "passthrough"))
        except CvBridgeError as e:
            print(e)

def main(args):
    
    ic = image_converter()
    
    try:
        ic.run()
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting down")
        ic.camera.release()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    main(sys.argv)