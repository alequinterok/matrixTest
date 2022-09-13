import os

#Modificar la matriz por la que se quiere evaluar
MATRIZ = [ 
         [1, 1, 0, 1, 0],
         [0, 1, 1, 1, 0],
         [1, 0, 1, 0, 1],
         [0, 0, 1, 1, 0],
         [1, 1, 0, 1, 1] ]


def limpiar_pantalla() -> None:
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")


def es_reflexiva() -> bool:
    reflexiva = True
    for i in range (0, len(MATRIZ)):
        if MATRIZ[i][i] == 0:
            reflexiva = False
        i += 1
    
    return reflexiva


def es_simetrica() -> bool:
    simetrica = True
    for j in range (0, len(MATRIZ)):
        for k in range (0, len(MATRIZ)):
            if MATRIZ[j][k] != MATRIZ[k][j]:
                    simetrica = False
            k += 1
        j += 1
        
    return simetrica


def es_antisimetrica() -> bool: 
    antisimetrica = True
    for i in range(len(MATRIZ)):
        for j in range(len(MATRIZ[i])):
            if (i != j and MATRIZ[i][j] == MATRIZ[j][i]):
                antisimetrica = False
    
    return antisimetrica

    
def es_transitiva() -> bool:
    transitiva = True
    for l in range (0, len(MATRIZ)):
        for m in range (0, len(MATRIZ)):
            for n in range (0, len(MATRIZ)):
                if MATRIZ[l][n] == MATRIZ[n][m] == 1 and MATRIZ[l][m] == 0:
                    transitiva = False
                n += 1
            m += 1
        l += 1
    
    return transitiva


def es_de_orden(reflexiva: bool, antisimetrica: bool, transitiva: bool) -> bool:
    relacion_de_orden = False
    if (reflexiva == True and antisimetrica == True and transitiva == True):
        relacion_de_orden = True
    
    return relacion_de_orden


def es_de_equivalencia(reflexiva: bool, simetrica: bool, transitiva: bool) -> bool:
    relacion_de_equivalencia = False
    if (reflexiva == True and simetrica == True and transitiva == True):
        relacion_de_equivalencia = True
    
    return relacion_de_equivalencia
        

def imprimir_matriz() -> None:
    for fila in MATRIZ:
        print(fila)
        

def main():
    
    reflexiva = es_reflexiva()
    antisimetrica = es_antisimetrica()
    simetrica = es_simetrica()
    transitiva = es_transitiva()
    
    relacion_de_orden = es_de_orden(reflexiva, antisimetrica, transitiva)
    relacion_de_equivalencia = es_de_equivalencia(reflexiva, simetrica, transitiva)
    
    limpiar_pantalla()
    
    print("\n\nTest de matrices de adyacencia - Matemática Discreta")
    print("\nEs reflexiva: ", reflexiva)
    print("Es antisimetrica: ", antisimetrica)
    print("Es simetrica: ", simetrica)
    print("Es transitiva: ", transitiva)
    
    
    if relacion_de_orden == True:
        print("\nEs relacion de orden: ", relacion_de_orden)
    
    if relacion_de_equivalencia == True:
        print("\nEs relacion de equivalencia: ", relacion_de_equivalencia)
        
main()    