from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # Nodo de signal_generator
        Node(
            package='challenge1',
            executable='signal_generator',
            name='signal_generator',
            output='screen',
            parameters=[
            ],
            remappings=[
            ]
        ),
        # Nodo de process_node
        Node(
            package='challenge1',
            executable='process_node',
            name='process_node',
            output='screen',
            parameters=[
            ],
            remappings=[
            ]
        ),
        # Nodo de rqt plot para visualizar ambos nodos
        Node(
            name ='rqt_plot',
            package='rqt_plot',
            executable='rqt_plot',
            arguments=['/proc_signal/data', '/signal/data'],
            output='screen'
        )
    ])