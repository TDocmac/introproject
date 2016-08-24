from numpy import float32
from scipy.sparse import dok_matrix
import time

t0 = time.time()

ratings = open("ratings.dat")

dict_movies = {}
dict_user = {}
matriz = dok_matrix((71568, 65134),dtype=float32)
lista_peli = []
lista_user = []

for i in range(65134):
    if i not in dict_movies:
        lista_peli.append(0)
    else:
        lista_peli.append(dict_movies[i])

for i in range(71568):
    lista_user.append([])

for linea in ratings:
    linear = linea.strip().split("::")
    if int(linear[1]) not in dict_movies:
        dict_movies[int(linear[1])] = []
    lista_user[int(linear[0])].append(int(linear[1]))
    #if linear[0] not in dict_user:
    #    dict_user[linear[0]] = []
    dict_movies[int(linear[1])].append(int(linear[0]))
    #dict_user[linear[0]].append(linear[1])
    matriz[int(linear[0]), int(linear[1])] = float(linear[2])

ratings.close()


t1 = time.time()


def similitud(user1,user2,matrix):
    lista1 = []
    lista2 = []
    lista_rat = []
    conj = set(lista_user[user1]) & set(lista_user[user2])
    for j in conj:
            lista_rat.append(matrix[user1,j] * matrix[user2,j])
            lista1.append(matrix[user1,j]**2)
            lista2.append(matrix[user2,j]**2)
    suma1 = sum(lista1)
    suma2 =  sum(lista2)
    suma_ratings = sum(lista_rat)
    if suma1 == 0  or suma2 == 0:
        return 0
    divisor = (suma1**0.5) * (suma2**0.5)

    return suma_ratings/divisor

t2 = time.time()

def prediccion(columna,user,matrix):
    lista_suma = []
    lista_div = []
    for j in lista_peli[columna]:
            sim = similitud(user, j, matrix)
            lista_suma.append(matriz[j, columna] * sim)
            lista_div.append(sim)
    suma = sum(lista_suma)
    divisor = sum(lista_div)
    if divisor == 0:
        return 0
    return suma/divisor




#print similitud(1,3,matriz)
print prediccion(518,1,matriz)
t3 = time.time()
print t3-t1

def top10(usuario):
    a =[0,0,0,0,0,0,0,0,0,0]
    for movie in dict_movies:
        p = prediccion(usuario, movie,matriz)
        if p > a[9]
            for r in range(len(a)):
                if p>a[r]:
                    a.insert(r,p)
                    del a[10]
                    break
    return a

#print top10(1)
