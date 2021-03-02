from listacircularsimple import ListaCircular


class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
    

class ListaSimpleEnlazada:
    # lista = ListaCircular()
    tamanio = 0
    def __init__(self):
        self.primero = None
        self.ultimo = None

    
    def isVacia(self):
        if self.primero == None:
            return True
        else:
            return False


    # def getSize():
    #     aux = self.primero
    #     contador = 0
    #     while aux != None:
    #         contador = contador + 1
    #         aux = aux.siguiente
    #     return contador
    
    
    
    def pop(self):
        if self.isVacia() == True:
            print("La lista esta vacia :D")
            
        elif self.primero  == self.ultimo:
            self.primero = None
            self.ultimo = None
            print("Ultimo elemento eliminado, lista vacia :D")
        else:
            validar = True
            temp = self.primero
            while(temp.siguiente != self.ultimo):
                temp = temp.siguiente
            temp.siguiente = None
            self.ultimo = temp


    def agregarUltimo(self, dato):
        if self.isVacia() == True:
            self.primero = self.ultimo = Nodo(dato)
            # self.tamanio = self.tamanio + 1 
        else:
            aux = self.ultimo
            self.ultimo = aux.siguiente = Nodo(dato)
            # self.tamanio = self.tamanio + 1



    
    # def __str__(self):
    #     aux = self.primero
    #     lst = []
    #     while aux != None:
    #         cadena = aux.dato
    #         lst.append(cadena)
    #         aux = aux.siguiente
    #     return lst


    def recorrido(self):
        aux = self.primero
        
        while aux != None:
            print(aux.dato)
            # print(aux.dato.datos.__str__())
            aux = aux.siguiente
    


    def buscar(self, nombre):
        aux = self.primero
        encontrado = False

        if self.isVacia == True:
            print("No hay elementos en la lista :D")
        else:
            contador = 0
            while aux != None:
                if aux.dato.nombre == nombre:
                    return aux.dato
                    # return aux.dato.nombre
                    encontrado = True
                    break
                else:
                    aux = aux.siguiente
                    contador = contador + 1    
            
            if encontrado == False:
                print("El elemento no se encuentra en la lista.")

    

    def buscarPosicion(self, posicion):
        aux = self.primero
        encontrado = False

        if self.isVacia == None:
            print("No hay elementos en la lista :D")
        else:
            while aux != None:
                if aux.dato.nombre == nombre:
                    # print("ENCONTRADO: ", aux.dato.nombre)
                    # return aux.dato.nombre
                    encontrado = True
                    break
                else:
                    aux = aux.siguiente    
            
            if encontrado == False:
                print("El elemento no se encuentra en la lista.")


                

# lista = ListaSimpleEnlazada()
# lista.agregarUltimo(22)
# lista.agregarUltimo(2)
# lista.agregarUltimo(5)
# lista.agregarUltimo(10)

# lista.recorrido()


# while lista.isVacia() == False:
#     lista.pop()

# lista.recorrido()

