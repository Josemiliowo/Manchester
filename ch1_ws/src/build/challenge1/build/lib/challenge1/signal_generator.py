import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import math

class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')
        # Publisher del topico '/signal'
        self.publisher_signal = self.create_publisher(Float32, 'signal', 10)
        # Publisher del topico '/time'
        self.publisher_time = self.create_publisher(Float32, 'time', 10)

        # Publicamos cada 0.05 segundos
        timer_period = 0.05  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

        # Variable que lleva el tiempo elapsado
        self.i = 0.0

    def timer_callback(self):
        msg2 = Float32()
        msg2.data = self.i
        # Wrappeamos el tiempo en un msg y lo publicamos
        self.publisher_time.publish(msg2)

        msg = Float32()
        # Calculamos el seno de t y lo amplificamos por 20 para que se vea mejor
        msg.data = math.sin(self.i)*20

        # Aumentamos el dt que es 0.05
        self.i += 0.05

        # Wrappeamos la senal y la publicamos
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