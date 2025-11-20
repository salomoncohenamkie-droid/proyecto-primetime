# -*- coding: utf-8 -*-
"""
Created on Thu Nov  6 09:26:55 2025

@author: 260987
"""
import json
import pygame
"""
#   Permite agregar instituciones. ✅ 
#   Permite agregar estudiantes dentro de las instituciones.✅ 
#   Permite agregar materias para cada institución ✅ 
#   Permite guardar los criterios para calificar la materia.✅ 
#   Advierte si la ponderación es diferente de 100%✅ 
    -   Si la calificación ponderada es mayor a 10, la calificación es 10. ✅
-   Guarda las materias que ya se le dieron al programa. ✅
-   Calcula la calificación por materia. ✅
-   Calcula la calificación global.✅
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

def es_calificacion_valida(calificación):
    return 0 <= calificación and calificación <= 10
def es_porcentaje_valido(porcentaje):
    return 0 <= porcentaje and porcentaje <= 100

def calcular_calificacion_final_materia(parciales, porcentajes):
    for c in parciales.values():
        if not es_calificacion_valida(c):
            raise ValueError(f"calificación {c} en {parciales} es inválida")

    for p in porcentajes.values():
        if not es_porcentaje_valido(p):
            raise ValueError(f"porcentaje inexistente {p}")

    if not parciales.keys() == porcentajes.keys():
        raise ValueError("elementos de los porcentajes no coinciden con las calificaciones")

    calificacion_final=0
    for k in parciales.keys():
        calificacion_final = calificacion_final + parciales[k]*porcentajes[k]
    return min(calificacion_final / 100 , 10)
            
def calcular_calificacion_global(finales):
    if not finales:
        return 0
    return sum(finales.values()) / len(finales)


def calcular_calificacion_maxima(parciales, porcentajes):
    pass












if __name__ == "__main__":
    assert calcular_calificacion_final_materia(
        {"examen":10, "tarea": 8, "proyecto": 9},
        {"examen":40, "tarea": 20, "proyecto": 40}
    ) == 9.2
    try:
        calcular_calificacion_final_materia({"prácticas":10, "entregas": 8, "presentacion": 9},{"examen":40, "tarea": 20, "proyecto": 40} )
        raise EOFError("Debería lanzar un error")
    except ValueError:
        pass
    assert calcular_calificacion_final_materia({"examen":10, "tarea": 10, "proyecto": 10},{"examen":40, "tarea": 40, "proyecto": 40}) == 10
    assert calcular_calificacion_global({"TEA":9, "TIU":8, "Intro a Ing.":9, "Física 1":8, "Lab. Física 1":7, "Cálculo":9, "Química":5}) - 7.8571428571 < 0.0000001
    assert calcular_calificacion_maxima(
        {"tarea": 8, "proyecto": 9},
        {"examen":40, "tarea": 20, "proyecto": 40}
    ) == 9.2, "No sabe calcular calif max"

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    