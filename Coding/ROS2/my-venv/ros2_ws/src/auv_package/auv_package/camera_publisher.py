import rclpy
from rclpy.node import Node
import cv2
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
from std_msgs.msg import String

class CameraPublisher(Node):
    
    def __init__(self):
        super().__init__('camera_publisher')
        self.dir = "/home/pratham/Documents/AUV/Coding/ROS2/my-venv/ros2_ws/src/auv_package/auv_package/Python/test_images/"
        self.node_name = "Camera Publisher: "
        self.publishing_node_name = "Vision Detector: "
        self.image_publisher = self.create_publisher(Image, 'camera', 10)
        self.br = CvBridge()
        self.feedback_publisher = self.create_publisher(String, 'feedback_topic', 10)
        self.feedback = String()
        self.feedback.data = self.node_name + "Detector Ready?"
        self.feedback_publisher.publish(self.feedback)
        self.feedback_subscription = self.create_subscription(
            String,
            'feedback_topic',
            self.feedback_callback,
            10)
        self.i = 0

    def feedback_callback(self, msg):
        if msg.data == self.publishing_node_name + "Detector Ready":
            self.feedback.data = self.node_name + f"Sending Image {self.i}"
            self.feedback_publisher.publish(self.feedback)
            img_path = self.dir + "test_image_1.jpeg"
            img = cv2.imread(img_path)
            self.image_publisher.publish(self.br.cv2_to_imgmsg(img))
            self.get_logger().info("Published Image: %d" % self.i)
            self.i += 1

def main(args=None):
    rclpy.init(args=args)

    camera_publisher = CameraPublisher()

    rclpy.spin(camera_publisher)
    
    camera_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
