#!/usr/bin/env python3
import rclpy 
from rclpy.node import Node 
from sensor_msgs.msg import Image 
from cv_bridge import CvBridge 
import cv2 

class image_converter(Node):
    def __init__(self):
        super().__init__('camera_sub_display')
        self.declare_parameter("cam_number", 0)
        num_camera = self.get_parameter('cam_number').get_parameter_value().integer_value
        self.bridge = CvBridge()
        self.subscription = self.create_subscription(Image, 'camera_image'+str(num_camera), self.callback, 10)
        self.subscription

  
    def callback(self,data):
        cv_image = self.bridge.imgmsg_to_cv2(data)

        # (rows,cols,channels) = cv_image.shape
        # if cols > 60 and rows > 60 :
        #   cv2.circle(cv_image, (50,50), 10, 255)

        cv2.imshow("Remote Video", cv_image)
        cv2.waitKey(1)


def main(args=None):
  rclpy.init(args=args)
  image_subscriber = image_converter()
  rclpy.spin(image_subscriber)
  

  image_subscriber.destroy_node()
  rclpy.shutdown()
  
if __name__ == '__main__':
  main()