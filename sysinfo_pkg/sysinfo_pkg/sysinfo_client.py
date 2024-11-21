#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from my_interfase.srv import SysInfo

class SysinfoClient(Node):
    def __init__(self, node_name: str):
        super().__init__(node_name)
        self.__sysinfo_client = self.create_client(SysInfo, "/sysinfo_srv")
        while not self.__sysinfo_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info("servicio no disponible, esperando por el servicio")
        self.get_logger().info(f"{node_name} service client inicializado")

    def call_server(self, cmd:str):
        peticion = SysInfo.Request()
        peticion.modo = cmd
        self.get_logger().info("xd")
        respuesta:SysInfo.Response = self.__sysinfo_client.call(peticion)
        self.get_logger().info("xdzss")
        if respuesta.success:
            self.get_logger().info(f"El proceso fue exitoso: {respuesta.string_status_message}")
            self.get_logger().info(respuesta.sysinfo_msg)
        else:
            self.get_logger().info(f'El proceso no fue exitoso: {respuesta.string_status_message}')


def main(args = None):
    rclpy.init(args=args)
    srv_client_node = SysinfoClient("Service_client")
    srv_client_node.call_server(cmd="full")
    srv_client_node.call_server(cmd="snapshot")
    srv_client_node.call_server("partial")
    rclpy.shutdown()

if __name__ == "__main__":
    main