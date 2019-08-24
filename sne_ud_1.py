'''
Metodo Weerakoon and Fernando
Computers and Structures
Performance of cubic convergent methods for implementing nonlinear constitutive models
Pag.2  M1 – Weerakoon and Fernando (2000) [21]
'''

import matplotlib.pyplot as plt
from sympy import Symbol, sympify, diff, Subs

# ENTRADAS
# f : funcion
# x0 : valor inicial
# tol : tolerancia
# graf = grafica
# SALIDAS
# xaprox : aproximacion de x
# iter : cantidad de iteraciones
def sne_ud_1(f, x0, tol, graf):
    x = Symbol("x")  # Declaracion de x como variable independiente
    try:
        ff = sympify(f)  # Funcion String -> Ecuacion
        fd = diff(ff, x)  # Derivada de la funcion
        i = 0  # Cantidad de iteraciones
        eje_x = []  # Valores en el eje x para la grafica
        eje_y = []  # Valores en el eje y para la grafica
        xk = x0  # Sucesion de x (valor inicial)
        while (abs(ff.subs(x, xk)) >= tol):  # Evaluacacion de la condicion de parada
            eje_x += [i]  # Nuevo punto al eje x
            eje_y += [abs(ff.subs(x, xk))]  # Nuevo punto al eje y            
            xk = xk - 2 * ff.subs(x, xk) / (fd.subs(x, xk) + fd.subs(x, xk - (ff.subs(x, xk) / fd.subs(x, xk))) )   # Sucesion de x
            i += 1  # Incremento de iteraciones
        if graf == 1:
            plt.plot(eje_x, eje_y)  # Llamado para gerenar la grafica
            plt.title('Metodo Weerakoon and Fernando')  # Titulo de la grafica
            plt.xlabel('iteraciones (k)')  # Nombre del eje x
            plt.ylabel('|f(xk)|')  # Nombre del eje y
            plt.grid(True)  # Despliege del grid
            plt.show()  # Despliege del grafico
        elif graf == 0:
            print("Sin grafica")  # Error
        else:
            print("Error: Entrada invalida (graf) : 1 | 0")  # Error
        print("xaprox " + str(float(xk)) + "\niter: " + str(i))  # Salida
    except:
        print('Error: Expresion no valida')  # Error
