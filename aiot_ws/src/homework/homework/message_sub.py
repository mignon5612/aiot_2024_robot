import rclpy
from rclpy.node import Node
from rclpy.qos import (
    QoSDurabilityPolicy,
    QoSHistoryPolicy,
    QoSProfile,
    QoSReliabilityPolicy,
    # qos_profile_sensor_data
)
from std_msgs.msg import String


class Message_pub(Node):
    def __init__(self):
        super().__init__("message_pub")
        self.qos_profile = QoSProfile(history=QoSHistoryPolicy.KEEP_ALL,
                                      reliability=QoSReliabilityPolicy.RELIABLE,
                                      durability=QoSDurabilityPolicy.TRANSIENT_LOCAL)
        # self.qos_profile = qos_profile_sensor_data
        self.create_subscription(String, "send", self.sub_callback, self.qos_profile)

    def sub_callback(self, msg: String):
        print(msg.data)

def main():
    rclpy.init()
    node = Message_pub()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.destroy_node()

if __name__ == "__main__":
    main()
