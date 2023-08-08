FROM osrf/ros:humble-desktop-jammy
# Update


RUN apt-get update
RUN apt-get install -y software-properties-common apt-utils -y



# Set working directory
WORKDIR /home/ros/src
RUN git clone https://github.com/arshadlab/orb_slam_3_ros.git
WORKDIR /home/ros
# Install ROS dependencies
RUN rosdep update \
&& rosdep install --from-paths src --ignore-src -r -y
WORKDIR /home/ros/src/orb_slam_3_ros/ORB_SLAM3
RUN ./install_dep.sh
RUN ./build.sh
WORKDIR /home/ros
RUN bash -c "./src/orb_slam_3_ros/docker/build_ros.sh"
