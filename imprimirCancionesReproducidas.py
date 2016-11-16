def imprimirCancionesReproducidas(playList):
    print ("La lista de música se ha reproducido en el siguiente orden: ")
    numeroCancion=1
    while numeroCancion < len(playList):
        for valor in playList:
            if valor==numeroCancion:
                print (valor, playList[valor])
                numeroCancion+=1