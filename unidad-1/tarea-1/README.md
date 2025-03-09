# Árbol Binario de Búsqueda en Python

Este proyecto contiene una implementación simple de un Árbol Binario de Búsqueda (ABB) en Python. El código permite crear un árbol de nodos a partir de entradas del usuario, insertar nuevos nodos en el árbol y recorrerlo en orden (inorden).

## Descripción del Código

- **Clase `Nodo`**:  
  La clase `Nodo` representa cada nodo del árbol. Cada nodo almacena un `valor` y tiene dos referencias, `izq` (subárbol izquierdo) y `der` (subárbol derecho).

- **Método `insertar`**:  
  Este método inserta un nuevo valor en el árbol. Si el nuevo valor es menor que el valor del nodo actual, se inserta en el subárbol izquierdo; de lo contrario, se inserta en el subárbol derecho.

- **Método `inorden`**:  
  Realiza un recorrido en inorden del árbol, imprimiendo los valores de los nodos.

- **Función `crear_arbol`**:  
  Método estático que:
  - Solicita al usuario el valor de la raíz.
  - Pregunta cuántos nodos se desean agregar.
  - Inserta cada uno de los nodos proporcionados en el árbol.
  - Retorna la raíz del árbol creado.

## Ejemplo de Uso

Al ejecutar el programa, se te solicitará:

1. **Escribir la raíz**:  
   Ingresa el valor del nodo raíz.

2. **Cantidad de nodos**:  
   Indica cuántos nodos adicionales deseas agregar.

3. **Ingresar cada nodo**:  
   Ingresa cada uno de los valores para los nodos.

El programa mostrará el árbol recorrido en inorden, lo que corresponde a los valores ordenados de menor a mayor.
