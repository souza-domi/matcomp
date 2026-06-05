import numpy as np
import matplotlib.pyplot as plt

from trajetoria import cx_interp, cy_interp
from leitura import t

# -----------------------------
# VELOCIDADE A PARTIR DO VI
# -----------------------------

vx_vi = np.gradient(cx_interp, t)
vy_vi = np.gradient(cy_interp, t)

# -----------------------------
# ACELERAÇÃO A PARTIR DO VI
# -----------------------------

ax_vi = np.gradient(vx_vi, t)
ay_vi = np.gradient(vy_vi, t)

# -----------------------------
# GRÁFICOS
# -----------------------------

if __name__ == "__main__":

    # VELOCIDADE
    plt.figure(figsize=(8,5))
    plt.plot(t, vx_vi, label="vx VI")
    plt.title("Velocidade X do VI")
    plt.xlabel("Tempo")
    plt.ylabel("vx")
    plt.legend()
    plt.grid()

    plt.figure(figsize=(8,5))
    plt.plot(t, vy_vi, label="vy VI")
    plt.title("Velocidade Y do VI")
    plt.xlabel("Tempo")
    plt.ylabel("vy")
    plt.legend()
    plt.grid()

    # ACELERAÇÃO
    plt.figure(figsize=(8,5))
    plt.plot(t, ax_vi, label="ax calculado pelo VI")
    plt.title("Aceleração X calculada a partir da trajetória VI")
    plt.xlabel("Tempo")
    plt.ylabel("ax")
    plt.legend()
    plt.grid()

    plt.figure(figsize=(8,5))
    plt.plot(t, ay_vi, label="ay calculado pelo VI")
    plt.title("Aceleração Y calculada a partir da trajetória VI")
    plt.xlabel("Tempo")
    plt.ylabel("ay")
    plt.legend()
    plt.grid()

    plt.show()