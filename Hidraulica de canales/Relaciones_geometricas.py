def canal_t(b, z, y):
    T = b+2*z*y
    A = b*y+z*y**2
    P = b*y+z*y**2
    R = A/P
    return T, A, P, R


if __name__ == '__main__':

    opcion = int(input('''

                ELEGIR EL TIPO DE CANAL

            1. CANAL RECTANGULAR
            2. CANAL TRAPEZOIDAL
            3. CANAL TRIANGULAR

            Seleccion: '''))
    if opcion == 1:
        b = float(input("b = "))
        y = float(input("y = "))
        T, A, P, R = canal_t(b, 0, y)
    elif opcion == 2:
        b = float(input("b = "))
        y = float(input("y = "))
        z = float(input("z = "))
        T, A, P, R = canal_t(b, z, y)
    elif opcion == 3:
        z = float(input("z = "))
        y = float(input("y = "))
        T, A, P, R = canal_t(0, z, y)
    print(f"""
          Espejo de agua:       {round(T,2)}
          Area:                 {round(A,2)}
          Perimetro:            {round(P,2)}
          Radio hidraulico:     {round(R,2)}""")
