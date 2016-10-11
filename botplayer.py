import numpy as np
from random import *

def escoger_movimiento( amenazas ):

    if len(amenazas) > 0:
        riesgocuadrante = amenazas.strip().split(":")
        riesgo = riesgocuadrante[0].strip().split("-")
        cuadrante = riesgocuadrante[1].strip().split("-")

        if len(riesgo) == 1:
            list_x = [-3,0,3]
            movimiento_x = str(choice(list_x))
            if movimiento_x != "0":
                movimiento_y = "0"
            else:
                list_y = [-3,3]
                movimiento_y = str(choice(list_y))
            return movimiento_x + "," + movimiento_y

        elif len(riesgo) > 1:
            if riesgo[1] == "1":
                list_x = [-3,-2,0,2,3]
                movimiento_x = str(choice(list_x))
                if movimiento_x != "0":
                    movimiento_y = "0"
                else:
                    list_y = [-3,-2,2,3]
                    movimiento_y = str(choice(list_y))
                return movimiento_x + "," + movimiento_y
            elif riesgo[1] == "2":
                list_x = [-2,-1,0,1,2]
                movimiento_x = str(choice(list_x))
                if movimiento_x != "0":
                    movimiento_y = "0"
                else:
                    list_y = [-2,-1,1,2]
                    movimiento_y = str(choice(list_y))
                return movimiento_x + "," + movimiento_y
            elif riesgo[1] == "3":
                list_x = [-1,0,1]
                movimiento_x = str(choice(list_x))
                if movimiento_x != "0":
                    movimiento_y = "0"
                else:
                    list_y = [-1,1]
                    movimiento_y = str(choice(list_y))
                return movimiento_x + "," + movimiento_y

    movimiento_x = "1"
    movimiento_y = "0"

    return movimiento_x + "," + movimiento_y


def escoger_disparo( amenazas ):
    riesgocuadrante = amenazas.strip().split(":")
    riesgo = riesgocuadrante[0].strip().split("-")

    if len(riesgo) == 1:
        list_x = [-5,5]
        disparo_x = str(choice(list_x))
        if disparo_x != "0":
            disparo_y = "0"
        else:
            list_y = [-5, 5]
            disp_y = str(choice(list_y))
            disparo_y = disp_y
        return disparo_x + "," + disparo_y

    elif len(riesgo) > 1:
        if riesgo[1] == "1":
            list_x = [-5, -4, -3 ,0, 3, 4, 5]
            disparo_x = str(choice(list_x))
            if disparo_x != "0":
                disparo_y = "0"
            else:
                list_y = [-5,-4,-3, 3, 4, 5]
                disparo_y = str(choice(list_y))
            return disparo_x + "," + disparo_y
        elif riesgo[1] == "2":
            list_x = [-3,-2, -1, 0, 1, 2, 3]
            disparo_x = str(choice(list_x))
            if disparo_x != "0":
                disparo_y = "0"
            else:
                list_y = [-3, -2, -1, 1, 2, 3]
                disparo_y = str(choice(list_y))
            return disparo_x + "," + disparo_y
        elif riesgo[1] == "3":
            list_x = [-2, -1, 0, 1, 2]
            disparo_x = str(choice(list_x))
            if disparo_x != "0":
                disparo_y = "0"
            else:
                list_y = [-2, -1, 1, 2]
                disparo_y = str(choice(list_y))
            return disparo_x + "," + disparo_y

    disparo_x = "0"
    disparo_y = "3"

    return disparo_x + "," + disparo_y
