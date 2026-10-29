
import math

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose


class PentagonDrawer(Node):

    def __init__(self):
        super().__init__('pentagon_drawer')

        self.publisher = self.create_publisher(
            Twist, '/turtle1/cmd_vel', 10
        )

        self.pose_subscriber = self.create_subscription(
            Pose, '/turtle1/pose', self.pose_callback, 10
        )

        self.pose = None
        self.side_length = 2.0
        self.turn_angle = math.radians(72.0)
        self.side_count = 0
        self.state = 'wait'
        self.start_x = 0.0
        self.start_y = 0.0
        self.start_theta = 0.0

        self.timer = self.create_timer(0.05, self.control)

    def pose_callback(self, msg):
        self.pose = msg

    def control(self):
        if self.pose is None:
            return

        cmd = Twist()


        if self.state == 'wait':
            self.start_x = self.pose.x
            self.start_y = self.pose.y
            self.state = 'forward'
            self.get_logger().info('Starting pentagon drawing')

        elif self.state == 'forward':
            distance = math.hypot(
                self.pose.x - self.start_x,
                self.pose.y - self.start_y
            )

            if distance >= self.side_length:
                self.publisher.publish(Twist())
                self.side_count += 1

                if self.side_count >= 5:
                    self.state = 'done'
                    self.get_logger().info('Pentagon completed!')
                    return

                self.start_theta = self.pose.theta
                self.state = 'turn'
            else:
                cmd.linear.x = 1.0

        elif self.state == 'turn':
            angle_turned = self.pose.theta - self.start_theta

            if angle_turned < 0:
                angle_turned += 2.0 * math.pi

            if angle_turned >= self.turn_angle:
                self.publisher.publish(Twist())
                self.start_x = self.pose.x
                self.start_y = self.pose.y
                self.state = 'forward'
            else:
                cmd.angular.z = 1.0

        elif self.state == 'done':
            self.publisher.publish(Twist())
            self.timer.cancel()
            return

        self.publisher.publish(cmd)


def main(args=None):
    rclpy.init(args=args)
    node = PentagonDrawer()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.publisher.publish(Twist())
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()

