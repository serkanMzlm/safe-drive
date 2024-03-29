import cv2
import os

import rclpy
from rclpy.node import Node
from cv_bridge import CvBridge
from sensor_msgs.msg import Image

class Recorder(Node):
  def __init__(self):
    super().__init__('camera_rec')
    self.sub_ = self.create_subscription(Image, 'camera', self.callbackCamera, 10)
    
    video_path = os.path.join(os.getcwd(), "front_camera.avi")
    self.out = cv2.VideoWriter(video_path, cv2.VideoWriter_fourcc('M','J','P','G'),
                             15, (360, 360))
    self.bridge = CvBridge()
    
  def callbackCamera(self, data):
    frame = self.bridge.imgmsg_to_cv2(data, 'bgr8')
    self.out.write(frame)
    cv2.imshow("Front Camera", frame)
    cv2.waitKey(1)

def main(args = None):
  rclpy.init(args=args)
  image_sub = Recorder()
  rclpy.spin(image_sub)    
  rclpy.shutdown()

if __name__ == '__main__':
  main()