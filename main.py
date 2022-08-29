from manejadorJuego import manejadorJuego

if __name__ == '__main__':
    cant_discos = int(input('Ingrese el numero de discos para iniciar el juego: '))
    objJuego = manejadorJuego(cant_discos)
    objJuego.comenzar_juego()
    