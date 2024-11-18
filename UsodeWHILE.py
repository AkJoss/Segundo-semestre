# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 10:38:59 2024

@author: josea
"""

#Ejemplo de uso de WHILE

contador = 0

while contador < 5:
    print(f"es menor:{contador}")
    #contador = contador + 1
    contador += 1
else:
    print("El bucle while ha completado su ejecucion")