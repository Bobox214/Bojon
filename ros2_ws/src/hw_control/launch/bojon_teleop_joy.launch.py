import os.path
import launch
import launch.actions
import launch.substitutions
import launch_ros.actions

from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    joy_config = os.path.join( get_package_share_directory('hw_control') , 'bojon.joy.yaml' )
    return launch.LaunchDescription([
        launch_ros.actions.Node(
            package='joy',node_executable='joy_node',name='joy_node'
        ,   parameters=[{'dev':'/dev/input/js0','deadzone':0.2,'autorepeat_rate':20.0}]
        )
    ,   launch_ros.actions.Node(
            package='teleop_twist_joy',node_executable='teleop_node',name='teleop_twist_joy_node'
        ,   parameters=[joy_config]
        )
    ,   launch_ros.actions.Node(
            package='hw_control',node_executable='motors',name='bojon_motors'
        )
    ])
