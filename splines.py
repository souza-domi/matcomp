

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

from leitura import t
from graficoSuav import ax_suave, ay_suave

# -----------------------------
# ORGANIZAÇÃO DOS DADOS
# -----------------------------

t_array = np.array(t)
ax_array = np.array(ax_suave)
ay_array = np.array(ay_suave)

# ordenar pelo tempo
ordem = np.argsort(t_array)

t_ord = t_array[ordem]
ax_ord = ax_array[ordem]
ay_ord = ay_array[ordem]

# remover tempos repetidos
t_spline_base, indices = np.unique(
    t_ord,
    return_index=True
)

ax_spline_base = ax_ord[indices]
ay_spline_base = ay_ord[indices]

# -----------------------------
# SPLINES CÚBICAS
# -----------------------------

spline_ax = CubicSpline(
    t_spline_base,
    ax_spline_base
)

spline_ay = CubicSpline(
    t_spline_base,
    ay_spline_base
)

# tempo mais denso para visualizar a spline
t_spline = np.linspace(
    t_spline_base.min(),
    t_spline_base.max(),
    5000
)

ax_spline = spline_ax(t_spline)
ay_spline = spline_ay(t_spline)

# -----------------------------
# GRÁFICOS
# -----------------------------

def plot_splines(**kwargs):
    ''' Plota as splines cúbicas para ax e ay. '''
    plt.figure(figsize=(8,5))

    plt.plot(
    t_spline_base,
    ax_spline_base,
    label="ax suavizado",
    alpha=0.5
    )

    plt.plot(
    t_spline,
    ax_spline,
    label="Spline cúbica ax"
    )

    plt.title("Spline cúbica da aceleração X")
    plt.xlabel("Tempo")
    plt.ylabel("ax")

    plt.legend()
    plt.grid()

    plt.figure(figsize=(8,5))

    plt.plot(
    t_spline_base,
    ay_spline_base,
    label="ay suavizado",
    alpha=0.5
    )

    plt.plot(
    t_spline,
    ay_spline,
    label="Spline cúbica ay"
    )

    plt.title("Spline cúbica da aceleração Y")
    plt.xlabel("Tempo")
    plt.ylabel("ay")

if __name__ == "__main__":
        plot_splines()
        plt.legend()
        plt.grid()
        plt.show()