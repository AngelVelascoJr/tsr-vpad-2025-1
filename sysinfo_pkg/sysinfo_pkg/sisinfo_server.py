#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from my_interfase.srv import SysInfo
from .arrg_utils.sysinfo import SysInfoTool

class SystemInfoService(Node):
    def __init__(self, node_name):
        super().__init__(node_name)
        self.__server = self.create_service(SysInfo, "/sysinfo_srv", self.__on_service_callback)
        self._sysinfotool = SysInfoTool()
        self.get_logger().info(f'{node_name} server inicializado.')

    def __on_service_callback(self, request:SysInfo.Request, response:SysInfo.Response):
        modo = request.modo
        response.success = True
        status_message = ""
        
        self.get_logger().info("Recibi una nueva peticion")
        if modo.lower() == "full":
            response.sysinfo_msg = str(self._sysinfotool.get_system_report())
            status_message = f"El modo seleccionado es correcto: {modo}."
        elif modo.lower() == "snapshot":
            response.sysinfo_msg = str(self._sysinfotool.get_system_snapshot())
            status_message = f"El modo seleccionado es correcto: {modo}."
        else:
            response.success = False
            response.sysinfo_msg = ""
            status_message = f"No reconosco el modo {modo}."

        response.string_status_message = status_message
        return response

def main(args=None):
    rclpy.init(args=args)
    srv_node = SystemInfoService("Service_Server")
    rclpy.spin(srv_node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()