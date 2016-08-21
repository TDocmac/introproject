from scipy.sparse import dok_matrix
from numpy import float32
from time import time
from re import sub

def correlacion(promedio_principal,promedio_user2,conjuntolibros,indiceprincipal,indiceuser2,matrizita):
    numerador = 0
    denominador1 = 0
    denominador2 = 0
    if len(conjuntolibros)==1:
        return 0
    for libro in conjuntolibros:
        numerador += (matrizita[indiceprincipal,libro]-promedio_principal)*(matrizita[indiceuser2,libro]-promedio_user2)
        denominador1 += (matrizita[indiceprincipal,libro]-promedio_principal)**2
        denominador2 += (matrizita[indiceuser2,libro]-promedio_user2)**2
    denominador = (denominador1**0.5)*(denominador2**0.5)
    if numerador == 0.0: #No hay correlacion lineal puede ser de otro tipo pero perason es lineal/ NaN es 0 por 0/0
        return 0
    return numerador/denominador

def ratingponderado(correlaciones, dic_user, matriz, indiceuser, libro, dic_libros):
    numerador = 0.0
    denominador = 0.0
    cont = 0
    for i in dic_libros[libro]:
        corr = correlaciones[i]
        if corr is not None and float(libro) in dic_user[i]:
            if corr != 0:
                cont += 1
            numerador += matriz[int(i), libro] * corr
            denominador += abs(corr)
    #Cuantas correlacioens deben ser consideradas como minimo
    if numerador == 0.0 or cont <= 2:
        return 0
    return numerador/denominador

archivo = open("matriz.txt","r")

#CREA MATRIZ DISPERZA (TAMANO,TIPO DE DATO)
matriz = dok_matrix((77805, 271380), dtype=float32)
dic_usuarios = {}#llave usuario, valor lista libros leidos
dic_libros = {}#llave libro, valor lista de usuarios que lo ham leido
inicio_t = time()
for linea in archivo:
    if linea != "\n":
        linea = linea.strip().split(",")
        linea = map(float, linea)
        if linea[0] not in dic_usuarios:
            dic_usuarios[linea[0]] = []
        if linea[1] not in dic_libros:
            dic_libros[linea[1]] = []
        dic_libros[linea[1]].append(linea[0])
        dic_usuarios[linea[0]].append(linea[1])
        matriz[linea[0], linea[1]] = linea[2]
fin_t = time()
tiempo1 = fin_t-inicio_t
archivo_usuarios = open("usuarios.txt", "r")
lista_usuarios = []
for usuarios in archivo_usuarios:
    usuarios = usuarios.strip()
    if usuarios != "":
        usuarios = usuarios.replace('"',"")
        lista_usuarios.append(usuarios)

while True:
    try:
        usuario = raw_input("Ingrese ID de usuario: ")
        indice = lista_usuarios.index(usuario)
        break
    except ValueError:
        print "Usuario invalido, intente nuevamente."
timei4 = time()
ratingsaurio = []
for libro in dic_usuarios[indice]:
    ratingsaurio.append(matriz[indice,libro])
prom_rating_user = sum(ratingsaurio)/len(ratingsaurio)
librosaurio = dic_usuarios[indice]
correlaciones = {}
timef4=time()
tiempo4=timef4 - timei4
timei=time()
for i in range(len(lista_usuarios)):
    try:
        libros = dic_usuarios[i]
        ratingu = []
        for libro in libros:
            ratingu.append(matriz[i, libro])
        prom_rating_u = sum(ratingu)/len(ratingu)
        conjunto = set(librosaurio) & set(libros)
        if conjunto == set([]):
            correla = 0
        else:
            correla = correlacion(prom_rating_user,prom_rating_u,conjunto,indice,i,matriz)
        if i != indice:
            correlaciones[i] = correla
        else:
            correlaciones[i] = None
    except KeyError:
        continue
timef=time()
tiempo2 = timef-timei
rating_ponderado = {}
for libro in dic_libros:
    if libro not in dic_usuarios[indice]:
        rating = ratingponderado(correlaciones, dic_usuarios, matriz, indice, libro, dic_libros) #Excluimos los 0 (no se recomiendan)
        if rating > 0.0:
            rating_ponderado[libro] = rating
sort_ratings = []
for libro in rating_ponderado:
    sort_ratings.append((rating_ponderado[libro],libro))
sort_ratings.sort()
sort_ratings.reverse()
while True:
    cantidad_ratings = input("Ingrese la cantidad de libros a sugerir: ")
    if cantidad_ratings <= len(sort_ratings):
        libros_final = sort_ratings[0:cantidad_ratings]
        break
    print "No es posible entregar esa cantidad de recomendaciones.Intente nuevamente."
timeinicio = time()
archivo_libros = open("BX-Books.csv", "r")
lista_libros = []
archivo_libros.readline()
for linea in archivo_libros:
    linea = linea.strip().split(";")
    for dato in linea:
        if ".MZ" in dato:
            imagen = dato
    libros.append((linea[1],imagen))
datos_tabla = []
for libro in libros_final:
    datos_tabla.append([libros[int(libro[1])][0],libro[0],libros[int(libro[1])][1]])
timefinal = time()
tiempo3 = timefinal-timeinicio
tiempo = tiempo1+tiempo2+tiempo3+tiempo4
print "El tiempo total de recomendacion de libros(Matriz,Correlaciones,Ratings) es de",tiempo,"segundos"
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#HTML-HTML-HTML-HTML-HTML-HTML-HTML-HTML-HTML-HTML-HTML-HTML-HTML-HTML-HTML-HTML-HTML-HTML-HTML-HTML-HTML-HTML-HTML-HTML-HTML-HTML
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
basehtml = '<!doctype html>\n<html>\n<head>\n<link rel="stylesheet" href="w3.css">\n<meta charset="utf-8">\n<title>Libros</title>\n<style>\ntd {\nheight: 160px;\nvertical-align: baseline;\n}\nimg {\nwidth:125px;\nheight:160px;\n}</style>\n</head>\n<body style="background-color:#455a64">\n<header class="w3-blue-grey w3-card-2">\n<div class="w3-container w3-teal">\n<h1>Libros Sugeridos</h1>\n</div>\n</header>\n<br>\n<div class="w3-content w3-container">\n'
print "INICIALIZANDO HTML"
for datos in datos_tabla:
    keyword = 'http://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords='
    titulo = sub('[-!:.,;"?_{}]', '', datos[0])
    titulo = titulo.replace(' ','+')
    keyword+=titulo
    iterando = '<div class="w3-container  w3-padding-8">\n<div class="w3-white"><table class = "w3-table w3-card-8" style="width:100%">\n<tr>\n<td><a href='+keyword+'><img src={0}></a></td>\n<td><h2 class="w3-center"><br>{1}</h2></td>\n<td><h2 style="text-align:right"><br>{2}</h2></td>\n</tr></table></div></div>'
    iterando = iterando.format(datos[2],datos[0].replace('"',''),str(round(datos[1],1)))
    basehtml+=iterando
archivoweb = open("archivoweb.html","w")
archivoweb.write(basehtml)
archivoweb.write('</div>\n</body>\n</html>')
archivoweb.close()
archivo.close()
archivo_usuarios.close()