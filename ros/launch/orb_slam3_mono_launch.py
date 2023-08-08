import os
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():

    use_sim_time = LaunchConfiguration('use_sim_time')
    params_file = LaunchConfiguration('params_file')
    voc_file = LaunchConfiguration('voc_file')
    setting_file = LaunchConfiguration('setting_file')
 
    remappings = [
        ('/camera/rgb/image_raw', '/camera/color/image_raw'),
        ('/camera/depth_registered/image_raw', '/camera/depth/image_rect_raw'),
        ('/camera/camera_info', '/camera/color/camera_info'),
    ]

    return LaunchDescription([
        DeclareLaunchArgument(
            'use_sim_time',
            default_value='false',
            description='Use simulation (Gazebo) clock if true'),

        DeclareLaunchArgument(
            'params_file',
            default_value=os.path.join(
                get_package_share_directory("orb_slam3_ros"),
                'ros', 'config', 'params_gazebo_mono.yaml'),
            description='Full path to the ROS2 parameters file to use for all launched nodes'),

        DeclareLaunchArgument(
            'voc_file',
            default_value=os.path.join(
                get_package_share_directory("orb_slam3_ros"),
                'ros', 'config', 'ORBvoc.txt'),
            description='Full path to vocabulary file to use'),
        DeclareLaunchArgument(
            'setting_file',
            default_value=os.path.join(
                get_package_share_directory("orb_slam3_ros"),
                'ros', 'config', 'TUM1.yaml'),
            description='Full path to vocabulary file to use'),

        Node(
            parameters=[
                params_file,
                {"voc_file": voc_file,
                 "use_sim_time": use_sim_time,
                 "setting_file": setting_file},
            ],
            package='orb_slam3_ros',
            executable='orb_slam3_ros_mono',
            name='orb_slam2_mono',
            output='screen',
            remappings=remappings
        )
    ])
