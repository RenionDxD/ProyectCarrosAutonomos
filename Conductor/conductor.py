import pygame
import math
from pygame.locals import *
from SuperAsisstent import draw_circle

# Inicializar pygame
pygame.init()

# Definir el tamaño de la pantalla
width, height = 500, 400
screen = pygame.display.set_mode((width, height))

# Establecer el color de fondo
background_color = (0, 0, 0)  # Blanco
screen.fill(background_color)

# Definir el color del volante y las líneas
wheel_color = (0, 100, 0)  # Negro
line_color = (200, 200, 200)  # Gris claro

# Definir las coordenadas y el radio del volante
wheel_x = width // 2
wheel_y = height // 2
wheel_radius = 150

# Definir el número de divisiones del volante
num_divisions = 36

# Bucle principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # Obtener la posición actual del cursor del mouse
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Calcular la diferencia entre la posición del cursor y el centro del volante
    diff_x = mouse_x - wheel_x
    diff_y = mouse_y - wheel_y

    # Calcular el ángulo de rotación basado en la diferencia entre el cursor y el centro del volante
    angle = math.atan2(diff_y, diff_x)

    # Convertir el ángulo a grados y ajustarlo al rango de 0 a 360
    degrees = math.degrees(angle) % 360
    print(degrees)
    
    # Dibujar el fondo y el volante en la pantalla
    screen.fill(background_color)
    pygame.draw.circle(screen, wheel_color, (wheel_x, wheel_y), wheel_radius)
 

    # Dibujar líneas y números de grados
    for i in range(num_divisions):
        # Calcular el ángulo de la línea actual
        line_angle = math.radians((360 / num_divisions) * i)  # Restamos 90 grados
        
        # Calcular las coordenadas de los extremos de la línea
        start_x = wheel_x + int(math.cos(line_angle) * wheel_radius)
        start_y = wheel_y + int(math.sin(line_angle) * wheel_radius)
        end_x = wheel_x + int(math.cos(line_angle) * (wheel_radius - 10))
        end_y = wheel_y + int(math.sin(line_angle) * (wheel_radius - 10))
        
        # Dibujar la línea
        pygame.draw.line(screen, line_color, (start_x, start_y), (end_x, end_y), 2)

        # Dibujar el número de grados
        font = pygame.font.Font(None, 12)
        text = font.render(str((360 // num_divisions) * i), True, line_color)
        text_rect = text.get_rect()

        # Posicionar el texto fuera del círculo
        text_radius = wheel_radius + 15
        text_x = wheel_x + int(math.cos(line_angle) * text_radius)
        text_y = wheel_y + int(math.sin(line_angle) * text_radius)
        text_rect.center = (text_x, text_y)

        screen.blit(text, text_rect)

    # Dibujar una línea para indicar la posición del cursor
    cursor_length = wheel_radius
    cursor_x = wheel_x + int(math.cos(angle) * cursor_length)
    cursor_y = wheel_y + int(math.sin(angle) * cursor_length)
    pygame.draw.line(screen, (255, 0, 0), (wheel_x, wheel_y), (cursor_x, cursor_y), 2)
    pygame.draw.circle(screen, (180, 180, 180), (wheel_x, wheel_y), wheel_radius-20)
    draw_circle(screen, (50, 100, 50), (wheel_x, wheel_y), wheel_radius-30)
    #pygame.draw.circle(screen, (50, 100, 50), (wheel_x, wheel_y), wheel_radius-20)
    
    # Actualizar la pantalla
    pygame.display.flip()

# Salir de pygame
pygame.quit()
