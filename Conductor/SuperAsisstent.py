import pygame
import math

def draw_circle(screen, color, position, radius):
    

    pygame.draw.circle(screen, color, position, radius)

    # Calcular la posición de los ojos
    eye_radius = radius // 5
    eye_x_offset = radius // 3

    # Calcular la posición del primer ojo
    eye1_x = position[0] - eye_x_offset
    eye1_y = position[1]

    # Calcular la posición del segundo ojo
    eye2_x = position[0] + eye_x_offset
    eye2_y = position[1]

    # Dibujar los ojos (círculos blancos)
    pygame.draw.circle(screen, (255, 255, 255), (eye1_x-10, eye1_y), eye_radius+10)
    pygame.draw.circle(screen, (255, 255, 255), (eye2_x+10, eye2_y), eye_radius+10)
