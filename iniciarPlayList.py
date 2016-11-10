def iniciarPlayList(numeroCancion):
    playList=[]
    cancionesIntroducidas = 0
    while cancionesIntroducidas <= len(libreria):
        cancionAIntroducir = seleccionaCancionRandom(libreria)
        if cancionAIntroducir not in playList:
            playList.append(cancionAIntroducir)
            cancionesIntroducidas += 1