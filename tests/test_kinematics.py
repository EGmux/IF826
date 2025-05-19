import math
import pytest
import src.kinematics as kinematics
import numpy as np
from math import pi


class Test:

    def setup_method(self):
        pass

    def test_RR_rotation_in_second_joint(
            self):
        sut = kinematics.fk(theta1=0,theta2=pi/2)
        x,y,theta, _ = sut
        np.testing.assert_almost_equal(x[0],1)
        np.testing.assert_almost_equal(y[1],1)
        np.testing.assert_almost_equal(theta,pi/2)

    def test_RR_rotation_in_both_joints(self):
        sut = kinematics.fk(theta1=pi/2,theta2=pi/2)
        x,y,theta,_ = sut
        np.testing.assert_almost_equal(x[0],-1)
        np.testing.assert_almost_equal(y[1],1)
        np.testing.assert_almost_equal(theta,pi)

    def test_RR_rotation_anticlockwise_and_clockwise(self):
        sut = kinematics.fk(theta1=pi/2,theta2=-pi/2)
        x,y,theta,_ = sut
        np.testing.assert_almost_equal(x[0],1)
        np.testing.assert_almost_equal(y[1],1)
        np.testing.assert_almost_equal(theta,0)

    def test_RR_rotation_identity(self):
        sut = kinematics.fk(theta1=-pi,theta2=pi)
        x,y,theta,_ = sut
        np.testing.assert_almost_equal(x[0],0)
        np.testing.assert_almost_equal(y[1],0)
        np.testing.assert_almost_equal(theta,0)

    def test_RR_rotation_effector_in_origin(self):
        sut = kinematics.fk(theta1=pi/2,theta2=-pi)
        x,y,theta,_ = sut
        np.testing.assert_almost_equal(x[0],0)
        np.testing.assert_almost_equal(y[1],0)
        np.testing.assert_almost_equal(theta,-pi/2)

