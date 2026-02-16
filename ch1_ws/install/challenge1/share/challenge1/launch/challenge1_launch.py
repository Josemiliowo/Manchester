from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='challenge1',
            executable='signal_generator',
            name='signal_generator',
            output='screen',
            parameters=[
                # Add parameters here if needed
                # {'param_name': param_value}
            ],
            remappings=[
                # Add topic remappings here if needed
                # ('old_topic', 'new_topic')
            ]
        ),
        Node(
            package='challenge1',
            executable='process_node',
            name='process_node',
            output='screen',
            parameters=[
                # Add parameters here if needed
                # {'param_name': param_value}
            ],
            remappings=[
                # Add topic remappings here if needed
                # ('old_topic', 'new_topic')
            ]
        ),
        Node(
            name ='rqt_plot',
            package='rqt_plot',
            executable='rqt_plot',
            arguments=['/proc_signal/data', '/signal/data'],
            output='screen'
        )
    ])