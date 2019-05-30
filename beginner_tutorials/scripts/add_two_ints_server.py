#!/usr/bin/env python

from beginner_tutorials.srv import *
import rospy

def handle_add_two_ints(req):
    if ( req.c == 1 ) :
    	print "Returning [%s + %s = %s]"%(req.a, req.b, (req.a + req.b))
    	return AddTwoIntsResponse(req.a + req.b) + "True"
    elif ( req.c==2 ) :
	print "Returning [%s - %s = %s]"%(req.a, req.b, (req.a - req.b))
	return AddTwoIntsResponse(req.a - req.b) + "True"
    	
    elif ( req.c==3 ) :
    	print "Returning [%s * %s = %s]"%(req.a, req.b, (req.a * req.b))
    	return AddTwoIntsResponse(req.a * req.b) + "True"	
    elif ( req.c==4 ) :
    	print "Returning [%s / %s = %s]"%(req.a, req.b, (req.a / req.b))
    	return AddTwoIntsResponse(req.a / req.b) + "True"
    else :
    	print"Returning 0"
    	return "0 False"
    
def calc_server():
    rospy.init_node('calc_server')
    s = rospy.Service('calc', AddTwoInts, handle_add_two_ints)
    print "Ready to perform calculations."
    rospy.spin()

if __name__ == "__main__":
    calc_server()
