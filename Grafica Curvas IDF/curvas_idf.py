""" ________________________________________________________________________________
 DESARROLLADOR       : Anthony Jean Paul Blaz Lazo
 LENGUAJE            : Python 3.9.1
 PROGRAMA            : Grafica de curvas IDF
 PAGINA              : www.faneci.com
 ________________________________________________________________________________"""
import numpy as np
import matplotlib.pyplot as plt

def grafica(periodos_de_retorno,lista_de_intensidades,duracion_en_minutos):
    for i in range(0,len(lista_de_intensidades)):
        periodo=periodos_de_retorno[i]
        plt.plot(duracion_en_minutos, lista_de_intensidades[i], label=f'T = {periodo} años', ls='-')
    v = [0, 60, 0, 400]
    plt.axis(v)
    plt.title('Curvas IDF para diferentes periodos de retorno', color='#00008B')
    plt.xlabel('Tiempo de duracion (min)')
    plt.ylabel('Intensidad (mm/hr)')
    plt.grid(b=True, which='major', color='#666666', linestyle='--')
    plt.legend(loc=1)
    plt.show()


def calculoDeIntensidades(duracion_en_minutos, periodos_de_retorno, coeficientes):
    K=coeficientes[0]
    n=coeficientes[1]
    m=coeficientes[2]
    lista_de_intensidades=[]
    for tr in periodos_de_retorno:
        intensidad=[]
        for t in duracion_en_minutos:
            i=(K*tr**m)/t**n
            intensidad.append(i)
        lista_de_intensidades.append(intensidad)
    grafica(periodos_de_retorno,lista_de_intensidades,duracion_en_minutos)

if __name__ == '__main__':

    inicio = 1
    fin = 60
    step = 1
    duracion_en_minutos = np.arange(inicio, fin+step, step)
    """ periodo_de_retorno= años a evaluar
        coeficientes=[k,n,m]
    """
    periodos_de_retorno = [2, 5, 10, 15, 25, 50, 100, 200, 500]
    coeficientes = [315.4687, 0.537521, 0.148940]
    calculoDeIntensidades(duracion_en_minutos, periodos_de_retorno, coeficientes)
