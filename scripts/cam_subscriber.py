#!/usr/bin/env python3
import sys
import rospy
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

class image_converter:

  def __init__(self):
    rospy.init_node('camera_sub_display', anonymous=True)
    self.bridge = CvBridge()
    self.image_sub = rospy.Subscriber("camera_image",Image,self.callback)

  def callback(self,data):
    try:
      cv_image = self.bridge.imgmsg_to_cv2(data, "passthrough")
      #print(cv_image.shape)
    except CvBridgeError as e:
      print(e)

    # (rows,cols,channels) = cv_image.shape
    # if cols > 60 and rows > 60 :
    #   cv2.circle(cv_image, (50,50), 10, 255)

    cv2.imshow("Remote Video", cv_image)
    cv2.waitKey(1)


def main(args):
    ic = image_converter()
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting down")
        cv2.destroyAllWindows()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main(sys.argv)