# joystick_web
This package provides the website has a joystick.

You can control your robots with the joystick.

THANK YOU SO MUCH FOR [JoyStick](https://github.com/bobboteck/JoyStick). I use `JoyStick` for making my packge.

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

## References
[1] bobboteck, 2021. https://github.com/bobboteck/JoyStick (accessed 2022 July 28)

[2] Isaac Saito, 2020. http://wiki.ros.org/roslibjs/Tutorials/BasicRosFunctionality (accessed 2022 July 28)