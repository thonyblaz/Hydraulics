import matplotlib.pyplot as plt
import numpy as np
# Datos previos
COLORES = ['g', "magenta", 'r', "orange", "blue", "red",
           "gold", "green", 'g', "magenta", "cyan", "red", "black"]
ESTILO = ['--', ":", ':', "-", "--", '--', ":", ':', "-", "--", "-", "--", ":"]
fig = plt.figure("Filtro")
#datos del canal
y = np.arange(0.01, 100, 0.01)  # Tirante de flujo y(m)
B = 2  # Base del canal en m
# grafica E-y
fig.add_subplot(1, 2, 1)
# =====
Q = [5, 10,15, 20, 30, 40]  # Caudal del canal m3/s
for i in range(len(Q)):
    x = y+Q[i]**2/(19.914*(B*y)**2)
    # diametro efectivo
    plt.plot(x, y, linestyle="-",
             color=COLORES[i], label="Q = "+str(Q[i])+"m3/s")
plt.plot([0, 10], [0, 10], linestyle="--", color="black")  # diametro efectivo
plt.grid(True)  # Activa cuadrícula del gráfico pero no se muestra
plt.xlim(0, 10)
plt.ylim(0, 10)
plt.title('Energia especifica E-y B = '+str(B)+"m", fontsize=10)
plt.xlabel("Energia E(m)")  # Establece el título del eje x
plt.ylabel("Tirante y(m)")   # Establece el título del eje y
plt.legend(loc="best")
# grafica Q-y
fig.add_subplot(1, 2, 2)
# =====
E = [1,1.5,2,3,5,10]  # Energia E(m)
for I in range(len(Q)):
    x = np.sqrt(19.914*(B*y)**2*(E[I]-y))
    # diametro efectivo
    plt.plot(x, y, linestyle="-", color=COLORES[I], label="E = "+str(E[I])+"m")
plt.title("Energia especifica Q-y B = "+str(B)+"m", fontsize=10)
# Establece el título del eje x
plt.xlabel("Caudal Q(m3/s) \n por: Anthony Blaz Lazo")
plt.ylabel("Tirante y(m)")    # Establece el título del eje y
# Activa cuadrícula del gráfico pero no se muestra
plt.grid(True)
plt.legend(loc="best")
# mostrar todo el grafico
plt.show()
