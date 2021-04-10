""" ________________________________________________________________________________
 DESARROLLADOR       : Anthony Jean Paul Blaz Lazo
 LENGUAJE            : Python 3.9.1
 PROGRAMA            : Diseno de u n tramo de un alcantarillado sanitario o pluvial
 PAGINA              : www.faneci.com
 ________________________________________________________________________________"""
import numpy as np


def angulo(Q, n, S, Dc):
    m = (2**(13/5))*(Dc**-1.6)*(Q*n/(S)**0.5)**(3/5)
    ang_inicial = 2.5
    for _ in range(0, 50):
        fx = np.sin(ang_inicial)+m*ang_inicial**0.4-ang_inicial
        dfx = np.cos(ang_inicial)+0.4*m*ang_inicial**-0.6-1
        tita = ang_inicial-fx/dfx
        error = abs(ang_inicial-tita)
        ang_inicial = tita
        if error < 0.0001:
            break
    return tita


def diseno(Q, S, n, elec):
    Q = Q/1000
    S = S/100
    if elec == 1:
        k = 1.6
        alc = 'Sanitario'
    elif elec == 2:
        k = 1.51
        alc = 'Pluvial'
    D = k*(Q*n/(S)**0.5)**(3/8)
    if round(D, 1) < D:
        Dc = round(D, 1)+0.05
        coef_Smin = 0.00067
    else:
        Dc = round(D, 1)
        coef_Smin = 0.001197
    Dc = round(Dc, 2)

    Qll = ((S**0.5)*(Dc**(8/3)))/(3.2*n)
    Vll = (1/n)*(S**0.5)*(Dc/4)**(2/3)
    Qpll_Qll = Q/Qll
    tita = angulo(Q, n, S, Dc)
    y_D = (1-np.cos(tita/2))/2
    area = (Dc**2)*(tita-np.sin(tita))/8
    espejo_de_agua = Dc*np.sin(tita/2)
    perimetro = tita*Dc/2
    rh = area/perimetro
    velocidad = (1/n)*(S**0.5)*(rh)**(2/3)
    Tension_tractiva = 1000*rh*S
    Smin = 100*(coef_Smin/Dc)
    nf = velocidad/(9.81*area/espejo_de_agua)**0.5
    if nf < 1:
        flujo = 'Subcritico'
    elif nf == 1:
        flujo = 'Critco'
    elif nf > 1:
        flujo = 'SuperCritico'
    print(f"\n                       Tramo de un Alcantarillado {alc}")
    print(f""" 
          Datos:
            Caudal:             Q = {Q*1000} (lt/s) 
            Pendiente:          S = {S*100} %
            Coef. de rugosidad: n = {round(n,3)}
          Calculos:
            Diametro Calculado: D = {round(D,3)}(m)
            Diametro Comercial: Dc = {Dc*1000} (mm)\n
                        Seccion  Llena\n
          Caudal:               Qll = {round(Qll*1000,3)} (lt/s)
          Velocidad:            Vll = {round(Vll,3)} (m/s)
          Relacion:        Qpll/Qll = {round(Qpll_Qll,3)}\n
                    Seccion Parcialmente Llena\n
          Angulo interno:               tita = {round(tita,4)} rad
          Relacion tirante diametro      y/D = {round(y_D,3)}
          Area:                            A = {round(area,4)} (m2)
          Perimetro:                       P = {round(perimetro,4)} (m)
          Radio Hidraulico                Rh = {round(rh,4)} (m)
          Espejo de agua:                  T = {round(espejo_de_agua,4)}
          Velocidad de flujo:              V = {round(velocidad,4)} (m/s)
          Tension tractiva:              Tau = {round(Tension_tractiva,4)} (kg/m2)
          Pendiente minima              Smin = {round(Smin,3)} % (Criterio de la tension tractiva)
          Numero de Froude                NF = {round(nf,3)} 
          Tipo de flujo:                {flujo} 
          """)
    return 1


if __name__ == '__main__':
    caudal = 9.95
    pendiente_porc = 0.6
    coef_de_rugosidad = 0.013
    alcantarillado = 1
    # 1 para alcantarillado sanitario y 2 para alcantarillado pluvial
    diseno(caudal, pendiente_porc, coef_de_rugosidad, alcantarillado)
