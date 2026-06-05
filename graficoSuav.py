#GRAFICO DA ACELERACAO VS TEMPO 
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter

from leitura import t
from referencialGlobal import ax_global, ay_global

# -----------------------------
# Savitzky-Golay
# -----------------------------

janela = 7
grau = 3

ax_suave = savgol_filter(ax_global, janela, grau)
ay_suave = savgol_filter(ay_global, janela, grau)

# -----------------------------
# GRÁFICOS
# -----------------------------

if __name__ == "__main__":

    plt.figure(figsize=(8,5))
    plt.plot(t, ax_global, label="ax global bruto", alpha=0.4)
    plt.plot(t, ax_suave, label="ax global suavizado")
    plt.title("Aceleração X global: bruto vs suavizado")
    plt.xlabel("Tempo")
    plt.ylabel("ax global")
    plt.legend()
    plt.grid()

    plt.figure(figsize=(8,5))
    plt.plot(t, ay_global, label="ay global bruto", alpha=0.4)
    plt.plot(t, ay_suave, label="ay global suavizado")
    plt.title("Aceleração Y global: bruto vs suavizado")
    plt.xlabel("Tempo")
    plt.ylabel("ay global")
    plt.legend()
    plt.grid()

    plt.show()