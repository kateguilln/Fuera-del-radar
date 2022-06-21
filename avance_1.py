#!/usr/bin/python3

# Importación de librerías
import pygame
import os

# Colores
celeste = (31, 206, 189)
negro = (0, 0, 0)
blanco = (255, 255, 255)
verde = (0, 255, 0)

reloj = pygame.time.Clock()
pygame.init()  # Inicialización del juego
# Ruta de la carpeta de descarga
carpeta = os.path.dirname(os.path.realpath(__file__))

# Pantalla
# Hay un error con la pantalla completa, no se muestra la imagen correctamente
# solo en los márgenes establecidos.
ancho = 800
altura = 500
tamaño = (ancho, altura)
pygame.display.set_mode((ancho, altura))  # Tamaño de la pantalla
pygame.display.set_caption("Fuera del Radar")  # Nombre del juego
pantalla = pygame.display.get_surface()
# Cargar fondo.
fondo = pygame.image.load(carpeta + "/sprites/background.png").convert()


# Clase para definir la nave
class Nave(pygame.sprite.Sprite):
    def __init__(self):  # Constructor
        super().__init__()
# Definición de la imagen (HAY QUE CAMBIARLA)
        self.image = pygame.image.load(carpeta +
                                       "/sprites/player.png").convert()
# Comando para eliminar fondo negro de la imagen
        self.image.set_colorkey(negro)
# Obtener el cuadrado alrededor de la imagen
        self.rect = self.image.get_rect()
# Ubicación inicial de la nave respecto al ancho, en este caso a la mitad
        self.rect.centerx = ancho // 2
# Ubicación inicial de la nave respecto a la altura
        self.rect.bottom = altura - 10
# Se define la componente horizontal de la velocidad
        self.speedx = 0

# Definición de la función "update", que se encarga de actualizar el
# movimiento de la nave
    def update(self):
        self.speedx = 0
# Lista que almacena las teclas presionadas
        estado_de_las_teclas = pygame.key.get_pressed()
# Flecha izquierda, muevase con una velocidad de 5 hacia la izquierda
        if estado_de_las_teclas[pygame.K_LEFT]:
            self.speedx = -5
# Flecha derecha, muevase con una velocidad de 5 hacia la derecha:
        elif estado_de_las_teclas[pygame.K_RIGHT]:
            self.speedx = 5
# A la posición de la nave, vaya sumándole la velocidad
        self.rect.x += self.speedx
# Para que la nave no se salga de la pantalla:
        if self.rect.right > ancho:
            self.rect.right = ancho
        elif self.rect.left < 0:
            self.rect.left = 0


# Definición de los sprites en la clase Group()
sprites = pygame.sprite.Group()
# Asigne la clase Nave, a la variable nave
nave = Nave()
# Agregue nave a los "sprites" de la clase Group
sprites.add(nave)

# Bucle de ejecución del juego
while True:
    reloj.tick(80)  # Velocidad de movimiento de la nave en fps
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            exit()
# Actualice los sprites de la clase Group
    sprites.update()
# Agrego el fondo de pantalla y agregue los "sprites"
    pantalla.blit(fondo, [0, 0])
    sprites.draw(pantalla)
# Muestre lo anterior en pantalla
    pygame.display.flip()

pygame.quit()  # Finalización del juego
