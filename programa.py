#!/usr/bin/python3

# Importación de librerías
import pygame
import random
import os

# Variables globales
velocidad = 3
puntos = 0

reloj = pygame.time.Clock()  # Rastrer el tiempo
pygame.init()  # Inicialización del juego
# Ruta de la carpeta de descarga
carpeta = os.path.dirname(os.path.realpath(__file__))

# Pantalla
ancho = 1075
altura = 605
tamaño = (ancho, altura)
pygame.display.set_mode((ancho, altura))  # Tamaño de la pantalla
pygame.display.set_caption("Fuera del Radar")  # Nombre del juego
pantalla = pygame.display.get_surface()
# Cargar fondo
fondo = pygame.image.load(carpeta + "/sprites/fondo.png").convert()


# Definición de función que se encarga de mostrar el texto en la pantalla
def texto_en_pantalla(superficie, texto, tamaño, x, y):
    # Fuente para texto en pantalla
    fuente = pygame.font.SysFont("Lucida Console", 20)
    # Asignación de fuente y color al texto
    superficie_texto = fuente.render(texto, True, (255, 255, 255))
    # Cuadrado de pixeles del texto
    cuadrado_texto = superficie_texto.get_rect()
    # Posicionamiento del texto
    cuadrado_texto.midtop = (x, y)
    # Mostrar el texto en pantalla
    superficie.blit(superficie_texto, cuadrado_texto)


# Definición de la función "dibujar_vida_nave", que se encarga de dibujar
# la barra de vida de la nave
def dibujar_vida_nave(pantalla, x, y, porcentaje):
    Largo_barra = 100
    Altura_barra = 10
# Definición de una variable que indica cuanta vida tiene la nave
    Cantidad_vida = int((porcentaje / 100) * Largo_barra)
# Definición de los bordes de la barra de vida, x y y representan la posicion
# la pantalla
    Bordes = pygame.Rect(x, y, Largo_barra, Altura_barra)
# Definición de la barra de vida que disminuye al chocar con los asteroides
    Cantidad_vida = pygame.Rect(x, y, Cantidad_vida, Altura_barra)
# Se dibujan los bordes y la barra de vida en la pantalla
    pygame.draw.rect(pantalla, (26, 182, 170), Cantidad_vida)
    pygame.draw.rect(pantalla, (255, 255, 255), Bordes, 2)


# Clase para definir la nave
class Nave(pygame.sprite.Sprite):
    def __init__(self):  # Constructor
        super().__init__()
# Definición de la imagen (
        self.image = pygame.image.load(carpeta +
                                       "/sprites/nave.png").convert()
# Comando para eliminar fondo negro de la imagen
        self.image.set_colorkey((0, 0, 0))
# Obtener el cuadrado alrededor de la imagen
        self.rect = self.image.get_rect()
# Ubicación inicial de la nave respecto al ancho, en este caso a la mitad
        self.rect.centerx = ancho // 2
# Ubicación inicial de la nave respecto a la altura
        self.rect.bottom = altura - 10
# Se define la componente horizontal de la velocidad
        self.speedx = 0
# Se define el nivel inicial de "salud"
        self.vida = 100

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
# Para que la nave no se salga de los margenes:
        if self.rect.right > 740:
            self.rect.right = 740
        elif self.rect.left < 336:
            self.rect.left = 336


# Definición de los sprites en la clase Group()
sprites = pygame.sprite.Group()
# Asigne la clase Nave, a la variable nave
nave = Nave()
# Agregar la nave a los "sprites" de la clase Group
sprites.add(nave)


# Clase para definir los asteroides
class Asteroide(pygame.sprite.Sprite):
    def __init__(self, tipo, linea):
        super().__init__()

        global velocidad

        self.tipo = tipo
        self.linea = linea
# Definición de la imagen
        self.image = pygame.image.load(carpeta +
                                       "/sprites/obs4.png"
                                       ).convert()
# Comando para eliminar fondo negro de la imagen
        self.image.set_colorkey((0, 0, 0))
# Obtener el cuadrado alrededor de la imagen
        self.rect = self.image.get_rect()
# Definir ubicación en x
        self.rect.x = self.linea
# Definir ubicación en y
        self.rect.y = -100
# Definir velocidad
        self.velocidad = velocidad

# Definición de la funcion "movimiento_frente" que se encarga de que el
# asteroide se mueva hacia abajo y de que vuelva a aparecer arriba cuando salga
# de la pantalla

    def movimiento_frente(self):
        self.rect.y += self.velocidad
        if self.rect.top > altura + 10:
            linea_asteroide = random.randrange(1, 4)
            linea = 0
            if linea_asteroide == 1:
                linea = 370
            elif linea_asteroide == 2:
                linea = 470
            elif linea_asteroide == 3:
                linea = 570
            elif linea_asteroide == 4:
                linea = 670

            self.rect.x = linea
            self.rect.y = -100
            self.velocidad = velocidad


# Definición de la lista de asteroides en la clase Group()
lista_de_asteroides = pygame.sprite.Group()


# Clase para definir las estrellas
class Estrellas(pygame.sprite.Sprite):

    def __init__(self, linea):
        super().__init__()

        global velocidad

        self.linea = linea
# Definición de la imagen
        self.image = pygame.image.load(carpeta +
                                       "/sprites/estrella.png").convert()
# Comando para eliminar fondo negro de la imagen
        self.image.set_colorkey((0, 0, 0))
# Obtener el cuadrado alrededor de la imagen
        self.rect = self.image.get_rect()
# Definir ubicación en x
        self.rect.x = self.linea
# Definir velocidad
        self.velocidad = velocidad

# Definición de la funcion "movimiento_frente" que se encarga de las estrellas
# se muevan hacia abajo y de que vuelva a aparecer arriba cuando salga
# de la pantalla
    def movimiento_frente(self):
        self.rect.y += self.velocidad
# Parte de la funcion que hace que vuelvan a aparecer los asteroides
# Esta parte se usa varias veces por lo que seria mejor volverlo una funcion
        if self.rect.top > altura + 10:
            linea_estrella = random.randrange(1, 4)
            linea = 0
            if linea_estrella == 1:
                linea = 360
            elif linea_estrella == 2:
                linea = 460
            elif linea_estrella == 3:
                linea = 560
            elif linea_estrella == 4:
                linea = 660

            self.rect.x = linea
            self.rect.y = -100
            self.velocidad = velocidad


# Definición de la lista de estrellas en la clase Group()
lista_de_estrellas = pygame.sprite.Group()


# Parte del codigo que crea los asteroides por primera vez

for asteroides in range(0, 5):
    # Se elige el tipo de asteroide, esto aun NO hace nada
    tipo = random.randrange(1, 4)
    # Se elige la linea por la que ira de asteroide, esto aun NO hace nada
    linea_asteroide = random.randrange(1, 4)
    linea = 0
    if linea_asteroide == 1:
        linea = 360
    elif linea_asteroide == 2:
        linea = 460
    elif linea_asteroide == 3:
        linea = 560
    elif linea_asteroide == 4:
        linea = 660

    # Se crea un asteroide que va por la linea_x y del tipo tipo_asteroide
    astoroide1 = Asteroide(tipo, linea)
    lista_de_asteroides.add(astoroide1)  # Agregar el astoroide1 a la lista
    sprites.add(astoroide1)  # Agregar el astoroide1 a los sprites

for estrella in range(0, 1):
    # Se elige la linea por la que ira de asteroide, esto aun NO hace nada
    linea_estrella = random.randrange(1, 4)
    linea = 0
    if linea_estrella == 1:
        linea = 360
    elif linea_estrella == 2:
        linea = 460
    elif linea_estrella == 3:
        linea = 560
    elif linea_estrella == 4:
        linea = 660
    # Se crea un asteroide que va por la linea_x y del tipo tipo_asteroide
    estrella1 = Estrellas(linea)
    lista_de_estrellas.add(estrella1)  # Agregar el astoroide1 a la lista
    sprites.add(estrella1)  # Agregar el astoroide1 a los sprites

# Bucle de ejecución del juego
while True:
    reloj.tick(80)  # Velocidad de movimiento de la nave en fps
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            exit()
# Se les da movimiento a los asteroides
    for asteroide in lista_de_asteroides:
        asteroide.movimiento_frente()
# Se les da movimiento a las estrellas
    for estrella in lista_de_estrellas:
        estrella.movimiento_frente()
# Actualice los sprites de la clase Group
    sprites.update()
# Se verifican las colisiones entre los asteroides y la nave
    colisiones = pygame.sprite.spritecollide(nave, lista_de_asteroides, True)
    # Al detectar una colision se crea un nuevo asteroide, porque sino van
    # desapareciendo y se reduce la barra de vida un cuarto
    for colision in colisiones:
        linea_asteroide = random.randrange(1, 4)
        linea_x = 0
        if linea_asteroide == 1:
            linea_x = 360
        elif linea_asteroide == 2:
            linea_x = 460
        elif linea_asteroide == 3:
            linea_x = 560
        elif linea_asteroide == 4:
            linea_x = 660

        astoroide1 = Asteroide(tipo, linea)
        lista_de_asteroides.add(astoroide1)  # Agregar el astoroide1 a la lista
        sprites.add(astoroide1)
        nave.vida -= 25
        # Si la vida de la nave es 0 o menor se acaba el juego
        if nave.vida <= 0:
            exit()
# Se verifican las colisiones entre los asteroides y la nave
    puntaje = pygame.sprite.spritecollide(nave, lista_de_estrellas, True)
    # Al detectar una colision se crea un nuevo asteroide, porque sino van
    # desapareciendo y se reduce la barra de vida un cuarto
    for punto in puntaje:
        linea_estrella = random.randrange(1, 4)
        linea = 0
        if linea_estrella == 1:
            linea = 360
        elif linea_estrella == 2:
            linea = 460
        elif linea_estrella == 3:
            linea = 560
        elif linea_estrella == 4:
            linea = 660

        estrella1 = Estrellas(linea)
        lista_de_estrellas.add(estrella1)  # Agregar el astoroide1 a la lista
        sprites.add(estrella1)
        puntos += 1
        velocidad += 1

# Agrego el fondo de pantalla y agregue los "sprites"
    pantalla.blit(fondo, [0, 0])
    sprites.draw(pantalla)

    dibujar_vida_nave(pantalla, 5, 5, nave.vida)
# Marcador
    texto_en_pantalla(pantalla, 'Marcador: ' + str(puntos), 25, 73, 17)
# Muestre lo anterior en pantalla
    pygame.display.flip()

pygame.quit()  # Finalización del juego
