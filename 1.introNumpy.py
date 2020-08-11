import numpy as np

number = [1, 2, 3]
numberNp = np.array(number)
print(numberNp * 3)

listNumber = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2d = np.array(listNumber)
print(matrix2d * numberNp)

print('# Membuat array 1 dimensi 0 - 9')
print(np.arange(0, 10))

print('# Membuat array 0 - 3 dengan jarak 5')
print(np.arange(0, 30, 5))

print('# Membuat array dengan value 0')
print(np.zeros(5))

print('# Membuat matrik 2D value 0')
print(np.zeros((2, 4)))

print('# Membuat matrik 2D value 1')
print(np.ones((2, 5)))

print('# Membuat matrik 2D value 0 sampai 20, dan dipecah menjadi 5')
print(np.linspace(0, 20, 5))
