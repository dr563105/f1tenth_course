import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class MoveTurtlebot(Node):

    def __init__(self):
        super().__init__('move_turtlebot')
        self.msg = None
        self.my_cmd_vel_pub = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.timer = self.create_timer(3, self.timer_callback)

    def timer_callback(self):
        msg = Twist()
        msg.linear.x = 0.5
        msg.angular.z = 0.0
        self.get_logger().info(f'Moving with linear velocity of {msg.linear.x}m/s')
        self.my_cmd_vel_pub.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    mt = MoveTurtlebot()
    rclpy.spin(mt)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
