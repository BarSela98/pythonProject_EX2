import numpy as np
import numpy as np


# Q1.1
def half(x):
    arr = np.array(x)
    return arr[1::2, 0::2] / 2


# Q1.2
def outer_product(x, y):
    return np.outer(x, y)


# Question 1.3
# ????????????????????????????????


# --------------- Question 1.4 ---------------

from numpy import linalg as LNG


def calc_norm(x, axis=0):
    return LNG.norm(x, axis)


def normalize(x, axis=0):
    norm_vec = np.array(calc_norm(x, axis))
    norm_vec = norm_vec.reshape((np.size(norm_vec)), 1)
    if axis == 0:  # cols of x normalized
        return (x.transpose() / norm_vec).transpose()
    else:  # rows of x normalized
        return x / norm_vec


# --------------- Question 1.5 ---------------
def matrix_norm(x, k=1000):
    return max(calc_norm(np.matmul(x, normalize(np.random.randn(x.shape[0], k), 0)), 0))


# --------------- Question 1.6 ---------------
def det(A):
    d = 0
    if A.shape == (2, 2):
        d = A[0, 0] * A[1, 1] - A[0, 1] * A[1, 0]
    else:
        num_rows, num_cols = A.shape
        for i in range(num_rows):
            temp_arr = np.delete(A, i, axis=0)
            temp_arr = np.delete(temp_arr, 0, axis=1)
            print(temp_arr)
            d = d + ((-1) ** i) * A[i, 0] * det(temp_arr)
    return d


# A = np.array([[1,2,3],[4,30,6],[7,8,20]])
# print(det(A))
# print(np.linalg.det(A))

# --------------- Question 1.7 ---------------

def segment(im, thresh=128):
    if im.ndim == 2:
        im_bw = im.astype(int)
    else:
        im_bw = np.mean(im, axis=2).astype(int)
    return np.where(im_bw < thresh, 0, 255)


# --------------- Question 1.8 ---------------

def linearville(robber, policeman):
    hours, stores, days = robber.shape
    x = robber.sum(axis=2)
    arr = x.sum(axis=1) == hours
    if np.array(np.where(arr == False)).size > 0:
        print("invalid input")
        return False

    for x in range(days):
        arr = np.where(robber[:, :, x] == policeman, 1, 0)
        if (np.any(arr.sum(axis=1) == stores)):
            return "Catch"
    return "Escape"


robber = np.zeros((2, 3, 2)).astype(int)
# 2 days
# 3 stores
# 2 hours
# first day - first hour
robber[0][0][0] = 1
robber[0][1][0] = 0
robber[0][2][0] = 0
# second hour
robber[1][0][0] = 0
robber[1][1][0] = 1
robber[1][2][0] = 0

# second day - first hour
robber[0][0][1] = 1
robber[0][1][1] = 0
robber[0][2][1] = 0
# second hour
robber[1][0][1] = 0
robber[1][1][1] = 1
robber[1][2][1] = 0

###########

policeman = np.zeros((2, 3)).astype(int)
# 3 stores
# 2 hours
# first hour
policeman[0][0] = 0
policeman[0][1] = 1
policeman[0][2] = 0
# second hour
policeman[1][0] = 0
policeman[1][1] = 0
policeman[1][2] = 1


# print(linearville(robber, policeman))


# --------------- Question 1.9 ---------------

def isMagicSquare(IsMagicSquare):
    s = np.trace(IsMagicSquare)
    row = IsMagicSquare.sum(axis=1)
    col = IsMagicSquare.sum(axis=0)

    opp_s = np.diag(np.fliplr(IsMagicSquare)).sum()
    if not np.all(row == s):
        return "Not a magic square"
    if not np.all(col == s):
        return "Not a magic square"
    if not opp_s == s:
        return "Not a magic square"
    return "It is magic square !!!"


#square = np.array([[17, 24, 1, 8, 15], [23, 5, 7, 14, 16], [4, 6, 13, 20, 22], [10, 12, 19, 21, 3], [11, 18, 25, 2, 9]])
#print(isMagicSquare(square))
