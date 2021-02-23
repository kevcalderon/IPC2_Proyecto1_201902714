from listacircularsimple import ListaCircular

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
    

class ListaSimpleEnlazada:
    lista = ListaCircular()
    def __init__(self):
        self.primero = None
        self.ultimo = None

    
    def isVacia(self):
        return self.primero == None
    
    
    def agregarUltimo(self, dato):
        if self.isVacia() == True:
            self.primero = self.ultimo = Nodo(dato)
        else:
            aux = self.ultimo
            self.ultimo = aux.siguiente = Nodo(dato)
            
    
    def recorrido(self):
        aux = self.primero
        
        while aux != None:
            print(aux.dato.nombre)
            print(aux.dato.fila)
            print(aux.dato.columna)       
            aux = aux.siguiente
    

# lista = ListaSimpleEnlazada()
# lista.agregarUltimo(12)
# lista.agregarUltimo(2)
# lista.agregarUltimo(5)
# lista.agregarUltimo(10)

# lista.recorrido()

# lista.agregarUltimo(100)


# lista.recorrido()

