import numpy as np
from scipy.sparse import dok_matrix
import time

ratings = open("ratings.dat")

t0 = time.time()
matriz = np.zeros((71567+1,65133+1), dtype=np.float32)
for i in range(71568):
    matriz[i,0] = i
for j in range(65134):
    matriz[0,j] = j
for linea in ratings:
    a = linea.strip().split("::")
    matriz[int(a[0]),int(a[1])] = float(a[2])


ratings.close()


def similitud(user1,user2,matrix):
    i = 1
    suma1 = 0
    suma2 = 0
    suma_ratings = 0
    a = matrix[user1]
    b = matrix[user2]
    for j in range(65133):
        if a[i] != 0 and b[i] != 0:
            suma_ratings += a[i] * b[i]
        suma1 += a[i]**2
        suma2 += b[i]**2
        i+=1
    divisor = (suma1**0.5) * (suma2**0.5)

    return suma_ratings/divisor

t1 = time.time()

def prediccion(columna,user,matrix):
    i = 1
    suma = 0
    divisor = 0
    for j in range(71567):
        if matrix[i,columna] != 0:
            sim = similitud(user,matrix[i,0],matrix)
            suma += matriz[i,columna] * sim
            print i
            divisor += sim
        i += 1
    return suma/divisor



t2 = time.time()


#print similitud(5510,5641,matriz)
print prediccion(518,1,matriz)
print t2-t1











'''
mat = dok_matrix((71567,65133), dtype=np.float32)
for linea in ratings:
    a = linea.strip().split("::")
    mat[int(a[0]),int(a[1])] = float(a[2])

print mat
'''





