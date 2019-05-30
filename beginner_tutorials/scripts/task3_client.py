#!/usr/bin/env python

import sys
import rospy
from beginner_tutorials.srv import *

def givenseq_client(x):
    rospy.wait_for_service('givenseq')
    try:
        calc = rospy.ServiceProxy('givenseq', task3)
        resp1 = givenseq(x)
        return resp1.outputmsg
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

def usage():
    return "%s [x]"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 2:
        x = str(sys.argv[1])

    else:
        print usage()
        sys.exit(1)


