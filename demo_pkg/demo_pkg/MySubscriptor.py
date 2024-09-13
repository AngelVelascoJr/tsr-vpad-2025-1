#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from my_interfase.msg import Myposition, TargetPosition

class MySubNode(Node) :
    def __init__(self, node_name):
        super().__init__(node_name=node_name)
        self._topic_sub = self.create_subscription(Myposition, '/mensaje', self._subs_callback, 10)
        self._target_pos_sub = self.create_subscription(TargetPosition, '/pos_objetivo', self._pos_subs_callback, 10)
        #self.get_logger().info(" Nodo Creado: " + self.get_name())

    def _subs_callback(self, message:Myposition):
        #self.get_logger().info(f"Recibi: {message.data}")
        self.get_logger().info(f"Recibi: [{message.etiqueta}]: PosX = {message.pos_x}, PosY = {message.pos_y}, PosZ = {message.pos_z}")

    def _pos_subs_callback(self, message:TargetPosition):
        self.get_logger().info(f"On [{message.header.stamp.sec}.{message.header.stamp.nanosec}]: destino = [{message.destino}] To [{message.target_point.x}, {message.target_point.y}, {message.target_point.z}]")

def main(args=None): 
    rclpy.init(args=args)
    myNodoSuscriptor = MySubNode(node_name='PedroEscuchador')
    rclpy.spin(myNodoSuscriptor)
    rclpy.shutdown()

if __name__ == '__main__':
    main()