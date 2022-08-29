import numpy as np
from Pila_Secuencial import Pila

class manejadorJuego(object):
    __arreglo_pilas = None
    __numero_discos = None
    __jugada_valida = None
    __cantidad_jugadas = None

    def __init__(self,numero_discos = 5):
        self.__numero_discos = numero_discos
        self.__arreglo_pilas = np.empty(3,dtype=Pila)
        self.__cantidad_jugadas = 0
        for i in range(3):
            pila = Pila(numero_discos)
            self.__arreglo_pilas[i] = pila
        self.inicializar_pila1()
    
    def inicializar_pila1(self):
        disco = self.__numero_discos
        while disco >= 1:
            self.__arreglo_pilas[0].insertar(disco)
            disco-=1
        print('Estado inicial: ')
        print('Pila 1:')
        self.__arreglo_pilas[0].mostrar()
        print('Pila 2 y 3: vacia')
    
    
    def verificar_jugada(self,pila_origen,pila_destino):
        if pila_origen == pila_destino or (pila_origen < 1 or pila_origen > 3) or (pila_destino < 1 or pila_destino > 3):
            print('ERROR: Jugada no valida!')
        else:
            if not self.__arreglo_pilas[pila_origen-1].vacio():

                if self.__arreglo_pilas[pila_destino-1].vacio():
                       self.__arreglo_pilas[pila_destino-1].insertar(int(self.__arreglo_pilas[pila_origen-1].suprimir()))
                       print('Disco movido a la pila {}'.format(pila_destino))
                       self.__cantidad_jugadas +=1
                       self.__jugada_valida = True
                else:
                    disco_pila_origen = int(self.__arreglo_pilas[pila_origen-1].suprimir())
                    disco_pila_destino = int(self.__arreglo_pilas[pila_destino-1].suprimir())
                    print(disco_pila_destino)
                    if disco_pila_origen < disco_pila_destino:
                        self.__arreglo_pilas[pila_destino-1].insertar(disco_pila_destino)
                        self.__arreglo_pilas[pila_destino-1].insertar(disco_pila_origen)
                        print('Disco movido a la pila {}'.format(pila_destino))
                        self.__jugada_valida = True
                        self.__cantidad_jugadas +=1
                    else:
                        #Si no se cumple la condición se vuelve a devolver los discos en las pilas originales
                        self.__arreglo_pilas[pila_destino-1].insertar(disco_pila_destino)
                        self.__arreglo_pilas[pila_origen-1].insertar(disco_pila_origen)
                        print('ERROR: el disco de la pila {} es mas grande que el de la pila {}' .format(pila_origen,pila_destino))
            else:
                print('ERROR: La pila {} está vacia!' .format(pila_origen))
                
    def comenzar_juego(self):
        while not self.__arreglo_pilas[0].vacio() or not self.__arreglo_pilas[2].lleno():
            self.__jugada_valida = False
            while not self.__jugada_valida:
                pila_origen = int(input('Ingrese el numero de pila origen: '))
                pila_destino = int(input('Ingrese el numero de pila destino: '))
                self.verificar_jugada(pila_origen, pila_destino)
        print('Felicitaciones, usted ha ganado el juego con una cantidad de {} jugadas' .format(self.__cantidad_jugadas))
        print('El numero minimo de jugadas que se pudo haber relizado es: {}' .format((2**self.__numero_discos)-1))
        print('Estado final pila 3:')
        self.__arreglo_pilas[2].mostrar()
        print('Pila 1 y 2 vacia')