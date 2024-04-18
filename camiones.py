"""Una empresa de transporte tiene tres camiones (C1, C2 y C3) y tres rutas (R1, R2 y R3) para entregar paquetes a diferentes destinos. 
Cada camión tiene una capacidad máxima diferente: C1 puede transportar hasta 10 paquetes, C2 puede transportar hasta 8 paquetes y C3 puede transportar hasta 6 paquetes.
Cada ruta tiene un número diferente de paquetes que deben entregarse: R1 tiene 12 paquetes, R2 tiene 7 paquetes y R3 tiene 5 paquetes.
La empresa quiere asignar los camiones a las rutas de manera que se entreguen todos los paquetes y se maximice la capacidad utilizada de cada camión. 
Además, cada camión solo puede hacer una ruta y cada ruta solo puede ser asignada a un camión. 
Crear un CSP para la Asignación de Camiones a Rutas"""

variables = ['c1', 'c2', 'c3']
rutas = ['r1', 'r2', 'r3']
capacidades_camiones = {'c1': 10, 'c2': 8, 'c3': 6} #Declaracion de librerias para las capacidades de los camiones 
nombre_usuario =  input("Por favor, ingrese su nombre: ") #"Yesid Castro"
paquetes_rutas = {'r1': 12, 'r2': 7, 'r3': 5} #Declaracion de Librerias para las rutas

def comprobar(asignacion):
    #Restriccion 1
    asignaciones_validas = set(asignacion) == set(rutas) and len(asignacion) == len(variables)   # verifica que cada  camion tenga exactamente una ruta asignada  
    #Restriccion 2
    paquetes_entregados = sum(paquetes_rutas[ruta] for ruta in asignacion) == sum(paquetes_rutas.values()) # verifica que todos los paquetes sean entregados
    # Restricción 3 
    capacidad_utilizada = all(sum(paquetes_rutas[ruta] for ruta in asignacion if ruta == camion) <= capacidades_camiones[camion] for camion in variables) # verifica que la cantidad de paquetes asignados a cada camion no exeda su capacidad.
    # Restricción 4 
    asignaciones_unicas = len(set(asignacion)) == len(asignacion) == len(set(variables)) == len(set(rutas)) == len(variables) # verifica que cada ruta sea asignaa a un unico camion.
    
    return asignaciones_validas and paquetes_entregados and capacidad_utilizada and asignaciones_unicas

# ______________Función de backtracking validar_______________
def backtracking(asignacion_actual, pos_camion):
    global mejor_asignacion, mejor_capacidad_utilizada, menor_paquetes_perdidos
    
    if pos_camion == len(variables):
        if comprobar(asignacion_actual):
            capacidad_utilizada_total = sum(min(paquetes_rutas[ruta], capacidades_camiones[camion]) for ruta, camion in zip(asignacion_actual, variables))
            paquetes_perdidos = sum(paquetes_rutas.values()) - capacidad_utilizada_total
            
            print("Ruta asignada:")
            for i, ruta in enumerate(asignacion_actual):
                camion = variables[i]
                paquetes_entregados = min(paquetes_rutas[ruta], capacidades_camiones[camion])
                print(f"Camion {camion} asignado a ruta {ruta} con {paquetes_entregados} paquetes entregados")
            print(f"Paquetes perdidos: {paquetes_perdidos}")
            print("--------------------------")
            
            if capacidad_utilizada_total > mejor_capacidad_utilizada or (capacidad_utilizada_total == mejor_capacidad_utilizada and paquetes_perdidos < menor_paquetes_perdidos):
                mejor_asignacion = asignacion_actual.copy()
                mejor_capacidad_utilizada = capacidad_utilizada_total
                menor_paquetes_perdidos = paquetes_perdidos
        return
    
    if pos_camion == 0 and asignacion_actual[0] == 'r1':
        asignacion_actual[pos_camion] = 'r1'
        backtracking(asignacion_actual.copy(), pos_camion + 1)
    else:
        for ruta in rutas:
            asignacion_actual[pos_camion] = ruta
            backtracking(asignacion_actual.copy(), pos_camion + 1)

# ____________busqueda de asignación vacía_______________
mejor_asignacion = []
mejor_capacidad_utilizada = float('-inf')
menor_paquetes_perdidos = float('inf')
backtracking([''] * len(variables), 0)

# _____________________Imprimir la mejor ruta________________________
if mejor_asignacion:
    print(f"{nombre_usuario},La mejor ruta fue la siguiente:")
    for i, ruta in enumerate(mejor_asignacion):
        camion = variables[i]
        paquetes_entregados = min(paquetes_rutas[ruta], capacidades_camiones[camion])
        print(f"Camion {camion} asignado a ruta {ruta} con {paquetes_entregados} paquetes entregados")
    print(f"Y fue la que menos paquetes perdido: {menor_paquetes_perdidos}")
else:
    print("No se encontró ninguna asignación válida.")
