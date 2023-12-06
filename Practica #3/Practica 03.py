#Libreria para crear arboles
import heapq
#Libreria para el tiempo
import time

#Definimos una clase que representara un grafo
class Graph:
    #Tiene un diccionario llamado vertices que manda cada vertice a una lista de tuplasque representa las conexiones desde ese vertice a otro y sus pesos
    def __init__(self):
        self.vertices = {}
    #Este metodo agregara vertices al grafo     
    def add_vertex(self, vertex):
        #Y los inicializara con una lista vacia de conexiones
        self.vertices[vertex] = []
    #Este meyodo se encarga de agregar aritas al grafo    
    def add_edge(self, from_vertex, to_vertex, weight):
        #Agrega tuplas que indica de que vertice a que vertice va la arista y su peso
        self.vertices[from_vertex].append((to_vertex, weight))
        
#Esta funcion toma un grafo y un vertice de inicio como entrada
def dijkstra(graph, start_vertex):
    #Inicializa un diccionario que recorrera cada vertice a la distamcia minima desde e del inicio
    distances = {vertex: float('infinity') for vertex in graph.vertices}
    #Todas las distancias se inicializan en infinito excepto la del inicio
    distances[start_vertex] = 0
    #Inicializamos una cola de prioridad como una lista de tuplasdonde cada tupla tiene la distancia actual y el vertice correspondiente
    priority_queue = [(0, start_vertex)]
    
    #En el bucle principla mientras la variable anterior este vacia, extraemos el vertice con la distancia minima actual desde la variable anterior
    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)
        #Si la distancia actual es mayor que la distancia conocida desde el vértice de inicio, se ignora y se pasa al siguiente ciclo del bucle
        if current_distance > distances[current_vertex]:continue
        #Itera sobre los vertices vecinos qu tenga el actual y calcula la distancia acumulada desde el vertice del inicio
        for neighbor, weight in graph.vertices[current_vertex]:
            distance = current_distance + weight
            #Si la nueva distancia es menor que la distancia que llevamso desde el vertice de inciio hasta el vecino
            if distance < distances[neighbor]:
                #Actualizaremos la distancia conocida 
                distances[neighbor] = distance
                #Y agregaremos el vecino a la cola de prioridad con la nueva distancia
                heapq.heappush(priority_queue, (distance, neighbor))

    #Luego de que la cola de prioridad este vacia y todas las distancias hayan sido actualizadas, se devolvera el diccionario distancias             
    return distances

def Tiempo_ejecucion(funcion, *args):
    inicio = time.time()
    resultado = funcion(*args)
    fin = time.time()
    tiempo_ejecucion = fin - inicio
    return resultado, tiempo_ejecucion

print("\nAlgoritmo de Dijkstra")

#Caso de prueba 1
grafo = Graph()
grafo.add_vertex("A")
grafo.add_vertex("B")
grafo.add_vertex("C")
grafo.add_vertex("D")
grafo.add_edge("A", "B", 2)
grafo.add_edge("A", "C", 1)
grafo.add_edge("B", "D", 3)
grafo.add_edge("C", "D", 4)

#Luego llamamos a la funcion dijkstra con el grafo y el vertice de inicio a 
start_vertex = "A"
resultado = dijkstra(grafo, start_vertex)
#Al final imprimimos el resultado
resultado, tiempo = Tiempo_ejecucion(dijkstra, grafo, start_vertex)
print("\n-> Ejemplo #1: ")
print(f"   Caminos mínimos desde {start_vertex}: {resultado}")
print(f"   Tiempo de ejecución: {tiempo} segundos")

#Caso de prueba 2
grafo2 = Graph()
grafo2.add_vertex("M")
grafo2.add_vertex("N")
grafo2.add_vertex("O")
grafo2.add_vertex("P")
grafo2.add_edge("M", "N", 5)
grafo2.add_edge("M", "O", 6)
grafo2.add_edge("M", "P", 3)
grafo2.add_edge("N", "P", 12)
grafo2.add_edge("O", "P", 9)

start_vertex2 = "M"
resultado2, tiempo2 = Tiempo_ejecucion(dijkstra, grafo2, start_vertex2)
print("\n-> Ejemplo #3: ")
print(f"   Caminos mínimos desde {start_vertex2}: {resultado2}")
print(f"   Tiempo de ejecución: {tiempo2} segundos")

# Caso de prueba 3
grafo3 = Graph()
grafo3.add_vertex("A")
grafo3.add_vertex("B")
grafo3.add_vertex("C")
grafo3.add_vertex("D")
grafo3.add_vertex("E")
grafo3.add_vertex("F")
grafo3.add_vertex("G")
grafo3.add_edge("A", "B", 2)
grafo3.add_edge("B", "C", 1)
grafo3.add_edge("C", "D", 3)
grafo3.add_edge("A", "E", 4)
grafo3.add_edge("E", "F", 5)
grafo3.add_edge("F", "G", 2)
grafo3.add_edge("C", "G", 2)

start_vertex3 = "A"
resultado3, tiempo3 = Tiempo_ejecucion(dijkstra, grafo3, start_vertex3)
print("\n-> Ejemplo #4: ")
print(f"   Caminos mínimos desde {start_vertex3}: {resultado3}")
print(f"   Tiempo de ejecución: {tiempo3} segundos")

#Caso de prueba 4
grafo4 = Graph()
grafo4.add_vertex("X")
grafo4.add_vertex("Y")
grafo4.add_vertex("Z")
grafo4.add_vertex("W")
grafo4.add_vertex("V")
grafo4.add_edge("X", "Y", 4)
grafo4.add_edge("Y", "Z", 1)
grafo4.add_edge("Y", "V", 3)
grafo4.add_edge("X", "W", 2)
grafo4.add_edge("W", "V", 5)

start_vertex4 = "X"
resultado4, tiempo4 = Tiempo_ejecucion(dijkstra, grafo4, start_vertex4)
print("\n-> Ejemplo #5: ")
print(f"   Caminos mínimos desde {start_vertex4}: {resultado4}")
print(f"   Tiempo de ejecución: {tiempo4} segundos")

#Caso de prueba 5
grafo5 = Graph()
grafo5.add_vertex("1")
grafo5.add_vertex("2")
grafo5.add_vertex("3")
grafo5.add_vertex("4")
grafo5.add_vertex("5")
grafo5.add_edge("1", "2", 2)
grafo5.add_edge("2", "3", 1)
grafo5.add_edge("2", "5", 1)
grafo5.add_edge("1", "4", 3)
grafo5.add_edge("4", "5", 4)

start_vertex5 = "1"
resultado5, tiempo5 = Tiempo_ejecucion(dijkstra, grafo5, start_vertex5)
print("\n-> Ejemplo #6: ")
print(f"   Caminos mínimos desde {start_vertex5}: {resultado5}")
print(f"   Tiempo de ejecución: {tiempo5} segundos")


