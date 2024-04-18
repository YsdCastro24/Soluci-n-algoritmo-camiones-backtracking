# Solución-algoritmo-camiones-backtracking
python algoritmo backtraking

El problema se describe de la siguiente manera:

La empresa de transporte tiene tres camiones (C1, C2 y C3) y tres rutas (R1, R2 y R3) para entregar paquetes a diferentes destinos.
Cada camión tiene una capacidad máxima diferente: C1 puede transportar hasta 10 paquetes, C2 hasta 8 paquetes, y C3 hasta 6 paquetes.
Cada ruta tiene un número diferente de paquetes que deben entregarse: R1 tiene 12 paquetes, R2 tiene 7 paquetes, y R3 tiene 5 paquetes.
El objetivo de la empresa es asignar los camiones a las rutas de forma que se entreguen todos los paquetes y se maximice la capacidad utilizada de cada camión.


El código busca resolver este problema mediante la técnica de backtracking. El proceso general es el siguiente:

Declaración de variables: Se definen las variables c1, c2, y c3 para representar los camiones, y r1, r2, y r3 para representar las rutas.
Verificación de restricciones: Se utiliza la función comprobar para verificar las restricciones del problema:
Que cada camión tenga asignada una única ruta.
Que se entreguen todos los paquetes.
Que la capacidad de cada camión no se vea sobrecargada.
Que cada ruta se asigne a un único camión.
Backtracking: La función backtracking se encarga de buscar posibles asignaciones de rutas a camiones utilizando la técnica de backtracking para explorar todas las combinaciones posibles. Se lleva un registro de la mejor asignación encontrada, maximizando la capacidad utilizada y minimizando la pérdida de paquetes.
Búsqueda de la mejor asignación: El algoritmo recorre todas las posibles asignaciones de rutas a camiones, y determina cuál es la mejor asignación según el criterio definido.
Impresión de resultados: Una vez que se encuentra la mejor asignación, se imprime la ruta asignada para cada camión y la cantidad de paquetes entregados, junto con la cantidad de paquetes perdidos.