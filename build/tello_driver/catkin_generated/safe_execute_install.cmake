execute_process(COMMAND "/home/amazing/Desktop/PROJECTS_AND_CODES/ROS/tello_ws/build/tello_driver/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/amazing/Desktop/PROJECTS_AND_CODES/ROS/tello_ws/build/tello_driver/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
