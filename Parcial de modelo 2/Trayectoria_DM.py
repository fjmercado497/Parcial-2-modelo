import matplotlib.pyplot as plt
import numpy as np

# Parámetros del vehículo
R = 0.1  # Radio de las ruedas (m)
L = 0.5  # Distancia entre ruedas (m)
m = 10 # Masa del vehículo (kg)
I = 0.5  # Momento de inercia (kg·m²)
F_r = 2.0  # Fuerza de la rueda derecha (N)
F_l = 2.0  # Fuerza de la rueda izquierda (N)
dt = 0.1  # Incremento de tiempo (s)
steps = 100  # Número de pasos de simulación

# Inicialización de variables
x, y, theta = 0, 0, 0  # Posición y orientación iniciales
v = 0  # Velocidad lineal inicial
omega = 0  # Velocidad angular inicial

# Listas para almacenar la trayectoria y orientación
posiciones_x = []
posiciones_y = []
orientaciones = []

# Simulación del movimiento dinámico
for _ in range(steps):
    # Cálculo de fuerzas y torques
    F_total = (F_r + F_l) / 2  # Fuerza promedio
    tau = R * (F_r - F_l)  # Torque neto

    # Aceleraciones
    a = F_total / m  # Aceleración lineal
    alpha = tau / I  # Aceleración angular

    # Actualización de velocidades
    v += a * dt
    omega += alpha * dt

    # Actualización de posición
    x += v * np.cos(theta) * dt
    y += v * np.sin(theta) * dt
    theta += omega * dt

    # Almacenar datos
    posiciones_x.append(x)
    posiciones_y.append(y)
    orientaciones.append(theta)

# Crear el gráfico
fig, ax = plt.subplots(figsize=(8, 8))
ax.plot(posiciones_x, posiciones_y, label='Trayectoria', color='blue')

# Agregar vectores de orientación
for i in range(0, steps, 10):  # Cada 10 pasos
    dx = 0.2 * np.cos(orientaciones[i])  # Longitud del vector de dirección
    dy = 0.2 * np.sin(orientaciones[i])
    ax.arrow(posiciones_x[i], posiciones_y[i], dx, dy, head_width=0.05, color='red')

# Etiquetas y diseño
ax.set_title("Movimiento Dinámico del Vehículo")
ax.set_xlabel("Posición X (m)")
ax.set_ylabel("Posición Y (m)")
ax.legend()
ax.grid()
plt.show()