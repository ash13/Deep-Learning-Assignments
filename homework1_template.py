import numpy as np

def problem1 (A, B):
	return A + B

def problem2 (A, B, C): #AB - C
	return np.dot(A,B) - C

def problem3 (A, B, C): #A*B -C
	return (A*B)- np.transpose(C)

def problem4 (x, y):
	return np.dot(np.transpose(x),y)

def problem5 (A):
	return np.zeros(A.shape)

def problem6 (A):
	return np.ones(A.shape[0])

def problem7 (A, x):
	return np.dot((np.linalg.inv(A)*(-1) ),x)

def problem8 (A, x):
	return ...

def problem9 (A, alpha):
	return ...

def problem10 (A, i, j):
	return A[i][j]

def problem11 (A, i):
	return np.sum(A[i])

def problem12 (A, c, d):
	return ...

def problem13 (A, k):
	return ...

def problem14 (x, k, m, s):
	return ...
