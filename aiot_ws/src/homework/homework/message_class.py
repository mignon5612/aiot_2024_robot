import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Message(Node):
    def __init__(self):
        super().__init__("message")
        self.create_timer(1, self.print_romi)
        self.pub = self.create_publisher(String, "send", 10)
        self.number = 0

    def print_romi(self):
        msg = String()
        msg.data = f"hello, my name is ROMI! + {self.number}"
        self.pub.publish(msg)
        print("hello, my name is ROMI!")
        self.number += 1

def main():
    rclpy.init()
    node = Message()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.destroy_node()

if __name__ == "__main__":
    main()
