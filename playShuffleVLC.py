
## UTILIDADES DE DEPURACION ## 


def checkSeleccionaCancionRandom(cancion, libreria):

def checkPlaySuffle(playList):

## RUTINAS DE UTILIDADES ## 


def seleccionaCancionRandom(libreria):
    import random
    assert isinstance(libreria, dict), "no es una libreria"
    longitudLibreriaInicial = len(libreria)
    tituloCancion = random.choice(list(libreria.keys()))


    assert tituloCancion in libreria, "titulo no esta en la libreria"
    assert longitudLibreriaInicial == len(libreria), "libreria modificada"

    return tituloCancion


def iniciarPlayList(numeroCancion):
    playList={}
    cancionesIntroducidas = 1
    while cancionesIntroducidas <= len(libreria):
        cancionAIntroducir = seleccionaCancionRandom(libreria)
        if cancionAIntroducir not in playList:
            playList[cancionesIntroducidas] = cancionAIntroducir
            cancionesIntroducidas += 1
    return playList


def imprimirCancionesReproducidas(playList):
    for k,v in playList.items():
        print ("%s -> %s" %(k,v))


def lanzarVLC(libreria, playList):

    import subprocess
    import shlex
    import os

    linuxPathVLC = "/usr/bin/vlc"
    lineaComandoVLC = linuxPathVLC
    separador = " "

    for numeroCancion in sorted(playList.keys()):
        tituloCancion = playList[numeroCancion]
        try:
            rutaAccesoFichero = libreria[tituloCancion]["location"]
        except KeyError:
            print("la cancion " + str(tituloCancion) + " no se encuentra en la biblioteca")
        else:
            if os.path.exists(str(rutaAccesoFichero)):
                lineaComandoVLC = lineaComandoVLC + separador + str(rutaAccesoFichero)
            else:
                pass

    # Popen necesita una lista de string
    args = shlex.split(lineaComandoVLC)

    try:
        procesoVLC = subprocess.Popen(args)
        # procesoVLC = subprocess.Popen(["/usr/bin/vlc", "California_Uber_Alles.mp3", "Seattle_Party.flac"])
    except OSError:
        print("el fichero no existe")
    except ValueError:
        print("argumentos invalidos")
    else:
        print("lanzando VLC con lista aleatoria")


## FUNCION PRINCIPAL ## 


def playSuffle(libreria, playList):

    genera la lista aleatoria de canciones a partir de la libreria



## PROGRAMA PRINCIPAL ##

playList = {}

libreria = {"California_Uber_Alles.mp3": 
                {"track-number": 3, "artist": "Dead Kennedys", "album": "Dead Kennedys", "location": "./biblioteca/California_Uber_Alles.mp3"},
            "Seattle_Party": 
                {"track-number": 1, "artist": "Chastity Belt", "album": "No regrets", "location": "./biblioteca/Seattle_Party.flac"},
            "King_Kunta":
                {"track-number": 3, "artist": "Kendrick Lamar", "album": "To Pimp A Butterfly", "location": "./biblioteca/King_Kunta.mp3"}   
            }

# for i in range(1,1001):
assert playSuffle(libreria, playList)

# libreriaLista = []
# assert playSuffle(libreriaLista)

imprimirCancionesReproducidas(playList)

lanzarVLC(libreria, playList)