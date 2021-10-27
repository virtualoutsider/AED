import os
from collections import defaultdict
class Graphdis:
  def __init__(self): #constructor 
    self.nodes = set()
    self.edges = defaultdict(list)
    self.distances = {}

  def add_node(self, value): #agrega nodos
    self.nodes.add(value)

  def add_edge(self, from_node, to_node, distance): #agrega aristas teniendo un nodo origen, uno destino y una distancia
    self.edges[from_node].append(to_node)
    self.edges[to_node].append(from_node)
    self.distances[(from_node, to_node)] = distance

def dijsktra(self, graph, initial):
  visited = {initial: 0}
  path = {}

  nodes = set(graph.nodes)

  while nodes: #usa una lista de prioridad basada en monticulos minimos
    min_node = None
    for node in nodes:
      if node in visited:
        if min_node is None:
          min_node = node
        elif visited[node] < visited[min_node]:#la cantidad de nodos de la lista de prioridad 
                                              #debe ser igual a la cantidad de vertices del grafo
          min_node = node

    if min_node is None:
      break

    nodes.remove(min_node) #se etiqueta el nodo minimo como procesado
    current_weight = visited[min_node] #mi tamaño actual es determinado por los nodos visitados

    for edge in graph.edges[min_node]: #por cada arista de mi nodo minimo existente en el grafo
      weight = current_weight + graph.distance[(min_node, edge)] #el peso es mi peso anterior sumado al de la nueva arista
      if edge not in visited or weight < visited[edge]: #si el nodo no ha sido agregado a visitados o el peso es menor 
        visited[edge] = weight #igualo ese peso a mi arista visitada
        path[edge] = min_node #selecciono esa arista para el camino de mi nodo

  return visited, path

grafo = {'a': [('p',4), ('j',15), ('b',1)],
      'b': [('a',1), ('d',2), ('e',2), ('c',2)],
  'j': [('a',15),('c',6)],
  'p': [('a',4),('d',8)],
  'd': [('b',2), ('g',3),('p',8)],
  'e': [('b',2), ('g',9), ('f',5), ('c',2),('h',4)],
  'c': [('b',2), ('e',2), ('f',5), ('i',20),('j',6)],
  'g': [('d',3), ('e',9), ('h',1)],
  'f': [('h',10), ('e',5), ('c',5),('i',2)],
  'i': [('c',20),('f',2)],
  'h': [('g',1),('e',4),('f',10)] 
}
print (grafo, 'a')


    