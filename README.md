# ROS 2 Turtlesim Navigation System

A robotics simulation project developed using ROS 2 Jazzy, Python, and Ubuntu 24.04.

## Overview

This project demonstrates target-based navigation of a turtle in the ROS 2 Turtlesim environment. A custom Python node controls the turtle using velocity commands and position feedback.

The project helps demonstrate the fundamentals of robot motion control and ROS 2 communication.

## Features

- Target-based turtle navigation
- Position feedback using ROS 2 topics
- Linear and angular velocity control
- Pentagon drawing experiment

## Technologies Used

- ROS 2 Jazzy
- Ubuntu 24.04 LTS
- Python 3
- Turtlesim
- Colcon
- Git and GitHub

## Project Structure

```text
turtle_navigation/
├── package.xml
├── setup.py
├── setup.cfg
├── resource/
├── turtle_navigation/
│   ├── __init__.py
│   └── navigator.py
└── README.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/zeeshanshaikh07-bit/ros2-turtlesim-navigation.git
```

Build the ROS 2 package:

```bash
cd ros2-turtlesim-navigation
colcon build
source install/setup.bash
```

## How to Run

Open Terminal 1:

```bash
source /opt/ros/jazzy/setup.bash
ros2 run turtlesim turtlesim_node
```

Open Terminal 2:

```bash
source /opt/ros/jazzy/setup.bash
source ~/turtle_ws/install/setup.bash
ros2 run turtle_navigation navigator
```

## Learning Outcomes

- Understanding ROS 2 nodes and topics
- Working with Python in ROS 2
- Implementing velocity-based robot control
- Understanding position feedback
- Building ROS 2 packages with Colcon

## Future Improvements

- Improve navigation accuracy
- Add configurable target positions
- Implement obstacle avoidance
- Add launch files
- Extend the project to a mobile robot

## Author

**Zeeshan Shaikh**

B.Tech – Robotics and Automation

GitHub: [zeeshanshaikh07-bit](https://github.com/zeeshanshaikh07-bit)

## License

For educational purposes.
