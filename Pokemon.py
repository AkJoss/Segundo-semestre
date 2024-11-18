# -*- coding: utf-8 -*-
"""
Created on Wed May  8 09:33:15 2024

@author: josea
"""
import random
class pokemon:
    def __init__ (self, nombre, tipo, hp, ataques):
        self.nombre = nombre
        self.tipo = tipo
        self.hp = hp
        self.ataques = ataques
        self.defensa_activa = False
        
        
    def atacar(self, ataques, oponente):
        if self.defensa_activa:
            print(f"{self.nombre} no puede atacar mientras esta defendiendo.")
            self.defensa_activa = False #reset de la defensa despues del turno
            return
        #Calculo del daño consideracion de tipo
        daño_base = self.ataques[ataques]
        multiplicador = 1
        if (self.tipo == "Fuego" and oponente.tipo == "Planta") or \
            (self.tipo == "Planta" and oponente.tipo == "Agua") or \
            (self.tipo == "Agua" and oponente.tipo == "Fuego"):
                multiplicador = 1.5
                print("¡Super efectivo!")
        elif (self.tipo == "Fuego" and oponente.tipo == "Agua") or \
            (self.tipo == "Planta" and oponente.tipo == "Fuego") or \
            (self.tipo == "Fuego" and oponente.tipo == "Planta"):
                multiplicador = 0.5
                print ("No es muy efectivo...")
        daño_final = int(daño_base * multiplicador)
        print(f"{self.nombre} usa {ataques} y causa {daño_final} de daño a {oponente.nombre}.")
        oponente.recibir_daño(daño_final)
            
    def recibir_daño(self, daño):
            if self.defensa_activa:
                daño //= 2 #reduce el daño a la mitad
                print(f"{self.nombre} ha defendido parte del ataque.")
                self.defensa_activa = False #reset de la defensa por cada turno
                self.hp -= daño
                print(f"{self.nombre} ahora tiene {self.hp} de HP.")
                 
    def defender(self):
                    self.defensa_activa = True
                    print(f"{self.nombre} esta en posicion defensiva")
                    
    def esta_vivo(self):
                    return self.hp > 0 
############################################################################
            
class BatallaPokemon:
    def __init__(self, pokemon1, pokemon2):
            self.pokemon1 = pokemon1
            self.pokemon2 = pokemon2
            
    def mostrar_estado(self):
            print("\nEstado de la batalla:")
            print(f"{self.pokemon1.nombre} - HP: {self.pokemon1.hp}")
            print(f"{self.pokemon2.nombre} - HP: {self.pokemon2.hp}")
            
    def ejecutar_turno(self, pokemon, accion, oponente):
            if accion in pokemon.ataques:
                pokemon.atacar(accion, oponente)
            elif accion == "defender":
                pokemon.defender()
            else:
                print("Accion no valida. Intentalo de nuevo")
############################################################################
#lista de pokemon disponibles
pokemones = [
    pokemon("Riolu", "Lucha", 100, {"Golpe bala": 20, "Aura esfera": 40}),
    pokemon("Charmander", "Fuego", 120, {"Lanzallamas": 18, "LLamarada": 24}),
    pokemon("Squierte", "Agua", 100, {"Chorro de agua": 16, "Hidrobomba": 26}),
    pokemon("Bulbasaur", "Plnta", 100, {"Latigo cepa": 15, "Rayo solar": 25})
    ]

#permitir que el usuario elija su Pokemon
print("Elige tu Pokemon:")
for i, p in enumerate(pokemones):
    print(f"{i + 1}. {p.nombre} - Tipo: {p.tipo} - HP: {p.hp}")
eleccion_jugador = int(input("numero del pokemon: ")) - 1 
jugador = pokemones[eleccion_jugador]
            
#permitir que el usuario elija su Pokemon
print("Elige tu Pokemon:")
for i, p in enumerate(pokemones):
    if i != eleccion_jugador: #No permite elegir el mismo pokemon
        print(f"{i + 1}. {p.nombre} - Tipo: {p.tipo} - HP: {p.hp}")
eleccion_joponente = int(input("numero del pokemon: ")) - 1 
oponente = pokemones[eleccion_jugador]
            
# Crear batalla
batalla = BatallaPokemon(jugador, oponente)

# Ejecutar la batalla
while jugador.esta_vivo() and oponente.esta_vivo():
    batalla.mostrar_estado()
    acciones = list(jugador.ataques.keys()) + ['defender']
    print(f"turno de {jugador.nombre}. elige un ataque:{acciones}")
    accion_jugador = input("Escribe tu eleccion: ")
    accion_oponente = random.choice(list(oponente.ataques.keys()) + ['defender'])
    batalla.ejecutar_turno(oponente, accion_jugador, oponente)
    if oponente.esta_vivo():
        batalla.ejecutar_turno(oponente, accion_oponente, jugador)
        
    #Mostrar el resultado de la batalla
    if jugador.esta_vivo():
        print(f"\n{jugador.nombre} ha ganado la batalla.")
    else:
        print(f"\n{oponente.nombre} ha ganado la batalla.")