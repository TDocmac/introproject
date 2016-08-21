import time
from numpy import float32
from scipy.sparse import dok_matrix

t0 = time.time()

ratings = open("ratings.dat")

dict_movies = {}
dict_user = {}
dict_user_rating = {}
matriz = dok_matrix((71567, 65134),dtype=float32)

for linea in ratings:
    linear = linea.strip().split("::")
    if int(linear[1]) not in dict_movies:
        dict_movies[int(linear[1])] = []
    if int(linear[0]) not in dict_user:
        dict_user[int(linear[0])] = []
    dict_movies[int(linear[1])].append(int(linear[0]))
    dict_user[int(linear[0])].append(int(linear[1]))
    matriz[linear[0], linear[1]] = linear[2]

ratings.close()

t4 = time.time()

print "tiempo diccionarios"
print t4-t0
'''
def similitud(usera,usercomp):
    suma_superior = 0
    suma_inferiori = 0
    suma_inferiord = 0
    peliculascomun = set(dict_user[usera]) & set(dict_user[usercomp])
    peliculasusera = dict_user[usera]
    peliculasusercomp = dict_user[usercomp]

    for pelicula in peliculascomun:
        suma_superior += dict_user_rating[(usera, pelicula)] * dict_user_rating[(usercomp, pelicula)]
    for pelicula in peliculasusera:
        suma_inferiori += (dict_user_rating[(usera, pelicula)]**2)
    for pelicula in peliculasusercomp:
        suma_inferiord += (dict_user_rating[(usercomp, pelicula)] ** 2)
    return suma_superior / ((suma_inferiori)**0.5 * (suma_inferiord)**0.5)

def prediccion(usera,pelicula):
    usuarios = dict_movies[pelicula]
    suma_sup = 0
    suma_inf = 0
    for usuario in usuarios:
        sim = similitud(usera, usuario)
        suma_sup += sim * dict_user_rating[usuario, pelicula]
        suma_inf += sim
    return suma_sup / suma_inf


t2 = time.time()
print prediccion(1,110)
t3 = time.time()
print t3-t2


t1 = time.time()
total = t1-t0
print total
'''