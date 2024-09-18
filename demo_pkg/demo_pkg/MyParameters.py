#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from rcl_interfaces.msg import ParameterDescriptor, SetParametersResult
from rclpy.parameter import Parameter

class ParamServer(Node):
    def __init__(self, node_name):
        super().__init__(node_name=node_name)
        #declarar parametros
        #se declara timer_period como flotante
        description = ParameterDescriptor(description='Timerxd')
        self.declare_parameter('timer_period',0.0, description)
        self.declare_parameters(
            namespace = '',
            parameters=[
                ('lin_vel', 0.1),
                ('ang_vel', 0.4),
                ('label_str', rclpy.Parameter.Type.STRING),
                ('param_int', rclpy.Parameter.Type.INTEGER),
                ('controller', [0.5, 0.7, 1000.0], ParameterDescriptor(description='Integral, Derivativo, Proporcional'))
            ]   
        )
        self._timer_Period = self.get_parameter('timer_period').get_parameter_value().double_value
        self.add_on_set_parameters_callback(self._on_parameter_change)
        self.get_logger().info("ParamServer inicializado")

    def _on_parameter_change(self, params : list[Parameter]):
        success = True
        for param in params:
            if param.name == 'timer_period':
                if param.value < 0:
                    success = False
                    self.get_logger().warning(f"el parametro '{param.name}' no puede ser negativo")
            else:
                self.get_logger().info(f"El parametro '{param.name}' no es monitoreado")
        return SetParametersResult(successful = success)
        

def main(args=None):
    rclpy.init(args=args)
    nodo = ParamServer('MyParams')
    rclpy.spin(nodo)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
