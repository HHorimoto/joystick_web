# joystick_web

**This package provides the website has a joystick.**

**You can control your robots with the joystick.**

<img src=./images/index.png width="50%">

## Video

if you are interested in this package., please check [here](https://youtu.be/s7hZe3tuLwk)

## Requirement
+ Ubuntu18.04
+ ROS(Melodic)

## SetUp
Download this package

```shell
$ cd ~/catkin_ws/src/
$ git clone https://github.com/HHorimoto/joystick_web.git
$ cd ~/catkin_ws
$ catkin_make
```

Download necessary ROS package for this package.

```shell
$ sudo apt-get install ros-melodic-roswww
$ sudo apt-get install ros-melodic-rosbridge-server
```

## How to Use

1. Start the launch with command
```shell
$ roslaunch joystick_web ros_web.launch
```

2. Go to the url : `http://localhost:8085/joystick_web/`

## License

Distributed under the MIT License. See `LICENSE` for more information.