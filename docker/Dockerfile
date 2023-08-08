FROM ros2:humble
# Update
RUN apt update
RUN apt-get install -y software-properties-common apt-utils -y
RUN apt-get update && \
    apt-get install -y librealsense2-dkms librealsense2-utils librealsense2-dev 


RUN git clone https://github.com/appliedAI-Initiative/orb_slam_2_ros.git
# Install ROS dependencies
RUN rosdep update \
&& rosdep install --from-paths src --ignore-src -r -y --skip-keys=librealsense2
