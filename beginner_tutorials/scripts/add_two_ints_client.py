#!/usr/bin/env python

import sys
import rospy
from beginner_tutorials.srv import *

def add_two_ints_client(x, y, z):
    rospy.wait_for_service('calc')
    try:
        calc = rospy.ServiceProxy('calc', AddTwoInts)
        resp1 = calc(x, y, z)
        return resp1.sum
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

def usage():
    return "%s [x y z]"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 4:
        x = int(sys.argv[1])
        y = int(sys.argv[2])
    	z = int(sys.argv[3])
    else:
        print usage()
        sys.exit(1)
    if ( z==1 ) :
    	print "Requesting %s+%s"%(x, y)
    	print "%s + %s = %s"%(x, y, add_two_ints_client(x, y, z))
    elif ( z==2 ) :
    	print "Requesting %s-%s"%(x, y)
    	print "%s - %s = %s"%(x, y, add_two_ints_client(x, y, z))
    elif ( z==3 ) :
    	print "Requesting %s*%s"%(x, y)
    	print "%s * %s = %s"%(x, y, add_two_ints_client(x, y, z))
    elif ( z==4 ) :
    	print "Requesting %s/%s"%(x, y)
    	print "%s / %s = %s"%(x, y, add_two_ints_client(x, y, z))
    else :
    	print "Requesting "%(x, y)
    	print ""%(x, y, add_two_ints_client(x, y, z))
