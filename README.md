# roboarm is a python library that provides a simple API to control a robotic arm

## Position module

This module provides functions to compute the coordinates of a point in a target frame given an origin frame by the means of a homogeneous transformation matrix in the euclidian plane.

- SE2_xy: given two coordinates, returns a translation matrix for the target frame.

- SE2_theta: given a rotation angle, in radians, returns a rotation matrix for the target frame.

- SE2_pose: given two coordinates and an angle returns the homogeneous transformation matrix for the target frame.

after calling one of the above functions apply the resulting matrix to a vector to get the position of the point in the target frame.

## Control module

TODO

## Trajectory module

TODO
