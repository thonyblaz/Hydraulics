""" ________________________________________________________________________________
 DESARROLLADOR       : Anthony Jean Paul Blaz Lazo
 LENGUAJE            : Python 3.9.1
 PROGRAMA            : Esquema de Relaciones Hidraulicas de una seccion circular
 PAGINA              : www.faneci.com
 ________________________________________________________________________________"""
import numpy as np
import matplotlib.pyplot as plt


# Ecuaciones a calcular
def relaciones(tita):
    relac_comun = tita-np.sin(tita)
    rpll_rll = relac_comun/tita
    vpll_vll = (rpll_rll)**(2/3)
    apll_all = relac_comun/(2*np.pi)
    qpll_qll = apll_all*vpll_vll
    return rpll_rll, vpll_vll, apll_all, qpll_qll

#Calculo del angulo
def angulo(x):
    tita = 2*(np.arccos(1-2*x))
    return tita


def grafica(yD):
    angle = []
    relac_radio = []
    relac_velocidad = []
    relac_area = []
    relac_caudales = []
    for i in yD:
        tita = angulo(i)
        angle.append(tita)
    for tita in angle:
        if tita == 0:
            radio = 0
            velocidad = 0
            area = 0
            caudal = 0
        else:
            radio, velocidad, area, caudal = relaciones(tita)
        relac_radio.append(radio)
        relac_velocidad.append(velocidad)
        relac_area.append(area)
        relac_caudales.append(caudal)
    # graficas
    v = [0, 1.3, 0, 1]
    plt.axis(v)
    plt.title(
        'Esquema de Elementos Hidraulicos \npara Seccion Circular', color='#00008B')
    plt.xlabel(
        'Relaciones de la seccion Parcialmente llena y Seccion Llena\n Rpll/Rll - Vpll/Vll - Apll/All - Qpll/Qll')
    plt.ylabel('Relacion Tirante - Diametro \ny/D')
    plt.xticks(np.linspace(0, 1.3, 14))
    plt.yticks(np.linspace(0, 1, 11))
    plt.grid(b=True, which='major', color='#666666', linestyle='--')
    plt.plot(relac_radio, yD, label="Rpll/Rll", ls='-')
    plt.plot(relac_velocidad, yD, label="Vpll/Vll", ls='-')
    plt.plot(relac_caudales, yD, label="Qpll/Qll", ls='-')
    plt.plot(relac_area, yD, label="Apll/All", ls='-')
    plt.legend(loc=4)
    plt.axhline(0.937, color='m', lw=1, ls='-.')
    plt.axhline(0.810, color='y', lw=1, ls='-.')
    plt.text(0.1, 0.945, 'Para un Qmax', color='#483D8B')
    plt.text(0.1, 0.818, 'Para una Vmax', color='#483D8B')
    plt.show()


if __name__ == '__main__':
    inicio = 0
    fin = 1
    step = 0.01
    yD = np.arange(inicio, fin+step, step)
    grafica(yD)
