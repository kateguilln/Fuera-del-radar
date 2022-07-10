#!/usr/bin/python3

# Importación de librerías
import pygame
import random
import os

# Variables globales
velocidad = 3
puntos = 0

# Colores
blanco = (0, 0, 0)
negro = (255, 255, 255)
dorado = (182, 143, 64)
verde = (215, 252, 212)

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
# Imagen del menu
menu = pygame.image.load(carpeta + "/sprites/menu.png").convert()
# Imagen de fondo de las instrucciones y de la pantalla de fin del juego
fondo_de_instrucciones = pygame.image.load(carpeta +
                                           "/sprites/Fondo_Instrucciones"
                                           ".png").convert()


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
                                       "/sprites/obs1.png"
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


# Definición de la clase Boton, la cual se va a utilizar cada vez que se quiera
# crear un botón nuevo. Recibe como argumentos la imagen (puede ser None), una
# tupla (obligatorio) que tiene como primer elemento la posición en x, y un
# segundo elemento que tiene la posición en y, el texto, la fuente para ese
# texto y el color de ese texto.
class Boton():
    def __init__(self, imagen, pos, texto_en, fuente, color_base):
        self.image = imagen
        self.x = pos[0]
        self.y = pos[1]
        self.fuente = fuente
        self.color_base = color_base
        self.texto_en = texto_en
        self.text = self.fuente.render(self.texto_en, True, self.color_base)
        if self.image is None:
            self.image = self.text
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.text_rect = self.text.get_rect(center=(self.x, self.y))

    def actualizar(self, pantalla):  # Muestra los botones en pantalla
        if self.image is not None:
            pantalla.blit(self.image, self.rect)
        pantalla.blit(self.text, self.text_rect)

    def chequar_click(self, posicion):  # Compprueba si el botón fue clickeado
        if (posicion[0] in range(self.rect.left, self.rect.right)
                and posicion[1] in range(self.rect.top, self.rect.bottom)):
            return True
        return False


# Esta función contiene el bucle principal de funcionamiento del juego
def bucle_principal():
    global puntos, velocidad
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
        colisiones = pygame.sprite.spritecollide(nave,
                                                 lista_de_asteroides, True)
        # Al detectar una colision se crea un nuevo asteroide, porque sino van
        # desapareciendo y se reduce la barra de vida un cuarto
        for colision in colisiones:
            tipo = random.randrange(1, 4)
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

            astoroide1 = Asteroide(tipo, linea_x)
            lista_de_asteroides.add(astoroide1)
            sprites.add(astoroide1)
            nave.vida -= 25
            # Si la vida de la nave es 0 o menor se acaba el juego
            if nave.vida <= 0:
                # Se borran todos los asteroides y estrellas que
                # quedan en la pantalla
                for asteroide in lista_de_asteroides:
                    asteroide.kill()
                for asteroide in lista_de_estrellas:
                    asteroide.kill()
                # Se reinician los parametros
                puntos = 0
                velocidad = 3
                puntos = 0
                nave.vida = 100
                # Se crean los asteroides y las estrellas para el siguiente
                # juego
                for asteroides in range(0, 5):
                    tipo = random.randrange(1, 4)
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
                    astoroide1 = Asteroide(tipo, linea)
                    lista_de_asteroides.add(astoroide1)
                    sprites.add(astoroide1)
                for estrella in range(0, 1):
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
                    lista_de_estrellas.add(estrella1)
                    sprites.add(estrella1)
                fin_del_juego()
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
            lista_de_estrellas.add(estrella1)
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


# Asigna la fuente indicada, en el tamaño indicado
def obtener_fuente(tamaño):
    return pygame.font.Font(carpeta + "/sprites/font.ttf", tamaño)


# La opción jugar contiene el bucle que ejecuta el juego como tal
def jugar():
    bucle_principal()


# Muestra las instrucciones del juego
def instrucciones():
    while True:
        posicion_mouse = pygame.mouse.get_pos()

        pantalla.blit(fondo_de_instrucciones, (0, 0))
        texto = obtener_fuente(30).render("Instrucciones", True, negro)
        cuadrado_texto = texto.get_rect(center=(ancho // 2, 50))
        pantalla.blit(texto, cuadrado_texto)
        texto = obtener_fuente(15).render("-Conduce la nave espacial "
                                          "sin chocar", True, negro)
        cuadrado_texto = texto.get_rect(center=(311, 150))
        pantalla.blit(texto, cuadrado_texto)
        texto = obtener_fuente(15).render("-Muevete hacia los lados con las "
                                          "flechas", True, negro)
        cuadrado_texto = texto.get_rect(center=(342, 250))
        pantalla.blit(texto, cuadrado_texto)
        texto = obtener_fuente(15).render("-Obten estrellas para aumentar tu "
                                          "puntaje y acelerar el juego",
                                          True, negro)
        cuadrado_texto = texto.get_rect(center=(500, 350))
        pantalla.blit(texto, cuadrado_texto)

        regresar = Boton(imagen=None, pos=(ancho // 2, 460),
                         texto_en="Regresar", fuente=obtener_fuente(25),
                         color_base=negro)

        regresar.actualizar(pantalla)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if regresar.chequar_click(posicion_mouse):
                    menu_principal()

        pygame.display.update()


# Muestra la pantalla del fin del juego
def fin_del_juego():
    while True:
        posicion_mouse = pygame.mouse.get_pos()

        pantalla.blit(fondo_de_instrucciones, (0, 0))
        texto = obtener_fuente(30).render("Fin del juego", True, negro)
        cuadrado_texto = texto.get_rect(center=(ancho // 2, 260))
        pantalla.blit(texto, cuadrado_texto)

        regresar = Boton(imagen=pygame.image.load(
                         carpeta + "/sprites/Jugar_Rect.png"),
                         pos=(ancho // 2, 460), texto_en="Regresar",
                         fuente=obtener_fuente(25),
                         color_base=negro)

        regresar.actualizar(pantalla)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if regresar.chequar_click(posicion_mouse):
                    menu_principal()

        pygame.display.update()


def menu_principal():
    while True:
        pantalla.blit(menu, (0, 0))

        posicion_mouse = pygame.mouse.get_pos()

        texto = obtener_fuente(65).render("FUERA DEL RADAR", True, dorado)
        cuadrado_texto = texto.get_rect(center=(ancho // 2, 100))

        Boton_jugar = Boton(imagen=pygame.image.load(
                    carpeta + "/sprites/Jugar_Rect.png"),
                    pos=(ancho // 2, 250), texto_en="Jugar",
                    fuente=obtener_fuente(40), color_base=verde)
        Boton_instrucciones = Boton(imagen=pygame.image.load(
                carpeta + "/sprites/INs_Rect.png"),
                pos=(ancho // 2, 400),
                texto_en="Instrucciones", fuente=obtener_fuente(40),
                color_base=verde)
        Boton_salir = Boton(imagen=pygame.image.load(
                carpeta + "/sprites/Salir_Rect.png"),
                pos=(ancho // 2, ancho // 2), texto_en="Salir",
                fuente=obtener_fuente(40), color_base=verde)

        pantalla.blit(texto, cuadrado_texto)

        for boton in [Boton_jugar, Boton_instrucciones, Boton_salir]:
            boton.actualizar(pantalla)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Boton_jugar.chequar_click(posicion_mouse):
                    jugar()
                if Boton_instrucciones.chequar_click(posicion_mouse):
                    instrucciones()
                if Boton_salir.chequar_click(posicion_mouse):
                    pygame.quit()
                    exit()

        pygame.display.update()


menu_principal()  # Se llama a la función que contine el menu
pygame.quit()  # Finalización del juego
