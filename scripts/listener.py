#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
import math

def callback(msg):
    rospy.loginfo("Received a /cmd_vel message")
    rospy.loginfo("Components: [linear_x=%.3f, linear_y=%.3f, angular_z=%.3f]", msg.linear.x, msg.linear.y, math.degrees(msg.angular.z))
    
def listener():
    rospy.init_node('cmd_vel_listener')
    rospy.Subscriber("/cmd_vel", Twist, callback)
    rate = rospy.Rate(1)
    rate.sleep()
    rospy.spin()

if __name__ == '__main__':
    listener()

