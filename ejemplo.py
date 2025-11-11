# -*- coding: utf-8 -*-
"""
Created on Thu Nov  6 09:26:55 2025

@author: 260987
"""
import json
import pygame
"""
#   Permite agregar instituciones.
#   Permite agregar estudiantes dentro de las instituciones.
#   Permite agregar materias para cada institución
#   Permite guardar los criterios para calificar la materia.
#   Advierte si la ponderación es diferente de 100%
    -   Si la calificación ponderada es mayor a 10, la calificación es 10.
-   Guarda las materias que ya se le dieron al programa.
-   Calcula la calificación por materia.
-   Calcula la calificación global.
-   Calcula la calificación máxima con las entregas hasta el momento.
-   Te dice qué necesitas sacar en una materia para llegar a tu calificación objetivo.
-   Tiene una interfaz para cada actividad.
-   Gestiona correctamente entrada de datos incorrectos.
"""

def guardar_informacion(info):
    with open("archivo","w") as f:
        f.write(json.dumps(info))

def cargar_informacion():
    with open ("archivo","r") as f:
        return json.loads(f.read())

info = {"IBERO": {"Salomon": 1}}
info = {"Anahuac": {"David": 1}}
info = {"Tecnologico de Monterrey":{"Pulver": 1}}