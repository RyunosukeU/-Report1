import numpy as np
def matrix(a, b, c, d, A1, A2):
  A = np.matrix([[a, b], [c, d]])
  determinant = np.linalg.det(A)
  if determinant != 0:
     inv_A = np.matrix(np.linalg.inv(A))
     B = np.matrix([[A1],[A2]])
     X = inv_A * B
     print(X)
  else:
    if c/a == A1 / A2:
      print('解が複数存在します')
    else:
      print('解が存在しません')
      
a = float(2)
b = float(-3)
c = float(5)
d = float(-2)
A1 = float(1)
A2 = float(8)

matrix(a, b, c, d, A1, A2)