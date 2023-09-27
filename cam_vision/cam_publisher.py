#!/usr/bin/env python3
import rclpy # Python Client Library for ROS 2
from rclpy.node import Node # Handles the creation of nodes
from sensor_msgs.msg import Image # Image is the message type
from cv_bridge import CvBridge # Package to convert between ROS and OpenCV Images
import cv2 # OpenCV library

class image_converter(Node):
    def __init__(self):
        super().__init__('camera_node')
        self.image_pub = self.create_publisher(Image, 'camera_image', 10)
        timer_period = 0.1  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.camera = cv2.VideoCapture(0)
        self.bridge = CvBridge()

    def timer_callback(self):
        ret, frame = self.camera.read()
          
        if ret == True:
            self.image_pub.publish(self.bridge.cv2_to_imgmsg(frame))


def main(args=None):
    rclpy.init(args=args)
    image_publisher = image_converter()
    rclpy.spin(image_publisher)

    image_publisher.destroy_node()
    rclpy.shutdown()
  
if __name__ == '__main__':
  main()