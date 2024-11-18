# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 20:21:21 2024

@author: josea
"""

#Clases
class personaje:
    def __init__(self, nombre, casa):
        self.nombre = nombre
        self.casa = casa
    def presentarse(self):
        return f"hola, mi nombre es {self.nombre} y soy de {self.casa}"
#creacion de un objeto de la clase personaje 
Ron = personaje ("Ron Weasley", "Gryffindor")

#llamada al metodo del objeto
print(Ron.presentarse())

# Parte 2 "Herencia 

# subclase que hereda de Personaje 

class estudiante(personaje):
    def __init__(self, nombre, casa, año):
        super().__init__(nombre, casa)
        self.año = año
        
    def detalle_estudiante(self):
        #estencion del metodo para agregar mas detalles
        return f"{self.presentarse()}, estoy en mi año {self.año} en Howarts"
    
    #creacion de un objeto estudiante 
Ron = estudiante ("Ron Weasley", "Griffindor", "5")
# uso de metodos heredados y nuevos 
print(Ron.detalle_estudiante())


#Parte 3 Polimorfismo
class personaje:
    def __init__(self, nombre, casa):
        self.nombre = nombre
        self.casa = casa
    def accion(self):
        return "participa en actividades de Howarts"
    
class estudiante(personaje):
    def __init__(self, nombre, casa, año):
        super(). __init__(nombre, casa)
        self.año = año 
    
    def accion(self):
        return f"Asiste a clase y estudia  para los examenes en {self.año} año"
    
class profesor(personaje):
    def __init__(self, nombre, casa, materia):
        super(). __init__(nombre, casa)
        self.materia = materia
        
    def accion(self):
        #metodo sobreescritoque especifica la accion para un profesor
        return f"enseña {self.materia}"
    #creacion de diferentes objetos de diferentes clases 
Ron = estudiante("Ron Weasley", "Griffindor", "5")
Mcgonagall = profesor("Minerva Mcgonagall", "Gryffindor", "Transformaciones")

#lista de personajes 
personajes = [Ron, Mcgonagall]

#polimorfismo en accion 
for personaje in personajes:
    print(f"{personaje.nombre}: {personaje.accion}")
