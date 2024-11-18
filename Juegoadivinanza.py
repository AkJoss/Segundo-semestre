# -*- coding: utf-8 -*-
"""
Created on Wed May  8 09:26:24 2024

@author: josea
"""

import random

class JuegoAdivinanza():
    def _init_(self):
        self.palabras = ["python", "drake", "perro", "reprobados"]
        self.palabra_secreta = random.choice(self.palabras)
        self.intentos_maximos = 5
        self.intentos_restantes = self.intentos_maximos
        self.letras_adivinadas = ["_"] * len(self.palabra_secreta)
        self.letras_usadas = set()
                 
                 
    def mostrar_estado(self):
        print("Palabra secreta: ", " ".join(self.letras_adivinadas))
        print("Intentos restantes: ", self.intentos_restantes)
        print("Letras usadas: ", ", ". join(sorted(self.letras_usadas)))
    
    def adivinar_letra(self, letra):
        if letra in self.letras_usadas:
            print(f"Ya has usado la letra '{letra}', intenta con otra")
            #compresin de listas
        else:
            self.letras_usadas.add(letra)
            if letra in self.palabra_secreta:
                indices = [i for i, l in enumerate(self.palabra_secreta) if l == letra]
                for index in indices:
                    self.letras_adivinadas[index] = letra
                print("Correcto")
            else:
                self.intentos_restantes -= 1
                print(f"La letra '{letra}' no esta en la palabrea")
        self.mostrar_estado()
        
    def adivinar_palabra(self, palabra):
        if palabra == self. palabra_secreta:
            self.letras_adivinadas = list(self.palabra_secreta)
            print("Felicidades, has adivinado la palabra secreta")
        else: 
            self.intentos_restantes -= 1
            print(f"La palabra'{palabra}' no es la palabra secreta")
        self.mostrar_estado()

###############################################################################
#codifo para iniciar el juego
juego = JuegoAdivinanza()
juego.mostrar_estado()
        
while juego.intentos_restantes > 0 and "_" in juego.letras_adivinadas:
    entrada = input("Adivina una ñetra o la palabra completa: ").lower()
    if len(entrada) == 1:
        juego.adivinar_letra(entrada)
    elif len(entrada) == len(juego.palabra):
        juego.adivinar__palabra(entrada)
    else:
        print("Por favor, introduce una letra o una palabra del tamaño correcto")
    
if "_" not in juego.letras_adivinadas:
    print("Ganaste")
else:
    print("Se acabaron los intentos. La palabra era: ", juego.palabra_secreta)