import numpy as np

'''def similitud(user,cercano):

    usuario = open("ratings.dat")
    lista_user = []
    lista_cercano = []
    for linea in usuario:
        if str(user) == linea.strip().split("::")[0]:
            lista_user.append(linea.strip().split("::")[1])
        elif str(cercano) == linea.strip().split("::")[0]:
            lista_cercano.append(linea.strip().split("::")[1])
    conjunto_user = set(lista_user)
    conjunto_cercano = set(lista_cercano)
    interseccion = conjunto_user & conjunto_cercano
    usuario.close()
    '''

'''archivo1 = np.loadtxt("ratings.dat", dtype = "float" ,comments = "#", delimiter = "::", usecols = (0,1,2))
np.save("archivo2",archivo1)'''


archivo = np.load("archivo2.npy")
'''
final = []
i = 0
for linea in archivo:
    if i < linea[0]:
        i += 1
        final.append([i,[]])
    if i == linea[0]:
        final[i-1][1].append((linea[1],linea[2]))
'''


final_peli = {}
for linea in archivo:
    if linea[1] not in final_peli:
        final_peli[linea[1]] = []
    final_peli[linea[1]].append((linea[0],linea[2]))



ratings = open("ratings.dat")

d={}
for linea in ratings:
    linear = linea.strip().split("::")
    d[int(linear[0]),int(linear[1])]=(linear[2])

def top10(usuario):
    a =[0,0,0,0,0,0,0,0,0,0]
    for movie in dict_movies:
        p = prediccion(usuario, movie)
        for r in range(len(a)):
            if p>a[r]:
                a[r]=p
                break
    return a


