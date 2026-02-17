// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from interfaces:srv/SetProcessBool.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES__SRV__DETAIL__SET_PROCESS_BOOL__BUILDER_HPP_
#define INTERFACES__SRV__DETAIL__SET_PROCESS_BOOL__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "interfaces/srv/detail/set_process_bool__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace interfaces
{

namespace srv
{

namespace builder
{

class Init_SetProcessBool_Request_enable
{
public:
  Init_SetProcessBool_Request_enable()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::interfaces::srv::SetProcessBool_Request enable(::interfaces::srv::SetProcessBool_Request::_enable_type arg)
  {
    msg_.enable = std::move(arg);
    return std::move(msg_);
  }

private:
  ::interfaces::srv::SetProcessBool_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::interfaces::srv::SetProcessBool_Request>()
{
  return interfaces::srv::builder::Init_SetProcessBool_Request_enable();
}

}  // namespace interfaces


namespace interfaces
{

namespace srv
{

namespace builder
{

class Init_SetProcessBool_Response_message
{
public:
  explicit Init_SetProcessBool_Response_message(::interfaces::srv::SetProcessBool_Response & msg)
  : msg_(msg)
  {}
  ::interfaces::srv::SetProcessBool_Response message(::interfaces::srv::SetProcessBool_Response::_message_type arg)
  {
    msg_.message = std::move(arg);
    return std::move(msg_);
  }

private:
  ::interfaces::srv::SetProcessBool_Response msg_;
};

class Init_SetProcessBool_Response_success
{
public:
  Init_SetProcessBool_Response_success()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_SetProcessBool_Response_message success(::interfaces::srv::SetProcessBool_Response::_success_type arg)
  {
    msg_.success = std::move(arg);
    return Init_SetProcessBool_Response_message(msg_);
  }

private:
  ::interfaces::srv::SetProcessBool_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::interfaces::srv::SetProcessBool_Response>()
{
  return interfaces::srv::builder::Init_SetProcessBool_Response_success();
}

}  // namespace interfaces

#endif  // INTERFACES__SRV__DETAIL__SET_PROCESS_BOOL__BUILDER_HPP_
