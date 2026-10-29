# ROS 2 Turtlesim Navigation System

## Overview
A beginner robotics project built with ROS 2 Jazzy,
Ubuntu 24.04 and Python using the Turtlesim simulator.

## Features
- Target-based turtle navigation
- Position feedback using ROS 2 topics
- Linear and angular velocity control
- Pentagon drawing experiment

## Technologies
- Ubuntu 24.04
- ROS 2 Jazzy
- Python
- Turtlesim
- Colcon

## Installation
Source ROS 2:

    source /opt/ros/jazzy/setup.bash

Build the package:

    cd ~/turtle_ws
    colcon build --packages-select turtle_navigation

Source the workspace:

    source install/setup.bash

Run the simulator in one terminal:

    ros2 run turtlesim turtlesim_node

Run the navigation program in another terminal:

    ros2 run turtle_navigation navigator
