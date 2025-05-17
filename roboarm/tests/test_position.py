import math
import pytest
import src.position
import numpy as np
from math import pi


class Test:

    def setup_method(self):
        pass

    def test_point_coords_in_reference_frame_given_translated_object_frame(
            self):
        sut = src.position.multiply(src.position.SE2_pose(x=1, y=0.25),
                                    src.position.adapt([0.5, 0.5]))
        np.testing.assert_array_equal(sut, np.array([1.5, 0.75]))

    def test_point_coords_in_translated_object_frame_given_reference_frame(
            self):
        sut = src.position.multiply(src.position.SE2_pose(x=-1, y=-0.25),
                                    src.position.adapt([0.5, 0.5]))
        np.testing.assert_array_equal(sut, [-0.5, 0.25])

    def test_point_coords_in_reference_frame_given_posed_object_frame(self):
        sut = src.position.multiply(
            src.position.SE2_pose(x=1, y=0.25, theta=math.pi / 4),
            src.position.adapt([0.5, 0.5]))
        np.testing.assert_array_equal(sut, [-0.5, 0.25])

    def test_point_in_posed_object_frame_given_reference_frame(self):
        sut = src.position.multiply(
            src.position.SE2_pose(x=-1, y=-0.25, theta=-math.pi / 4),
            src.position.adapt([0.5, 0.5]))
        np.testing.assert_array_equal(sut, [-0.5, 0.25])

    def test_point_in_object_frame_given_rotated_reference_frame(self):
        sut = src.position.multiply(
            src.position.SE2_pose(x=0.0, y=-0.0, theta=math.pi / 4),
            src.position.adapt([0.5, 0.5]))
        np.testing.assert_array_equal(sut, [-0.5, 0.25])

    def test_point_in_object_frame_equal_to_non_posed_reference_frame(self):
        sut = src.position.multiply(
            src.position.SE2_pose(x=0.0, y=-0.0, theta=0),
            src.position.adapt([0.5, 0.5]))
        np.testing.assert_array_equal(sut, [0.5, 0.5])

    def test_point_in_object_frame_given_rotated_reference_frame_anticlockwise_is_same_as_clockwise(
            self):
        sut = src.position.multiply(
            src.position.SE2_pose(x=0.0, y=-0.0, theta=-pi / 4),
            src.position.adapt([0.5, 0.5]))
        sut2 = src.position.multiply(
            src.position.SE2_pose(x=0.0, y=-0.0,
                                  theta=(3 * pi) / 2 + (pi / 4)),
            src.position.adapt([0.5, 0.5]))
        np.testing.assert_array_almost_equal(sut, sut2)

    def test_point_in_reference_frame_given_pose_composition_in_object_frame(
            self):
        compose1 = src.position.SE2_pose(x=1.0, y=0.25, theta=0)
        compose2 = src.position.SE2_pose(x=0.0, y=0.0, theta=pi / 4)
        composed = src.position.multiply4(compose1, compose2)
        sut = src.position.multiply(composed, src.position.adapt([0.5, 0.5]))
        np.testing.assert_array_almost_equal(sut, [1.353, 0.604], 2)
