import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist

class MinimalSubscriber(Node):
    def __init__(self):
        super().__init__('jetbot_motors')
        self.subscription = self.create_subscription(
            Twist
        ,   'cmd_vel'
        ,   self.cmd_vel_cb
        ,   10
        )
    def cmd_vel_cb(self,msg):
        self.get_logger().info('I heard you !')


def main(args=None):
    rclpy.init(args=args)

    sb= MinimalSubscriber()
    
    rclpy.spin(sb)

    sb.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
