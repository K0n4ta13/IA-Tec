# 8-Puzzle

Este proyecto contiene una implementación de un solucionador del rompecabezas 8-Puzzle en Python. Utiliza el algoritmo de Búsqueda A* para encontrar la solución óptima y mostrar los pasos necesarios para resolver el rompecabezas desde un estado inicial dado hasta el estado objetivo.

## Ejemplo de Uso

Al ejecutar el programa, se mostrará la evolución del tablero paso a paso hasta alcanzar la solución.

```bash
uv run puzzle8.py
```

Salida esperada:

```
Estado inicial:
2 5 4
3 8 6
7 1  

Paso 1:
2 5 4
3 8  
7 1 6

...

Estado final alcanzado en X movimientos y Y segundos.
```
