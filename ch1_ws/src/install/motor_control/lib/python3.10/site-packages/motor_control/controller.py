import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
from rcl_interfaces.msg import SetParametersResult
from interfaces.srv import SetProcessBool

#Class Definition
class Controller(Node):
    def __init__(self):
        super().__init__('controller')

        self.declare_parameter('Kp', 0.0)
        self.declare_parameter('Kd', 0.0)
        self.declare_parameter('Ki', 0.0)

        self.kp = self.get_parameter('Kp').value
        self.kd = self.get_parameter('Kd').value
        self.ki = self.get_parameter('Ki').value

        self.target = 0.0
        self.error = 0.0
        self.previous_error = 0.0

        self.integral = 0.0
        self.sample_time = 0.02

        self.power = 0.0
        self.on = True

        self.motor_output_sub = self.create_subscription(Float32, 'motor_speed_y', self.calculate_error_callback,10)
        self.target_sub = self.create_subscription(Float32, 'set_point', self.update_target_callback,10)
        self.motor_speed_pub = self.create_publisher(Float32, 'motor_input_u', 10)

        self.add_on_set_parameters_callback(self.parameters_callback)

        self.enable_controller = self.create_service(SetProcessBool, 'enable_controller', self.enable_controller_callback)

        self.get_logger().info('Started controller')

    def update_target_callback(self,msg):
        self.target = msg.data

    def calculate_error_callback(self, msg):
        self.error = self.target - msg.data
        self.publish_control_signal()

    def publish_control_signal(self):
        self.integral += self.error * self.sample_time
        self.power = self.kp * self.error + self.kd * (self.error - self.previous_error) / self.sample_time + self.ki * self.integral
        self.previous_error = self.error

        motor_msg = Float32()

        if (self.on):
            motor_msg.data = self.power
        else:
            motor_msg.data = 0.0

        self.motor_speed_pub.publish(motor_msg)
        self.get_logger().info(f"Target: {self.target:.2f}, Error: {self.error:.2f}, Power: {self.power:.2f}, Kp: {self.kp:.2f}, Kd: {self.kd:.2f}, Ki: {self.ki:.2f}")

    def parameters_callback(self, params):
        for param in params:
            if param.name == 'Kp':
                self.kp = param.value
            elif param.name == 'Kd':
                self.kd = param.value
            elif param.name == 'Ki':
                self.ki = param.value

        return SetParametersResult(successful=True)

    def enable_controller_callback(self, request, response):
        if self.on and request.enable:
            response.success = False
            response.message = "Controller is already enabled."
        elif not self.on and not request.enable:
            response.success = False
            response.message = "Controller is already disabled."
        else:
            self.on = request.enable
            response.success = True
            response.message = f"Controller {'enabled' if self.on else 'disabled'} successfully."
        
        return response

def main(args=None):
    rclpy.init(args=args)

    node = Controller()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()