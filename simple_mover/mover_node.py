import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time

class MoverNode(Node):
    def __init__(self):
        super().__init__('mover_node')

        self.publisher_ = self.create_publisher(Twist, 'cmd_vel', 10)

        self.timer = self.create_timer(0.1, self.timer_callback)
        self.start_time = time.time()

    def timer_callback(self):
        msg = Twist()
        elapsed_time = time.time() - self.start_time

        # Maju 3 meter
        if elapsed_time < 6.0:
            msg.linear.x = 0.5
            msg.angular.z = 0.0
            self.get_logger().info('Maju 1...')

        # Rotasi 90 derajat
        elif elapsed_time < 9.14:
            msg.linear.x = 0.0
            msg.angular.z = 0.5
            self.get_logger().info('Rotasi 1...')

        # Maju 2 meter
        elif elapsed_time < 13.14:
            msg.linear.x = 0.5
            msg.angular.z = 0.0
            self.get_logger().info('Maju 2...')

        # Rotasi 90 derajat
        elif elapsed_time < 16.28:
            msg.linear.x = 0.0
            msg.angular.z = 0.5
            self.get_logger().info('Rotasi 2...')

        # Maju 3 meter
        elif elapsed_time < 22.28:
            msg.linear.x = 0.5
            msg.angular.z = 0.0
            self.get_logger().info('Maju 3...')

        # Rotasi 90 derajat
        elif elapsed_time < 25.42:
            msg.linear.x = 0.0
            msg.angular.z = 0.5
            self.get_logger().info('Rotasi 3...')

        # Maju 2 meter
        elif elapsed_time < 29.42:
            msg.linear.x = 0.5
            msg.angular.z = 0.0
            self.get_logger().info('Maju 4...')

        # Rotasi 90 derajat
        elif elapsed_time < 32.56:
            msg.linear.x = 0.0
            msg.angular.z = 0.5
            self.get_logger().info('Rotasi 4...')

        # Berhenti
        else:
            msg.linear.x = 0.0
            msg.angular.z = 0.0
            self.get_logger().info('Berhenti.')

            self.publisher_.publish(msg)
            self.timer.cancel()
            rclpy.shutdown()
            return

        self.publisher_.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = MoverNode()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        if rclpy.ok():
            node.destroy_node()
            rclpy.shutdown()


if __name__ == '__main__':
    main()
