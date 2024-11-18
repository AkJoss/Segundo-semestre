# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 20:21:24 2024

@author: josea
"""

class personaje:
    def __init__(self, nombre, casa):
        self.nombre = nombre
        self.casa = casa
    def presentarse(self):
        #metodo que permite presentarse al personaje
        return f"Hola mi nombre es {self.nombre} y mi casa es {self.casa}"
class varita:
    def __init__(self, material, longitud):
        self.material = material
        self.longitud = longitud
    def descripcion_varita(self):
        return f"Varita de {self.material}, y la longitud de mi varita es de {self.longitud} cm"
    
class estudiante(personaje):
    def __init__(self, nombre, casa, año):
        super().__init__(nombre, casa)
        self.año = año
    def detalle_estudiante(self):
        return f"{self.presentarse()} estoy en mi año {self.año} en howarts"
    
class profesor(personaje):
    def __init__(self, nombre,casa, materia):
        super().__init__(nombre, casa)
        self.materia = materia
    def detalle_profesor(self):
        return f"{self.nombre}: Enseña {self.materia}"
harry = estudiante("Harry Potter", "Gryffindor", "5")
harry_varita = varita("Sauco", "33")

mcgonagall = profesor("Minerva McGonagal", "Gryffindor", "Transformaciones")

print(harry.detalle_estudiante())
print()
print(harry_varita.descripcion_varita())
print()
print(mcgonagall.detalle_profesor())
