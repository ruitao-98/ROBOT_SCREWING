// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from robot_msgs:action/Screw.idl
// generated code does not contain a copyright notice

#ifndef ROBOT_MSGS__ACTION__DETAIL__SCREW__BUILDER_HPP_
#define ROBOT_MSGS__ACTION__DETAIL__SCREW__BUILDER_HPP_

#include "robot_msgs/action/detail/screw__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace robot_msgs
{

namespace action
{

namespace builder
{

class Init_Screw_Goal_num
{
public:
  Init_Screw_Goal_num()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::robot_msgs::action::Screw_Goal num(::robot_msgs::action::Screw_Goal::_num_type arg)
  {
    msg_.num = std::move(arg);
    return std::move(msg_);
  }

private:
  ::robot_msgs::action::Screw_Goal msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::robot_msgs::action::Screw_Goal>()
{
  return robot_msgs::action::builder::Init_Screw_Goal_num();
}

}  // namespace robot_msgs


namespace robot_msgs
{

namespace action
{

namespace builder
{

class Init_Screw_Result_result
{
public:
  Init_Screw_Result_result()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::robot_msgs::action::Screw_Result result(::robot_msgs::action::Screw_Result::_result_type arg)
  {
    msg_.result = std::move(arg);
    return std::move(msg_);
  }

private:
  ::robot_msgs::action::Screw_Result msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::robot_msgs::action::Screw_Result>()
{
  return robot_msgs::action::builder::Init_Screw_Result_result();
}

}  // namespace robot_msgs


namespace robot_msgs
{

namespace action
{

namespace builder
{

class Init_Screw_Feedback_screw_status
{
public:
  Init_Screw_Feedback_screw_status()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::robot_msgs::action::Screw_Feedback screw_status(::robot_msgs::action::Screw_Feedback::_screw_status_type arg)
  {
    msg_.screw_status = std::move(arg);
    return std::move(msg_);
  }

private:
  ::robot_msgs::action::Screw_Feedback msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::robot_msgs::action::Screw_Feedback>()
{
  return robot_msgs::action::builder::Init_Screw_Feedback_screw_status();
}

}  // namespace robot_msgs


namespace robot_msgs
{

namespace action
{

namespace builder
{

class Init_Screw_SendGoal_Request_goal
{
public:
  explicit Init_Screw_SendGoal_Request_goal(::robot_msgs::action::Screw_SendGoal_Request & msg)
  : msg_(msg)
  {}
  ::robot_msgs::action::Screw_SendGoal_Request goal(::robot_msgs::action::Screw_SendGoal_Request::_goal_type arg)
  {
    msg_.goal = std::move(arg);
    return std::move(msg_);
  }

private:
  ::robot_msgs::action::Screw_SendGoal_Request msg_;
};

class Init_Screw_SendGoal_Request_goal_id
{
public:
  Init_Screw_SendGoal_Request_goal_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Screw_SendGoal_Request_goal goal_id(::robot_msgs::action::Screw_SendGoal_Request::_goal_id_type arg)
  {
    msg_.goal_id = std::move(arg);
    return Init_Screw_SendGoal_Request_goal(msg_);
  }

private:
  ::robot_msgs::action::Screw_SendGoal_Request msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::robot_msgs::action::Screw_SendGoal_Request>()
{
  return robot_msgs::action::builder::Init_Screw_SendGoal_Request_goal_id();
}

}  // namespace robot_msgs


namespace robot_msgs
{

namespace action
{

namespace builder
{

class Init_Screw_SendGoal_Response_stamp
{
public:
  explicit Init_Screw_SendGoal_Response_stamp(::robot_msgs::action::Screw_SendGoal_Response & msg)
  : msg_(msg)
  {}
  ::robot_msgs::action::Screw_SendGoal_Response stamp(::robot_msgs::action::Screw_SendGoal_Response::_stamp_type arg)
  {
    msg_.stamp = std::move(arg);
    return std::move(msg_);
  }

private:
  ::robot_msgs::action::Screw_SendGoal_Response msg_;
};

class Init_Screw_SendGoal_Response_accepted
{
public:
  Init_Screw_SendGoal_Response_accepted()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Screw_SendGoal_Response_stamp accepted(::robot_msgs::action::Screw_SendGoal_Response::_accepted_type arg)
  {
    msg_.accepted = std::move(arg);
    return Init_Screw_SendGoal_Response_stamp(msg_);
  }

private:
  ::robot_msgs::action::Screw_SendGoal_Response msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::robot_msgs::action::Screw_SendGoal_Response>()
{
  return robot_msgs::action::builder::Init_Screw_SendGoal_Response_accepted();
}

}  // namespace robot_msgs


namespace robot_msgs
{

namespace action
{

namespace builder
{

class Init_Screw_GetResult_Request_goal_id
{
public:
  Init_Screw_GetResult_Request_goal_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::robot_msgs::action::Screw_GetResult_Request goal_id(::robot_msgs::action::Screw_GetResult_Request::_goal_id_type arg)
  {
    msg_.goal_id = std::move(arg);
    return std::move(msg_);
  }

private:
  ::robot_msgs::action::Screw_GetResult_Request msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::robot_msgs::action::Screw_GetResult_Request>()
{
  return robot_msgs::action::builder::Init_Screw_GetResult_Request_goal_id();
}

}  // namespace robot_msgs


namespace robot_msgs
{

namespace action
{

namespace builder
{

class Init_Screw_GetResult_Response_result
{
public:
  explicit Init_Screw_GetResult_Response_result(::robot_msgs::action::Screw_GetResult_Response & msg)
  : msg_(msg)
  {}
  ::robot_msgs::action::Screw_GetResult_Response result(::robot_msgs::action::Screw_GetResult_Response::_result_type arg)
  {
    msg_.result = std::move(arg);
    return std::move(msg_);
  }

private:
  ::robot_msgs::action::Screw_GetResult_Response msg_;
};

class Init_Screw_GetResult_Response_status
{
public:
  Init_Screw_GetResult_Response_status()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Screw_GetResult_Response_result status(::robot_msgs::action::Screw_GetResult_Response::_status_type arg)
  {
    msg_.status = std::move(arg);
    return Init_Screw_GetResult_Response_result(msg_);
  }

private:
  ::robot_msgs::action::Screw_GetResult_Response msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::robot_msgs::action::Screw_GetResult_Response>()
{
  return robot_msgs::action::builder::Init_Screw_GetResult_Response_status();
}

}  // namespace robot_msgs


namespace robot_msgs
{

namespace action
{

namespace builder
{

class Init_Screw_FeedbackMessage_feedback
{
public:
  explicit Init_Screw_FeedbackMessage_feedback(::robot_msgs::action::Screw_FeedbackMessage & msg)
  : msg_(msg)
  {}
  ::robot_msgs::action::Screw_FeedbackMessage feedback(::robot_msgs::action::Screw_FeedbackMessage::_feedback_type arg)
  {
    msg_.feedback = std::move(arg);
    return std::move(msg_);
  }

private:
  ::robot_msgs::action::Screw_FeedbackMessage msg_;
};

class Init_Screw_FeedbackMessage_goal_id
{
public:
  Init_Screw_FeedbackMessage_goal_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Screw_FeedbackMessage_feedback goal_id(::robot_msgs::action::Screw_FeedbackMessage::_goal_id_type arg)
  {
    msg_.goal_id = std::move(arg);
    return Init_Screw_FeedbackMessage_feedback(msg_);
  }

private:
  ::robot_msgs::action::Screw_FeedbackMessage msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::robot_msgs::action::Screw_FeedbackMessage>()
{
  return robot_msgs::action::builder::Init_Screw_FeedbackMessage_goal_id();
}

}  // namespace robot_msgs

#endif  // ROBOT_MSGS__ACTION__DETAIL__SCREW__BUILDER_HPP_
