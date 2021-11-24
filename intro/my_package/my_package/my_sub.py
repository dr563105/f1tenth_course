import rclpy
from rclpy.node import Node

#from std_msgs.msg import String
from custom_interfaces.msg import Num 

class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        #self.subscriber = self.create_subscription(String, 'my_topic', self.listener_callback, 1)
        self.subscriber = self.create_subscription(Num, 'my_topic', self.listener_callback, 1)

    def listener_callback(self, msg):
        #self.get_logger().info(f"I heard {msg.data}")
        self.get_logger().info(f"I heard {msg.num}")

def main(args=None):
    rclpy.init(args=args)
    ms = MinimalSubscriber()
    rclpy.spin(ms)

if __name__ == '__main__':
    main()
    

