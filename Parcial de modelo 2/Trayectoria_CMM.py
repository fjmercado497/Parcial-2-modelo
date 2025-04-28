import pygame
import math

# Inicializa Pygame
pygame.init()

# Configuración de la ventana
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simulación de Vehículo Diferencial")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Parámetros del vehículo
R = 0.1  # Radio de las ruedas (m)
L = 0.5  # Distancia entre ruedas (m)
v_r = 0.1 # Velocidad rueda derecha (m/s)
v_l = 0.5  # Velocidad rueda izquierda (m/s)
dt = 0.1  # Incremento de tiempo (s)

# Escala para ajustar las dimensiones a píxeles
SCALE = 100  # 1 metro = 100 píxeles

# Posición inicial del vehículo
x, y = WIDTH // 2, HEIGHT // 2  # Centro de la pantalla
theta = 0  # Ángulo inicial en radianes

# Reloj para controlar la velocidad de la simulación
clock = pygame.time.Clock()

# Listas para almacenar la trayectoria
trajectory = []

# Función para actualizar la posición del vehículo
def update_position(x, y, theta, v_r, v_l, dt):
    v = (v_r + v_l) / 2  # Velocidad promedio
    omega = (v_r - v_l) / L  # Velocidad angular
    x += v * math.cos(theta) * dt * SCALE
    y -= v * math.sin(theta) * dt * SCALE  # Nota: eje Y invertido en Pygame
    theta += omega * dt
    return x, y, theta

# Bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Actualiza la posición del vehículo
    x, y, theta = update_position(x, y, theta, v_r, v_l, dt)

    # Guarda la posición en la trayectoria
    trajectory.append((x, y))

    # Dibuja en la pantalla
    screen.fill(WHITE)  # Limpia la pantalla
    for i in range(1, len(trajectory)):
        pygame.draw.line(screen, BLUE, trajectory[i-1], trajectory[i], 2)  # Traza la trayectoria
    pygame.draw.circle(screen, RED, (int(x), int(y)), 5)  # Dibuja el vehículo como un punto rojo

    # Actualiza la pantalla
    pygame.display.flip()

    # Controla la velocidad de la simulación (10 FPS)
    clock.tick(10)

# Salir de Pygame
pygame.quit()