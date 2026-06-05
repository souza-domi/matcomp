import matplotlib.pyplot as plt

from leitura import cx, cy

# -----------------------------
# GRÁFICO DA TRAJETÓRIA REAL
# -----------------------------


plt.figure(figsize=(7,7))

plt.plot(cx, cy, label="Trajetória real")

plt.title("Trajetória real do VI")

plt.xlabel("x")
plt.ylabel("y")

plt.legend()
plt.grid()

plt.axis("equal")

plt.show()