import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import Detector
import sys

class VisionDetector(Node):

    def __init__(self):
        super().__init__('vision_detector')
        self.obj = Detector.VisionDetector()
        self.node_name = "Vision Detector: "
        self.subscribed_node_name = "Camera Publisher: "
        self.publishing_node_name = "Detections Logger: "
        self.feedback_publisher = self.create_publisher(String, 'feedback_topic', 10)
        self.detections_publisher = self.create_publisher(String, 'detections', 10)
        self.feedback = String()
        self.feedback.data = self.node_name + "Detector Ready"
        self.feedback_publisher.publish(self.feedback)
        self.camera_subscription = self.create_subscription(
            Image,
            'camera',
            self.image_callback,
            10)
        self.feedback_subscription = self.create_subscription(
            String,
            'feedback_topic',
            self.feedback_callback,
            10)
        self.br = CvBridge()
        self.i = 0
        self.processing = False
        self.published = False
        self.publish_msg = String()

    def feedback_callback(self, msg):
        if msg.data == (self.subscribed_node_name + "Detector Ready?"):
            if not self.processing:
                self.feedback.data = self.node_name + "Detector Ready"
                self.feedback_publisher.publish(self.feedback)
        elif msg.data == (self.publishing_node_name + "Detections Logger Ready"): 
            if not self.processing and not self.published and self.publish_msg.data != "":
                self.detections_publisher.publish(self.publish_msg)
                self.published = True
        elif len(msg.data) > (len(self.publishing_node_name) + 19) and msg.data[:(len(self.publishing_node_name) + 19)] == (self.publishing_node_name + "Received Detections"):
            self.feedback.data = self.node_name + "Detector Ready"
            self.feedback_publisher.publish(self.feedback)

    def image_callback(self, data):
        self.feedback.data = self.node_name + f"Received Image {self.i}, Processing..."
        self.feedback_publisher.publish(self.feedback)
        self.get_logger().info("Received Image %d, Processing..." % self.i)
        self.processing = True
        self.published = False
        img = self.br.imgmsg_to_cv2(data)
        sys.setrecursionlimit(img.shape[0]*img.shape[1])
        colours_detected = self.obj.colour_detector(img)
        shapes_detected = self.obj.shape_detector(img, colours_detected)
        temp_msg = f"\nIn Image {self.i}:"
        temp_msg += "\nColours Detected are: "
        for colour in colours_detected:
            if len(colours_detected[colour]) != 0:
                temp_msg += f"{colour}, "
        if temp_msg == f"\nIn Image {self.i}:\nColours Detected are: ":
            temp_msg = "No Colours Detected."
        else:
            temp_msg = temp_msg[:-2] + "."
        temp_msg += "\nShapes Detected are: "
        for shape in shapes_detected:
            temp_msg += f"{shape}, "
        if temp_msg[-5:] == "are: ":
            temp_msg = temp_msg[:-21] + "No Shapes Detected."
        else:
            temp_msg = temp_msg[:-2] + "."
        self.publish_msg.data = temp_msg
        self.feedback.data = self.node_name + f"Processed Image {self.i}"
        self.feedback_publisher.publish(self.feedback)
        self.get_logger().info("Processed Image %d" % self.i)
        self.i += 1
        self.processing = False
        self.feedback.data = self.node_name + "Detections Logger Ready?"
        self.feedback_publisher.publish(self.feedback)

def main(args=None):
    rclpy.init(args=args)
    
    vision_detector = VisionDetector()

    rclpy.spin(vision_detector)

    vision_detector.destroy_node()

    rclpy.shutdown()
   
main()
