# Matias Moreno
# Benjamin Camblor
# Jose Tomas Docmac

from random import choice
from numpy import float32
from scipy.sparse import dok_matrix
import time

t0 = time.time()


dict_movies = {}
dict_user = {}
matriz = dok_matrix((71568, 65134),dtype=float32)
lista_peli = []
lista_user = []
peliculas = []

for i in range(71568):
    lista_user.append([])

movies = open("movies.dat")
ratings = open("ratings.dat")

for pelicula in movies:
    l_pelicula = pelicula.strip().split("::")
    peliculas.append(int(l_pelicula[0]))




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



for i in range(65134):
    if i not in dict_movies:
        lista_peli.append([])
    else:
        lista_peli.append(dict_movies[i])

t1 = time.time()
print "diccionario"
print t1-t0

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


def num_pelis(num):
    l_pelis = []
    for i in range(num):
        l_pelis.append(choice(peliculas))
    l_final = list(set(l_pelis))
    return l_final


def top(usuario,num):
    l_predicciones = []
    l_top10 = []
    l_pelis = num_pelis(num)
    t_top0 = time.time()
    j = 0
    print "Realizando predicciones, espere por favor..."
    for i in l_pelis:
        p = prediccion(i,usuario,matriz)
        l_predicciones.append((round(p,1),i))
        j += 1
        if j == 1:
            t_top2 = time.time()
            print "Tiempo que toma una prediccion = "+str(round((t_top2-t_top0),3))+" segundos"
            print "Tiempo estimado total = "+str(round((t_top2-t_top0),3)*num)+" segundos"
    l_predicciones.sort()
    l_predicciones.reverse()
    for i in range(10):
        l_top10.append(l_predicciones[i])
    t_top1 = time.time()
    l_top10_nombres = []
    for tupla in l_top10:
        for linea in movies:
            a = linea.strip().split("::")
            if int(tupla[1]) == int(a[0]):
                l_top10_nombres.append((a[1],tupla[0]))
                break
    print "El top 10 de las "+str(num)+" peliculas es:"
    print l_top10_nombres
    print "Tiempo de prediccion para el usuario "+str(usuario)+" con "+str(num)+" peliculas, es de "+str(round(t_top1-t_top0))+" segundos."

top(1,30)
t4 = time.time()
print "tiempo total"
print t4-t0

print "Bienvenido al sistema de recomendaciones Sansanito"
sel = 1
while sel != 0:
    print "Por favor, indique el numero del usuario al cual desea hacer la prediccion"
    sel = int(raw_input("Seleccion: "))
    print "Por favor, indique el numero de peliculas al azar que seran seleccionadas en la base de datos"
    num = int(raw_input("Seleccion:"))
    top(sel,min(num,65134))
    print "Para realizar otra prediccion ingrese '1'"
    print "Para salir ingrese '0'"
    sel = int(raw_input("Seleccion: "))

if sel == 0:
    movies.close()
    ratings.close()
