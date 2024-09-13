#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from my_interfase.msg import Myposition, TargetPosition


class MyTestNode(Node) :
    def __init__(self, node_name:str):
        super().__init__("my_test_node")
        self._topic_pub = self.create_publisher(Myposition, '/mensaje', 10)
        self.target_pos_pub = self.create_publisher(TargetPosition, "/pos_objetivo", 10)
        self.timer = self.create_timer(3.0,  self._timer_callback)
        self.target_timer = self.create_timer(1.0, self._pub_trg_pos_clbk)
        self._count = 0.0
        self.get_logger().info(" Nodo Creado: " + self.get_name())

    def _timer_callback(self):
        self._count += 1.0
        mensaje = Myposition()
        mensaje.pos_x = self._count
        mensaje.pos_y = self._count / 2.0
        mensaje.pos_z = self._count / 3.0
        mensaje.etiqueta = f"{self._count} repeticiones cada 2 segundos"
        self._topic_pub.publish(mensaje)

    def _pub_trg_pos_clbk(self):
        target_msg = TargetPosition()
        # Header del mensaje
        target_msg.header.frame_id = 'origin_cs'
        target_msg.header.stamp = self.get_clock().now().to_msg()
        # Etiqueta del punto destino
        target_msg.destino = 'Punto destino'
        # Variables de la posicion destino
        target_msg.target_point.x = self._count
        target_msg.target_point.y = self._count / 2
        target_msg.target_point.z = self._count / 3
        self.target_pos_pub.publish(target_msg)

def main(args=None): 
    rclpy.init(args=args)
    mynodo = MyTestNode(node_name='Pedro')
    rclpy.spin(mynodo)
    rclpy.shutdown()

if __name__ == '__main__':
    main()