import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import cumulative_trapezoid

from splines import (
    t_spline,
    ax_spline,
    ay_spline
)

# -----------------------------
# REMOVER BIAS
# -----------------------------

ax = ax_spline - np.mean(ax_spline)
ay = ay_spline - np.mean(ay_spline)

# -----------------------------
# INTEGRAÇÃO 1
# aceleração -> velocidade
# -----------------------------

vx = cumulative_trapezoid(
    ax,
    t_spline,
    initial=0
)

vy = cumulative_trapezoid(
    ay,
    t_spline,
    initial=0
)

# -----------------------------
# INTEGRAÇÃO 2
# velocidade -> posição
# -----------------------------

x = cumulative_trapezoid(
    vx,
    t_spline,
    initial=0
)

y = cumulative_trapezoid(
    vy,
    t_spline,
    initial=0
)

# centralizar
x = x - x[0]
y = y - y[0]

# -----------------------------
# GRÁFICOS
# -----------------------------

if __name__ == "__main__":

    plt.figure(figsize=(8,5))
    plt.plot(t_spline, vx, label="vx")
    plt.plot(t_spline, vy, label="vy")
    plt.title("Velocidade integrada")
    plt.xlabel("Tempo")
    plt.ylabel("m/s")
    plt.legend()
    plt.grid()

    plt.figure(figsize=(7,7))
    plt.plot(
        x,
        y,
        label="Trajetória IMU"
    )

    plt.title("Trajetória estimada pela IMU")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.axis("equal")
    plt.legend()
    plt.grid()

    plt.show()