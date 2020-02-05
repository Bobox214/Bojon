import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist
from jetbot            import Robot

JETBOT_WHEEL_SEPARATION = 0.116

class MotorsNode(Node):
    def __init__(self,robot):
        super().__init__('jetbot_motors')
        self.robot        = robot
        self.cmd_received = False
        self.subscription = self.create_subscription(
            Twist
        ,   'cmd_vel'
        ,   self.cmd_vel_cb
        ,   10
        )
        self.timer = self.create_timer(0.2,self.timer_cb)
        self.get_logger().info("Motor control initialized")
    def cmd_vel_cb(self,msg):
        self.cmd_received = True
        vX = msg.linear.x
        vW = msg.angular.z
        self.robot.right_motor.value = vX+vW/2
        self.robot.left_motor .value = vX-vW/2
    def timer_cb(self):
        if not self.cmd_received:
            self.robot.stop()
        self.cmd_received = False


def main(args=None):
    rclpy.init(args=args)

    robot = Robot()

    motorsNode = MotorsNode(robot)
    
    rclpy.spin(motorsNode)

    sb.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
