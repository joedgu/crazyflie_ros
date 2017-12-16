#!/usr/bin/env python

import rospy
import tf
from geometry_msgs.msg import TransformStamped, PoseStamped


rospy.init_node('publish_pose', anonymous=True)
worldFrame = rospy.get_param("~worldFrame", "/world")
name = rospy.get_param("~name")
r = rospy.get_param("~rate")
x = rospy.get_param("~x")
y = rospy.get_param("~y")
z = rospy.get_param("~z")


def callback():

	msg = PoseStamped()
    msg.header.seq = 0
    msg.header.stamp = rospy.Time.now()
    msg.header.frame_id = worldFrame
    msg.pose.position.x = x
    msg.pose.position.y = y
    msg.pose.position.z = z
    quaternion = tf.transformations.quaternion_from_euler(0, 0, 0)
    msg.pose.orientation.x = quaternion[0]
    msg.pose.orientation.y = quaternion[1]
    msg.pose.orientation.z = quaternion[2]
    msg.pose.orientation.w = quaternion[3]
    
    msg.header.seq += 1
    msg.header.stamp = rospy.Time.now()
	
	pub.publish(msg)
	rate.sleep()

#sub = rospy.Subscriber('/vicon/Quad7/Quad7', TransformStamped, callback)
#pub = rospy.Publisher('vicon_repub_pose', PoseStamped
pub = rospy.Publisher(name, PoseStamped, queue_size=1)

rospy.spin()
