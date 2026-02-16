import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import math

class MinimalSubscriber(Node):
    def __init__(self):
        super().__init__('minimal_subscriber')
        
        # Suscriptor para el el topico '/time'
        self.subscription_time = self.create_subscription(
            Float32,
            'time',
            self.time_callback,
            10)
        
        # Suscriptor para el topico '/signal'
        self.subscription_signal = self.create_subscription(
            Float32,
            'signal',
            self.signal_callback,
            10)
        
        # Publisher para el topico '/proc_signal'
        self.publisher_signal = self.create_publisher(Float32, 'proc_signal', 10)
        self.buffer_time = []
        
        # Como se llama el suscriptor 2 veces (una por time y otra por signal)
        # es necesario hacer un pequeno buffer para estar seguro de que si llegaron
        # ambos datos
        self.latest_time = None
        self.latest_signal = None

    # En caso de que llegue el topico /time
    def time_callback(self, msg):
        self.latest_time = msg.data
        self.process_if_ready()
    
    # En caso de que llegue el topico /signal
    def signal_callback(self, msg):
        self.latest_signal = msg.data
        self.process_if_ready()
    
    def process_if_ready(self):
        # Revisar si existen ambos datos
        if self.latest_time is not None and self.latest_signal is not None:
            # Anade los valores a un buffer, este nos va a permitir el time shift
            self.buffer_time.append(self.latest_signal)
            
            # Si el buffer tiene mas de 30 datos, poppea el ultimo
            # esto genera un time shift de 30*0.05 = 1.5 segundos
            if len(self.buffer_time) > 30:
                shifted_signal = self.buffer_time.pop(0)
                # Divide la amplitud a la mitad y lo offsetea en 12 hacia arriba
                processed_signal = (shifted_signal/2) + 12
            else:
                # Si no han llegado el dato completo, mandamos el anterior
                processed_signal = (self.latest_signal/2) + 12
            
            msg = Float32()
            # Wrappeamos la nueva senal y la publicamos
            msg.data = processed_signal
            self.publisher_signal.publish(msg)
            self.get_logger().info('[PROC] Published: %f' % msg.data)

def main(args=None):
    rclpy.init(args=args)
    minimal_subscriber = MinimalSubscriber()
    rclpy.spin(minimal_subscriber)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()