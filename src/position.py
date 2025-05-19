import numpy as np


def multiply(matrix1, matrix2):
    matrix = np.multiply(matrix1, matrix2)
    sut = [
        matrix[0][0][0][0] + matrix[0][1][0][0],
        matrix[0][0][1][1] + matrix[0][1][1][1]
    ]
    return sut


def multiply4(compose1, compose2):
    return np.array([
        [(compose1[0][0] @ compose2[0][0] + compose1[0][1] @ compose2[1][0]),
         (compose1[0][1] @ compose2[1][0] + compose1[0][1] @ compose2[1][1])],
        [(compose1[1][0] @ compose2[0][0] + compose1[1][1] @ compose2[1][0]),
         (compose1[1][0] @ compose2[0][1] + compose1[1][1] @ compose2[1][1])]
    ])


def adapt(vec):
    return np.array([np.array([[vec[0]], [vec[1]]]), np.array([[1], [1]])])

def R(theta):
    """
    given an angle in radians, return the rotation matrix for that angle
    ---------------------------------
    input
    theta: Number, rotation in radians
    ---------------------------------
    output
    numpy.array, the rotation matrix
    """
    return np.array([
        [np.cos(theta), np.sin(theta)],
        [-np.sin(theta), np.cos(theta)],
    ],
                    dtype=np.ndarray)


def R_inverse(theta):
    """
    given an angle in radians, return the inverse rotation matrix for that angle
    note that such matrix is the transpose of the rotation matrix, R(theta)
    -----------------------------------
    input
    theta: Number, rotation in radians
    ----------------------------------
    output
    numpy.array, the inverse of the rotation matrix
    """
    return np.array([
        [np.cos(theta), -np.sin(theta)],
        [np.sin(theta), np.cos(theta)],
    ]),


def SE2_xy(x, y):
    """
    given a translation coordinate in 2D return the corresponding homogenous matrix as numpy.array
    SE stands for special euclidian group
    -------------------------------------
    input
    x: Number, translation in the x-axis
    y: Number, translation in the y-axis
    -------------------------------------
    output
    numpy.array, the linear transformation responsible for translation
    """
    return np.array(
        [

            [[[0,0],[0,0]], [[x, 0],[0,y]]],
            # dot is matrix product
            [[[0, 0],[0,0]], [[0,0],[0,0]]]

        ], dtype=np.ndarray) #yapf:disable


def SE2_theta(theta):
    """
    given a rotation angle in radians return the correspoding homogenous matrix as numpy.array
    SE stands for special euclidian group
    -------------------------------------
    input
    theta: Number, rotation in radians
    -------------------------------------
    output
    numpy.array, the linear transformation responsible for rotation
    """
    return np.array(
            [

                [R(theta),[[0,0],[0,0]]],
                [[[0,0],[0,0]], [[1,0],[0,1]]]

            ],dtype=np.ndarray) #yapf: disable

def SE2_pose(x=0.0, y=0.0, theta=0):
    """
    composition of SE2_theta and SE2_xy, returns a homogeneous matrix as numpy.array
    _____________________________________
    input
    x: Number, translation in the x-axis in meters
    y: Number, translation in the y-axis in meters
    theta: Number, rotation in radians
    ----------------------------------------
    return
    hom: Numpy array, homogeneous transformation matrix
    """
    return SE2_theta(theta) + SE2_xy(x, y)

