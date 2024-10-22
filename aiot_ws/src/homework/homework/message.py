import rclpy
from rclpy.node import Node

def print_romi():
    print("hello, my name is ROMI!")
    print("ROMI!!")

def main():
    rclpy.init()
    node = Node("message")
    node.create_timer(1, print_romi)
    rclpy.spin(node)

if __name__ == "__main__":
    main()
