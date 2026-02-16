import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import math

class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher_signal = self.create_publisher(Float32, 'signal', 10)
        self.publisher_time = self.create_publisher(Float32, 'time', 10)
        timer_period = 0.1  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0.0

    def timer_callback(self):
        msg2 = Float32()
        msg2.data = self.i
        self.publisher_time.publish(msg2)

        msg = Float32()
        msg.data = math.sin(self.i)
        self.i += 0.1
        self.publisher_signal.publish(msg)
        self.get_logger().info('[ORI] Sin at t: "%f" is "%f"' % (msg2.data, msg.data))


def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_publisher)

    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()