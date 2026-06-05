import numpy as np
import matplotlib.pyplot as plt

from leitura import t, t_vi, cx, cy

#eh com esse grafico que vamos comparar no final 

# transformar em arrays
t_imu = np.array(t)
t_vi_array = np.array(t_vi)
cx_array = np.array(cx)
cy_array = np.array(cy)

# ordenar o VI pelo tempo
ordem = np.argsort(t_vi_array)

t_vi_ord = t_vi_array[ordem]
cx_ord = cx_array[ordem]
cy_ord = cy_array[ordem]


# interpolar trajetória do VI nos tempos da IMU
cx_interp = np.interp(t_imu, t_vi_ord, cx_ord)
cy_interp = np.interp(t_imu, t_vi_ord, cy_ord)

if __name__ == "__main__":

    plt.figure(figsize=(7,7))

    #plt.plot(cx_ord, cy_ord, label="Trajetória original", alpha=0.4)

    plt.plot(cx_interp, cy_interp, label="Trajetória interpolada", linewidth=2)

    plt.title("Cruzamento dos dados")
    plt.xlabel("x")
    plt.ylabel("y")

    plt.legend()
    plt.grid()
    plt.axis("equal")


'''

  esses dois gráficos são X vs T e Y vs T das posições do VI com o tempo da IMU. 
  Ou seja, a posição do VI interpolada nos tempos da IMU.  
    plt.figure(figsize=(8,5))

    plt.plot(
        t_imu,
        cx_interp,
        label="x(t)"
    )

    plt.title("Posição X vs tempo")
    plt.xlabel("Tempo")
    plt.ylabel("x")

    plt.legend()
    plt.grid()

    # -------------------
    # Y vs T
    # -------------------

    plt.figure(figsize=(8,5))

    plt.plot(
        t_imu,
        cy_interp,
        label="y(t)"
    )

    plt.title("Posição Y vs tempo")
    plt.xlabel("Tempo")
    plt.ylabel("y")
    plt.legend()
    plt.grid()
'''
plt.show()