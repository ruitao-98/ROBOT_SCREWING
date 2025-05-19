#include "screw_robot_control/jaka/servo_motor_function.hpp"
#include "robot_msgs/msg/current_pub.hpp"
#include "robot_msgs/msg/width_pub.hpp"
#include <iostream>
#include <fstream>
#include <string>
#include <rclcpp/rclcpp.hpp>
#include <iomanip>

class endeffector: public motors
{
private:
	std::string delta_width = "/home/yanji/robot_screwing/src/screw_robot_control/data/delta_width.txt";
	std::string delta_circle = "/home/yanji/robot_screwing/src/screw_robot_control/data/delta_circle.txt";
	std::string standard_path = "/home/yanji/robot_screwing/src/screw_robot_control/data/standard.txt";

public:
	endeffector();
	void width_reduce(int distance, rclcpp::Publisher<robot_msgs::msg::CurrentPub>::SharedPtr pub,
									robot_msgs::msg::CurrentPub &msg);
	void width_increase(int distance, rclcpp::Publisher<robot_msgs::msg::CurrentPub>::SharedPtr pub,
									robot_msgs::msg::CurrentPub &msg,
									rclcpp::Publisher<robot_msgs::msg::WidthPub>::SharedPtr pub1,
									robot_msgs::msg::WidthPub &msg1);

	int width_reduce_full_for_handover(rclcpp::Publisher<robot_msgs::msg::CurrentPub>::SharedPtr pub,
										robot_msgs::msg::CurrentPub &msg,
										rclcpp::Publisher<robot_msgs::msg::WidthPub>::SharedPtr pub1,
										robot_msgs::msg::WidthPub &msg1); 
    int width_reduce_or_increase_full(int judge); 
    int width_recovery();
    /**
	* @brief +1 reduce -1 increase
    * @return void
	*/

	int screwing_s1(int speed, float circle, rclcpp::Publisher<robot_msgs::msg::CurrentPub>::SharedPtr pub,
		robot_msgs::msg::CurrentPub &msg);
	int screwing_s2(int speed, rclcpp::Publisher<robot_msgs::msg::CurrentPub>::SharedPtr pub,
		robot_msgs::msg::CurrentPub &msg); 
	int screwing_s3(int speed,int yuzhi);


	//
	void unscrewing_s1(int speed_1, int speed_2);
	void unscrewing_sx(int speed);
	void unscrewing_final(int speed, float circle);

	float average_function(int *data, int length);

	void rotate_to(float angle);

	int unscrew_to_zero(int speed);

	void screw_to_zero();

	int measure_angle(int standard);



};