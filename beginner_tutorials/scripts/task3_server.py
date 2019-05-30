#!/usr/bin/env python

from beginner_tutorials.srv import *
import rospy
import time

def handle_msg(req):
	start = time.time()
	count=0
	while (req.a != "a given sequence"):
		count++
		print("Length of the message is",len(a))
	count++
	done = time.time()
	elapsed = done - start
    	return task3Response("The time elapsed is",elapsed,"and the number o messages sent are",count)

def givenseq_server():
	rospy.init_node('givenseq_server')
	s = rospy.Service('givenseq', task3, handle_msg)
	print "Ready to take inputs."
	rospy.spin()

if __name__ == "__main__":
	givenseq_server()
