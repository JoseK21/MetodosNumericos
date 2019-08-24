'''
Metodo Frontini and Sormani, 0zban 
Computers and Structures
Performance of cubic convergent methods for implementing nonlinear constitutive models
Pag.2-3  M2 – Frontini and Sormani (2003) [22], 0zban (2004) [23]
Ecuación (7)
Ejemplo : sne_ud_2("x**3 + 6*x**2 - 18",3,0.0001,1)
'''

import matplotlib.pyplot as plt
from sympy import Symbol, sympify, diff, Subs

# CONSISTE EN
#   un método multipunto redescubrierto propuesto por Traub siguiendo el procedimiento adoptado Kiran et al.
# ENTRADAS
#   f : función
#   x0 : valor inicial
#   tol : tolerancia
#   graf = parámetro para mostrar la gráfica
# SALIDAS
#   xaprox : aproximacián de x
#   iter : cantidad de iteraciones
#   graf : gráfica resultante
def sne_ud_2(f, x0, tol, graf):
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
            xk = xk - ff.subs(x, xk) / fd.subs(x, xk - 0.5 * ff.subs(x, xk) / fd.subs(x, xk))  # Sucesion de x
            i += 1  # Incremento de iteraciones
        if graf == 1:
            plt.plot(eje_x, eje_y)  # Llamado para gerenar la grafica
            plt.title('Metodo Frontini and Sormani, 0zban')  # Titulo de la grafica
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
