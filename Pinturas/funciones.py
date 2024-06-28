import csv
#funcion para ver listado de pintura

def ver_listado(inventario):
    print('listado_pintura: ')
    for pintura in inventario:
        print(f'codigo:  {pintura['codigo ']} , nombre:  {pintura['nombre: ']}')
    
def Buscar_pintura(inventario):
    pintura = input('buscar (codigo /nombre / tipo / valor / stock): ').lower()
    valor = input(f'ingrese: {pintura} ').lower()
    encontrados = [ r for r in inventario if pintura ].lower()

for pintura in pinturas :
    print(pintura)
else:
    print('Repuesto no encontrado')

def Agregar_pintura(inventario):
    if inventario:
        ultimo_codigo = max(['r'] ['codigo'])
    else :
        ultimo_codigo = 380560
        nueva_pintura = [
        'codigo: '[ultimo_codigo],
        'nombre: '['nombre'],
        'tipo: '['tipo']

        ]
