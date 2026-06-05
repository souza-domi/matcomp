import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import cumulative_simpson
from scipy.spatial import procrustes

from splines import t_spline, ax_spline, ay_spline
from trajetoria import cx_interp, cy_interp
from leitura import t as t_imu

# -----------------------------
# ESCOLHER JANELA
# -----------------------------

inicio = 35
fim = 56

# -----------------------------
# IMU NA JANELA
# -----------------------------

mascara_imu = (t_spline >= inicio) & (t_spline <= fim)

t_local = t_spline[mascara_imu]
ax = ax_spline[mascara_imu]
ay = ay_spline[mascara_imu]

t_local = t_local - t_local[0]

# remover bias local da aceleração
ax = ax - np.mean(ax)
ay = ay - np.mean(ay)

# aceleração -> velocidade
vx = cumulative_simpson(ax, x=t_local, initial=0)
vy = cumulative_simpson(ay, x=t_local, initial=0)

# corrigir drift linear da velocidade
vx = vx - np.linspace(vx[0], vx[-1], len(vx))
vy = vy - np.linspace(vy[0], vy[-1], len(vy))

# velocidade -> posição
x_imu = cumulative_simpson(vx, x=t_local, initial=0)
y_imu = cumulative_simpson(vy, x=t_local, initial=0)

x_imu = x_imu - x_imu[0]
y_imu = y_imu - y_imu[0]

# -----------------------------
# VI / VICON NA MESMA JANELA
# -----------------------------

mascara_vi = (t_imu >= inicio) & (t_imu <= fim)

x_vi = cx_interp[mascara_vi]
y_vi = cy_interp[mascara_vi]

x_vi = x_vi - x_vi[0]
y_vi = y_vi - y_vi[0]

# -----------------------------
# IGUALAR TAMANHOS
# -----------------------------

n = min(len(x_imu), len(x_vi))

x_imu = x_imu[:n]
y_imu = y_imu[:n]

x_vi = x_vi[:n]
y_vi = y_vi[:n]

t_plot = t_local[:n]
vx_plot = vx[:n]
vy_plot = vy[:n]
ax_plot = ax[:n]
ay_plot = ay[:n]

# -----------------------------
# ESCALA SIMPLES DA IMU
# -----------------------------

escala_imu = np.sqrt(np.mean(x_imu**2 + y_imu**2))
escala_vi = np.sqrt(np.mean(x_vi**2 + y_vi**2))

fator = escala_vi / escala_imu

x_imu_esc = x_imu * fator
y_imu_esc = y_imu * fator

# -----------------------------
# ROTAÇÃO FIXA 135°
# -----------------------------

theta = np.radians(135)

x_rot = (
    x_imu_esc * np.cos(theta)
    - y_imu_esc * np.sin(theta)
)

y_rot = (
    x_imu_esc * np.sin(theta)
    + y_imu_esc * np.cos(theta)
)

# -----------------------------
# PROCRUSTES
# -----------------------------

vi_pts = np.column_stack((x_vi, y_vi))
imu_pts = np.column_stack((x_rot, y_rot))

m1, m2, disparity = procrustes(vi_pts, imu_pts)

print("Disparity:", disparity)

# -----------------------------
# GRÁFICOS
# -----------------------------

plt.figure(figsize=(8,5))
plt.plot(t_plot, ax_plot, label="ax global")
plt.plot(t_plot, ay_plot, label="ay global")
plt.title("Aceleração global na janela")
plt.xlabel("Tempo local")
plt.ylabel("Aceleração")
plt.legend()
plt.grid()

plt.figure(figsize=(8,5))
plt.plot(t_plot, vx_plot, label="vx corrigido")
plt.plot(t_plot, vy_plot, label="vy corrigido")
plt.title("Velocidade integrada com Simpson e correção de drift")
plt.xlabel("Tempo local")
plt.ylabel("Velocidade")
plt.legend()
plt.grid()

plt.figure(figsize=(7,7))
plt.plot(x_vi, y_vi, label="VI / Vicon")
plt.plot(x_rot, y_rot, label="IMU rotacionada 135°")
plt.title("Antes do Procrustes")
plt.xlabel("x")
plt.ylabel("y")
plt.axis("equal")
plt.legend()
plt.grid()

plt.figure(figsize=(7,7))
plt.plot(m1[:,0], m1[:,1], label="VI")
plt.plot(m2[:,0], m2[:,1], label="IMU alinhada")
plt.title(f"Procrustes + 135° + Simpson | disparity = {disparity:.4f}")
plt.xlabel("x")
plt.ylabel("y")
plt.axis("equal")
plt.legend()
plt.grid()

plt.show()