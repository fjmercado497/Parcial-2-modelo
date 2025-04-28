import numpy as np
import matplotlib.pyplot as plt

# Parámetros del vehículo
R = 0.1  # Radio de las ruedas (m)
L = 0.5  # Distancia entre ruedas (m)
v_r = 1.0  # Velocidad rueda derecha (m/s)
v_l = 0.5  # Velocidad rueda izquierda (m/s)
dt = 0.1  # Incremento de tiempo (s)
steps = 100  # Cantidad de pasos de simulación

# Posición inicial del vehículo
x, y, theta = 0, 0, 0

# Listas para almacenar posiciones
posiciones_x = [x]
posiciones_y = [y]

# Simulación de movimiento
for _ in range(steps):
    v = (v_r + v_l) / 2  # Velocidad promedio
    omega = (v_r - v_l) / L  # Velocidad angular
    x += v * np.cos(theta) * dt
    y += v * np.sin(theta) * dt
    theta += omega * dt
    posiciones_x.append(x)
    posiciones_y.append(y)

# Gráfico de trayectoria del vehículo
plt.figure(figsize=(8, 6))
plt.plot(posiciones_x, posiciones_y, label='Trayectoria del vehículo')
plt.xlabel('Posición X (m)')
plt.ylabel('Posición Y (m)')
plt.title('Simulación de Movimiento del Vehículo Diferencial')
plt.legend()
plt.grid()
plt.show()