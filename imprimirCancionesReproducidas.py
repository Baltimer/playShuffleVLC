#Esta funcion coge una libreria en la cual hay valores del 1 a x desordenados
#y tiene que imprimirlos por pantalla de forma ordenada:


def imprimirCancionesReproducidas(playList):
    print ("La lista de música se ha reproducido en el siguiente orden: ")
    numeroCancion=1
    while numeroCancion < len(playList):
        for valor in playList:
            if valor==numeroCancion:
                print (valor, playList[valor])
                numeroCancion+=1


#CASOS TEST#
test = {2: "soy la cancion numero 2",
        1: "soy la cancion numero 1",
        3: "soy la cancion numero 3"
        }
imprimirCancionesReproducidas(test)
###==>  La lista de música se ha reproducido en el siguiente orden: 
#       1 soy la cancion numero 1
#       2 soy la cancion numero 2
#       3 soy la cancion numero 3