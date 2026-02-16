import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
from message_filters import Subscriber, ApproximateTimeSynchronizer
import math

class MinimalSubscriber(Node):
    def __init__(self):
        super().__init__('minimal_subscriber')
        
        self.subscriber_time = Subscriber(self, Float32, 'time')
        self.subscriber_signal = Subscriber(self, Float32, 'signal')
        
        # Add allow_headerless=True
        self.ats = ApproximateTimeSynchronizer(
            [self.subscriber_time, self.subscriber_signal], 
            queue_size=10,
            slop=0.1,
            allow_headerless=True  # Add this parameter
        )
        self.ats.registerCallback(self.listener_callback)
        
        self.publisher_signal = self.create_publisher(Float32, 'proc_signal', 10)
        self.buffer_time = []

    def listener_callback(self, msg_time, msg_signal):
        t = msg_time.data
        signal = msg_signal.data
        self.buffer_time.append(signal)
        self.get_logger().info('Buffer size: %d' % len(self.buffer_time))
        
        if(len(self.buffer_time) > 30):
            shifted_signal = self.buffer_time.pop(0)
            processed_signal = (shifted_signal/2)+4
            msg = Float32()
            msg.data = processed_signal
            self.publisher_signal.publish(msg)
            self.get_logger().info('[PROC] Published processed signal: "%f"' % msg.data)
        else:
            msg = Float32()
            msg.data = 0.0
            self.publisher_signal.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    minimal_subscriber = MinimalSubscriber()
    rclpy.spin(minimal_subscriber)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()