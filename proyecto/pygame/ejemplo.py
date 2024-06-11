import pygame
import sys


def dibujar_tablero(screen):
    tamaño_celda = 100
    color_linea = (0, 0, 0)
    for i in range(4):
        # Dibujar líneas horizontales
        pygame.draw.line(screen, color_linea, (0, i * tamaño_celda), (300, i * tamaño_celda), 2)
        # Dibujar líneas verticales
        pygame.draw.line(screen, color_linea, (i * tamaño_celda, 0), (i * tamaño_celda, 300), 2)

def main():
    pygame.init()
    screen = pygame.display.set_mode((300, 300))
    pygame.display.set_caption("Tablero 3x3")
    screen.fill((255, 255, 255))

    dibujar_tablero(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.flip()

if __name__ == "__main__":
    main()
