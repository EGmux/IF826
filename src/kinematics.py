from math import cos, radians, sin
import numpy
import src.position as hom


def fk(theta1, theta2):
    """
    given a robotic arm configuration, type RR, find the pose in the effector frame
    --------------------------
    input
    theta1: Number, angle in radians of the first joint
    theta2: Number, angle in radians of the second joint
    --------------------------
    return
    x: Number, effector frame translation from base joint in the x-axis
    y: Number, effector frame translation from base joint in the y-axis
    theta: Number, in radians, effector frame rotation angle
    fk: Numpy.array, linear transformation from base joint frame to effector frame
    """
    fk = hom.SE2_pose(x=cos(theta1+theta2)+cos(theta1),y=sin(theta1+theta2)+sin(theta1),theta= theta1+theta2)
    return (fk[0][1][0],fk[0][1][1],theta1+theta2,fk)

def ik(x,y):
    """
    given a robotic arm, type RR, effector pose, return the required joint configuration
    ----------------------
    input
    x: Number, x coordinate of effector frame
    y: Number, y coordinate of effector frame
    ----------------------
    return
    theta1: Number, angle in radians, angle of first joint
    theta2: Number, angle in radians, angle of second joint
    """
    theta2 = numpy.arccos((x^2 + y^2 -2)/2)
    theta1 = numpy.arctan(y/x)-(numpy.arctan(sin(theta2)/(1+cos(theta2))))
    return (theta1,theta2)

