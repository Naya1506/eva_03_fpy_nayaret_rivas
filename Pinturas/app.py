import json
import os 
from funciones import ver_listado , Buscar_pintura , Agregar_pintura, Eliminar_pintura, Exportar_pintura
from pathlib import Path 

def cargar_datos():
    try:
        with open('inventario.json', 'r') as file:
            return json.load(file)
    except:
        FileNotFoundError  
        with open('inventario.json', 'w') as file:
            json.dump([], file)
            return[]
        
def guardar_datos(datos):
    with open('inventario.json', 'w') as file:
        json.dump(datos, file, indent=4)

inventario = cargar_datos()


while True:
    print('\n1. Ver listado pintura acrilica')
    print('2. Buscar pintura')
    print('3. Agregar pintura')
    print('4. Eliminar pintura')
    print('5. Exportar pintura')
    print('6. Salir')

    opcion = input('Selecciona una opción: \n')
    
    if opcion == '1':
        ver_listado(inventario) 
    elif opcion == '2':
        Buscar_pintura(inventario)
    elif opcion == '3':
        Agregar_pintura(inventario)
        guardar_datos(inventario)
    elif opcion == '4':
        Eliminar_pintura(inventario)
    elif opcion == '5':
        Exportar_pintura(inventario)   
    elif opcion == '6':
        break
    else:
        print('Opción no valida\n')