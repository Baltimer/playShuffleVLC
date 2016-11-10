def seleccionaCancionRandom(libreria):
    import random
    assert isinstance(libreria, dict), "no es una libreria"
    longitudLibreriaInicial = len(libreria)
    tituloCancion = random.choice(list(libreria.keys()))


    assert tituloCancion in libreria, "titulo no esta en la libreria"
    assert longitudLibreriaInicial == len(libreria), "libreria modificada"

    return tituloCancion

## CASOS TEST ##
libreria = {"Titulo": "ok", "Titulo2": "ok2", "Titulo3": "ok3"}
for i in range(1,21):
    print (seleccionaCancionRandom(libreria))