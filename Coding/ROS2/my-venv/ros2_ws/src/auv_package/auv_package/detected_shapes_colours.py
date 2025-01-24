import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class DetectedShapesColours(Node):

    def __init__(self):
        super().__init__('detected_shapes_colours')
        self.feedback_publisher = self.create_publisher(String, 'feedback_topic', 10)
        self.node_name = "Detections Logger: "
        self.subscribed_node_name = "Vision Detector: "
        self.feedback = String()
        self.feedback.data = self.node_name + "Detections Logger Ready"
        self.feedback_publisher.publish(self.feedback)
        self.create_subscription(
            String,
            'detections',
            self.detections_callback,
            10)
        self.create_subscription(
            String,
            'feedback_topic',
            self.feedback_callback,
            10)
        self.i = 0

    def detections_callback(self, msg):
        self.feedback.data = self.node_name + f"Received Detections {self.i}"
        self.feedback_publisher.publish(self.feedback)
        self.get_logger().info(msg.data)
        self.i += 1

    def feedback_callback(self, msg):
        if msg.data == self.subscribed_node_name + "Detections Logger Ready?":
            self.feedback.data = self.node_name + "Detections Logger Ready"
            self.feedback_publisher.publish(self.feedback)

def main(args=None):
    rclpy.init(args=args)

    detected_shapes_colours = DetectedShapesColours()

    rclpy.spin(detected_shapes_colours)

    detected_shapes_colours.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
