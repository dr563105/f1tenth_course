import rclpy
from rclpy.node import Node

#from std_msgs.msg import String
from custom_interfaces.msg import Num 

class MinimalPublisher(Node):
    
    def __init__(self):
        super().__init__(node_name='minimal_publisher')
        #self.publisher = self.create_publisher(String, 'my_topic', 1)
        self.publisher = self.create_publisher(Num, 'my_topic', 1)
        self.timer = self.create_timer(2.0, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        #msg = String()
        msg = Num()
        #msg.data = f"Hello World: {self.i}"
        msg.num = self.i
        self.publisher.publish(msg)
        #self.get_logger().info(f"Publishing: {msg.data}")
        self.get_logger().info(f"Publishing: {msg.num}")
        self.i +=1

def main(args=None):
    rclpy.init(args=args)
    mp = MinimalPublisher()
    rclpy.spin(mp)


if __name__ == '__main__':
    main()
