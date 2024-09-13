cmake_minimum_required(VERSION 3.8)
project(my_interfase)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()
#en esta seccion se declaran las referencias necesarias
find_package(ament_cmake REQUIRED)
#tiene las herramienta para convertir el archivo descriptor 
#del mensaje a las diferentres interfaces del programa (c++, Python, DDS, etc)
find_package(geometry_msgs REQUIRED)
find_package(rosidl_default_generators REQUIRED)

rosidl_generate_interfaces(${PROJECT_NAME}
  "msg/Myposition.msg"
  "msg/TargetPosition.msg"
  DEPENDENCIES geometry_msgs
)

ament_export_dependencies(rosidl_default_runtime)

ament_package()
