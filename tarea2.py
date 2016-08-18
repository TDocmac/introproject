def similitud(user,cercano):

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
    print interseccion

similitud(1,2)

