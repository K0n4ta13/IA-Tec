class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None

    def insertar(self, nuevo_valor):
        if nuevo_valor < self.valor:
            if self.izq is None:
                self.izq = Nodo(nuevo_valor)
            else:
                self.izq.insertar(nuevo_valor)
        else:
            if self.der is None:
                self.der = Nodo(nuevo_valor)
            else:
                self.der.insertar(nuevo_valor)

    def inorden(self):
        if self.izq:
            self.izq.inorden()
        print(self.valor, end=" ")
        if self.der:
            self.der.inorden()

    def crear_arbol():
        top = int(input("Escriba la raiz: ")) 
        raiz = Nodo(top)
        cant_nodos = int(input("Cuantos nodos quieres? ")) 

        for i in range(cant_nodos):
            nodonue = int(input(f"Ingrese el nodo {i + 1}: "))  
            raiz.insertar(nodonue)

        return raiz

raiz = Nodo.crear_arbol()
print("ARBOL: ")
raiz.inorden()