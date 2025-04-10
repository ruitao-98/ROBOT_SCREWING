cmake_minimum_required(VERSION 3.5)
project(robot_msgs)

# Default to C99
if(NOT CMAKE_C_STANDARD)
  set(CMAKE_C_STANDARD 99)
endif()

# Default to C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rosidl_default_generators REQUIRED)
find_package(rclpy REQUIRED)  # 如果需要 Python 支持
find_package(std_msgs REQUIRED)  # 确保 std_msgs 在这里被找到

rosidl_generate_interfaces(${PROJECT_NAME}
  "msg/FtPub.msg"
  "msg/RobotStatus.msg"
  "msg/ControlCommand.msg"
  "msg/RefStatus.msg"
  "srv/StartPose.srv"
  DEPENDENCIES std_msgs
  # "srv/MoveRobot.srv"
  # DEPENDENCIES geometry_msgs
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
