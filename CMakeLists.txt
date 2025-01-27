cmake_minimum_required(VERSION 3.5)
project(orb_slam3_ros)

IF(NOT CMAKE_BUILD_TYPE)
  SET(CMAKE_BUILD_TYPE Release)
endif()


# Default to C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

set(ORB_SLAM3_DIR ${CMAKE_CURRENT_SOURCE_DIR}/ORB_SLAM3)
list(APPEND CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} "${CMAKE_CURRENT_SOURCE_DIR}/CMakeModules/")

find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)
find_package(sensor_msgs REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(cv_bridge REQUIRED)
find_package(message_filters REQUIRED)
find_package(image_common REQUIRED)
find_package(image_transport REQUIRED)
find_package(tf2_geometry_msgs REQUIRED)
find_package(tf2_ros REQUIRED)
find_package(rosidl_default_generators REQUIRED)
find_package(Pangolin REQUIRED )
find_package(ORB_SLAM3 REQUIRED )
find_package(Eigen3 3.1.0 REQUIRED)


set(dependencies
  rclcpp
  std_msgs
  sensor_msgs
  geometry_msgs
  cv_bridge
  image_common
  image_transport
  tf2_geometry_msgs
  tf2_ros
  ORB_SLAM3
)

find_package(OpenCV 4.0 QUIET)
if(NOT OpenCV_FOUND)
   find_package(OpenCV 3.0 QUIET)
   if(NOT OpenCV_FOUND)
      find_package(OpenCV 2.4.3 QUIET)
      if(NOT OpenCV_FOUND)
         message(FATAL_ERROR "OpenCV > 2.4.3 not found.")
     endif()
   endif()
endif()

find_package(Eigen3 3.1.0 REQUIRED)

rosidl_generate_interfaces(${PROJECT_NAME}
  "srv/SaveMap.srv"
  DEPENDENCIES builtin_interfaces std_msgs
)

include_directories(
  ${PROJECT_SOURCE_DIR}/ros/include
  ${EIGEN3_INCLUDE_DIR}
  include
)
#Mono
add_executable(${PROJECT_NAME}_mono
  ros/src/MonoNode.cc
  ros/src/Node.cc
)
ament_target_dependencies(${PROJECT_NAME}_mono
  ${dependencies}
)

target_link_libraries(${PROJECT_NAME}_mono
  ${OpenCV_LIBS}
  ${EIGEN3_LIBS}
  ${Pangolin_LIBRARIES}
  ${ORB_SLAM3_DIR}/Thirdparty/DBoW2/lib/libDBoW2.so
  ${ORB_SLAM3_DIR}/Thirdparty/g2o/lib/libg2o.so
  -lboost_serialization
  -lcrypto
)

rosidl_get_typesupport_target(cpp_typesupport_target ${PROJECT_NAME} "rosidl_typesupport_cpp")

target_link_libraries(${PROJECT_NAME}_mono ${cpp_typesupport_target})

#Stereo
add_executable (${PROJECT_NAME}_stereo
  ros/src/StereoNode.cc
  ros/src/Node.cc
)
ament_target_dependencies(${PROJECT_NAME}_stereo
  ${dependencies}
)
target_link_libraries(${PROJECT_NAME}_stereo
${OpenCV_LIBS}
${EIGEN3_LIBS}
${Pangolin_LIBRARIES}
${ORB_SLAM3_DIR}/Thirdparty/DBoW2/lib/libDBoW2.so
${ORB_SLAM3_DIR}/Thirdparty/g2o/lib/libg2o.so
-lboost_serialization
-lcrypto
)

target_link_libraries(${PROJECT_NAME}_stereo ${cpp_typesupport_target})

#RGBD
add_executable(${PROJECT_NAME}_rgbd
  ros/src/RGBDNode.cc
  ros/src/Node.cc
)
ament_target_dependencies(${PROJECT_NAME}_rgbd
  ${dependencies}
)
target_link_libraries(${PROJECT_NAME}_rgbd
${OpenCV_LIBS}
${EIGEN3_LIBS}
${Pangolin_LIBRARIES}
${ORB_SLAM3_DIR}/Thirdparty/DBoW2/lib/libDBoW2.so
${ORB_SLAM3_DIR}/Thirdparty/g2o/lib/libg2o.so
-lboost_serialization
-lcrypto
)

target_link_libraries(${PROJECT_NAME}_rgbd ${cpp_typesupport_target})


install(TARGETS ${PROJECT_NAME}_mono ${PROJECT_NAME}_stereo ${PROJECT_NAME}_rgbd
  RUNTIME DESTINATION lib/${PROJECT_NAME}
)

install(DIRECTORY ros/launch/
  DESTINATION share/${PROJECT_NAME}/ros/launch
)

install(DIRECTORY ros/config/
  DESTINATION share/${PROJECT_NAME}/ros/config
)

install(DIRECTORY ORB_SLAM3/Vocabulary/
  DESTINATION share/${PROJECT_NAME}/ORB_SLAM3/Vocabulary
)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  ament_lint_auto_find_test_dependencies()
endif()

ament_export_include_directories(include)
ament_export_dependencies(
  ${dependencies}
  rosidl_default_runtime
)

ament_environment_hooks("${CMAKE_CURRENT_SOURCE_DIR}/env-hooks/env.dsv.in")

ament_package()
