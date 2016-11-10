def iniciarPlayList(numeroCancion):
    playList={}
    cancionesIntroducidas = 1
    while cancionesIntroducidas <= len(libreria):
        cancionAIntroducir = seleccionaCancionRandom(libreria)
        if cancionAIntroducir not in playList.values():
            playList[cancionesIntroducidas] = cancionAIntroducir
            cancionesIntroducidas += 1
    return playList