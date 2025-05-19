cmake_minimum_required(VERSION 3.5)
project(screw_robot_control)

# Default to C99
if(NOT CMAKE_C_STANDARD)
  set(CMAKE_C_STANDARD 99)
endif()

# Default to C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 17)
endif()

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(Eigen3 REQUIRED)
find_package(robot_msgs REQUIRED)
find_package(rclcpp_action REQUIRED)

include_directories(
  include
  include/screw_robot_control
  ${EIGEN3_INCLUDE_DIRS}
)
# 定义 SERVO_MOTOR 库
add_library(SERVO_MOTOR SHARED
  src/servo_motor_function.cpp
)
ament_target_dependencies(SERVO_MOTOR
  rclcpp
  robot_msgs
)
target_link_libraries(SERVO_MOTOR
  ${CMAKE_SOURCE_DIR}/lib/libdxl_x64_cpp.so
)
# 定义 SCREWING_TOOL 库
add_library(SCREWING_TOOL SHARED
  src/screwing_tool.cpp
)
ament_target_dependencies(SCREWING_TOOL
  rclcpp
  robot_msgs
)
target_link_libraries(SCREWING_TOOL
  ${CMAKE_SOURCE_DIR}/lib/libdxl_x64_cpp.so
  SERVO_MOTOR
)
# 定义 right_arm_control 可执行文件
add_executable(right_arm_control src/right_arm_control.cpp)
target_link_libraries(right_arm_control
  ${EIGEN3_LIBRARIES}
  SCREWING_TOOL
  ${CMAKE_SOURCE_DIR}/lib/libjakaAPI.so
)
ament_target_dependencies(right_arm_control 
                          rclcpp 
                          std_msgs 
                          geometry_msgs 
                          robot_msgs
                          rclcpp_action
                          Eigen3
                          )

add_executable(right_arm_control_tcp src/right_arm_control_tcp.cpp)
target_link_libraries(right_arm_control_tcp
  ${EIGEN3_LIBRARIES}
  SCREWING_TOOL
  ${CMAKE_SOURCE_DIR}/lib/libjakaAPI.so
)
ament_target_dependencies(right_arm_control_tcp 
                          rclcpp 
                          std_msgs 
                          geometry_msgs 
                          robot_msgs
                          rclcpp_action
                          Eigen3
                          )

# 定义 task_control_screw 可执行文件
add_executable(task_control_screw src/task_control_screw.cpp)
ament_target_dependencies(task_control_screw
  rclcpp
  std_msgs 
  robot_msgs
  rclcpp_action
  Eigen3
)
target_link_libraries(task_control_screw
  SCREWING_TOOL
  ${CMAKE_SOURCE_DIR}/lib/libdxl_x64_cpp.so
)

# 安装库
install(TARGETS SERVO_MOTOR SCREWING_TOOL
  ARCHIVE DESTINATION lib
  LIBRARY DESTINATION lib
  RUNTIME DESTINATION bin
)

# 安装可执行文件
install(TARGETS 
  right_arm_control
  task_control_screw
  right_arm_control_tcp
  DESTINATION lib/${PROJECT_NAME}
)

# 安装外部库
install(FILES
  ${CMAKE_SOURCE_DIR}/lib/libjakaAPI.so
  ${CMAKE_SOURCE_DIR}/lib/libdxl_x64_cpp.so
  DESTINATION lib
)

# 安装头文件
install(DIRECTORY include/
  DESTINATION include
)

install(DIRECTORY launch
  DESTINATION share/${PROJECT_NAME}
)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  # the following line skips the linter which checks for copyrights
  # uncomment the line when a copyright and license is not present in all source files
  #set(ament_cmake_copyright_FOUND TRUE)
  # the following line skips cpplint (only works in a git repo)
  # uncomment the line when this package is not in a git repo
  #set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()
