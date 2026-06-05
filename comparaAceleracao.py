'''compara os graficos de aceleração do IMU e do VI, usando o mesmo intervalo de tempo para ambos
o do VI é calculado usando a segunda derivada.'''

import numpy as np
import matplotlib.pyplot as plt

from leitura import t
from graficoSuav import ax_suave, ay_suave
from aceleracaoVI import ax_vi, ay_vi

# -----------------------------
# CONVERTER IMU DE g PARA m/s²
# -----------------------------

g = 9.80665

ax_imu = ax_suave * g
ay_imu = ay_suave * g

# -----------------------------
# GRÁFICOS
# -----------------------------

plt.figure(figsize=(8,5))

plt.plot(t, ax_imu, label="IMU ax em m/s²")
plt.plot(t, ax_vi, label="VI ax calculado")

plt.title("Comparação da aceleração X")
plt.xlabel("Tempo")
plt.ylabel("Aceleração X (m/s²)")

plt.legend()
plt.grid()


plt.figure(figsize=(8,5))

plt.plot(t, ay_imu, label="IMU ay em m/s²")
plt.plot(t, ay_vi, label="VI ay calculado")

plt.title("Comparação da aceleração Y")
plt.xlabel("Tempo")
plt.ylabel("Aceleração Y (m/s²)")

plt.legend()
plt.grid()

plt.show()