import cv2
import rclpy
from sensor_msgs.msg import Image
from rclpy.node import Node
from cv_bridge import CvBridge

class SubscriberNodeClass(Node):
    def __init__(self):
        super().__init__('subscriber_node')
        self.cameraDeviceNumber = 0
        self.bridgeObject = CvBridge()
        self.topicNameFrames = '/topic_camara_image'
        self.queueSize = 10
        self.subscription = self.create_subscription(Image,self.topicNameFrames, self.listener_callbackFunction, self.queueSize)
        self.subscription
       

    def listener_callbackFunction(self, imageMessage):
        self.get_logger().info('The image frame is received')
        openCVImage = self.bridgeObject.imgmsg_to_cv2(imageMessage)
        cv2.imshow("Camera Video", openCVImage)

def main(args=None):
    rclpy.init(args = args)
    subscriberNode = SubscriberNodeClass()
    rclpy.spin(subscriberNode)
    subscriberNode.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()