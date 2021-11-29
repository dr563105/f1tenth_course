import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math

class MoveTurtlebot(Node):

    def __init__(self):
        super().__init__('move_turtlebot')
        self.twist_msg = Twist()
        self.pose = Pose()
        self.origin_pose_x = 5.5444
        self.origin_pose_y = 5.5444
        self.origin_theta = 0.0
        self.tolerance_distance = 0.5 #range 0.1 - 1. Different turtle need different value.
        self.my_cmd_vel_pub = self.create_publisher(Twist, '/turtle1/cmd_vel', 1)
        self.my_pose_sub = self.create_subscription(Pose, '/turtle1/pose',
                self.pose_cb, 1)
        self.timer = self.create_timer(0.5, self.timer_cb)

    def pose_cb(self, data):
        a, b, c = data.x, data.y, data.theta
        self.pose.x = round(a, 4)
        self.pose.y = round(b, 4)
        self.pose.theta = round(c, 2)
        # self.get_logger().info(f'x: {data.x},y: {data.y}, theta: {round(data.theta, 1)}')

    def euclidean_distance(self):
        return math.sqrt(pow((self.origin_pose_x - self.pose.x), 2) + pow((self.origin_pose_y - self.pose.y), 2))

    def timer_cb(self):
        self.my_cmd_vel_pub.publish(self.twist_msg)
        # self.get_logger().info(f'Current position: ({self.pose.x}, {self.pose.y})')
        # self.get_logger().info(f'ED before: {self.euclidean_distance()}')
        # if (self.pose.theta == self.origin_theta):
        if (self.euclidean_distance() <= self.tolerance_distance):
            # self.get_logger().info(f'ED after: {self.euclidean_distance()}')
            self.twist_msg.angular.z = 0 - self.twist_msg.angular.z
            self.my_cmd_vel_pub.publish(self.twist_msg)

def main(args=None):
    rclpy.init(args=args)
    mt = MoveTurtlebot()
    linear_velocity = float(input("Enter Linear velocity between 2.0 and 6.0: "))
    if (2.0 <= linear_velocity <= 6.0):
        angular_velocity = float(input("Enter Angular velocity between 1.0 and 3.0: "))#0.1
        if(0.0 <= angular_velocity <= 3.0):
            mt.twist_msg.linear.x = linear_velocity
            mt.twist_msg.angular.z = -angular_velocity
            rclpy.spin(mt)
        else:
            print("Error! - Value of angular velocity must be between 1.0 and 3.0")
    else:
        print("Error! - Value of linear velocity must be between 2.0 and 6.0")

if __name__ == '__main__':
    main()

