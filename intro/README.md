This *intro* directory contains three packages that explore the basics of Robotics
Operating System(ROS) namely ROS nodes, topics, services, launches, pub-sub, and custom
messages. 

These tutorials are basically follow the tutorials that are available in the [ROS docs](https://docs.ros.org/en/galactic/Tutorials.html). Also, this is an attempt to implement these basics in ROS2.

Here, [ROS2 Galactic](https://docs.ros.org/en/galactic/index.html) version is used. 

## my_package

Explores the publisher-subscriber model, and also integrates the use of custom message
type.

Some of the highlights/thoughts:
- Uses `ament_python` as build tool
- `setup.py` complements `CMakeLists.txt` in python setup.
- `setup.py`'s `entry_points` tag allows to define the node's entry point.
- Python scripts are placed inside the `node_name`(which often has the same name as the
  `package_name`).

## py_srvcli

Explores the minimal service-client approach. Also tests simple custom services. 

## custom_interfaces

Package to familiarise making custom msg and service. The package is built using
`ament_cmake` as currently there is no way to do it with python. These new custom
msgs/srvs have to be converted into source code in both C++ and python. So, we make use of
**interface definition language**(IDL). Therefore, ROS IDL generators/interfaces are added as
dependencies in `CMakeLists.txt` and `package.xml`.
