'''
Metodo del esquema de Steffensen
Applied Mathematics and Computation
A family of Kurchatov-type methods and its stability
Pag.1 Steffensen’s scheme [25]
Ejemplo : sne_fd_3("x**2 - 18",3,0.0001,1)
'''

import matplotlib.pyplot as plt
from sympy import Symbol, sympify, diff, Subs

# CONSISTE EN
# 
# ENTRADAS
# f : funcion
# x0 : valor inicial
# tol : tolerancia
# graf = grafica
# SALIDAS
# xaprox : aproximacion de x
# iter : cantidad de iteraciones
def sne_fd_3(f, x0, tol, graf):
    x = Symbol("x")  # Declaración de x como variable independiente
    try:
        ff = sympify(f)  # Función String -> Ecuación
        fd = diff(ff, x)  # Derivada de la función
        i = 0  # Cantidad de iteraciones
        eje_x = []  # Valores en el eje x para la grafica
        eje_y = []  # Valores en el eje y para la grafica
        xk = x0  # Sucesión de x (valor inicial)
        while (abs(ff.subs(x, xk)) >= tol):  # Evaluacación de la condición de parada
            eje_x += [i]  # Nuevo punto al eje x
            eje_y += [abs(ff.subs(x, xk))]  # Nuevo punto al eje y            
            wk = xk + ff.subs(x, xk)  # # Sucesión de w
            fxkwk =  (ff.subs(x, xk) - ff.subs(x, wk)) / (xk - wk) # Sucesión de f(xk, wk)
            xk = xk - ff.subs(x, xk) / fxkwk  # Sucesión de x
            xk = float(xk) # xk decimal 
            i += 1  # Incremento de iteraciones
        if graf == 1:
            plt.plot(eje_x, eje_y)  # Llamado para gerenar la grafica
            plt.title('Metodo del Esquema de Steffensen')  # Titulo de la grafica
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
        print('Error: Expresión no valida')  # Error
        