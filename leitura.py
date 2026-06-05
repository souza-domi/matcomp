import pandas as pd

# -----------------------------
# IMU
# -----------------------------

imu = pd.read_csv(
    "C:/Users/Domi/Desktop/matcomp/imu1.csv",
    header=None
)

# tempo da IMU
t = imu[0]
t = t - t.iloc[0]

# orientação do sensor
roll = imu[1]
pitch = imu[2]
yaw = imu[3]

# aceleração no referencial do sensor
ax = imu[10]
ay = imu[11]
az = imu[12]

# -----------------------------
# VI / VICON - Trajetória Real
# -----------------------------

vi = pd.read_csv(
    "C:/Users/Domi/Desktop/matcomp/vi1.csv",
    header=None
)

# tempo do VI está em nanossegundos
t_vi = vi[0]
t_vi = t_vi - t_vi.iloc[0]
t_vi = t_vi / 1e9

# coordenadas da trajetória real
cx = vi[2]
cy = vi[3]