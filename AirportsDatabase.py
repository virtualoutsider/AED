class Vertex(object):
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}
    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight
    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])
    def getConnections(self):
        return self.connectedTo.keys()
    def getId(self):
        return self.id
    def getWeight(self,nbr):
        return self.connectedTo[nbr]

#---------------------------------------------------------------------------------------------------

class Graph:
    def __init__(self):
        self.__graph_dict = {}
        self.numVertices = 0
    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.__graph_dict[key] = newVertex
        print(self.__graph_dict)
        return newVertex
    def getVertex(self,n):
        if n in self.__graph_dict:
            return self.__graph_dict[n]
        else:
             return None
    def __str__(self):
        text=''
        for n in self.__graph_dict:
            text+=n+' '
        return text
    def __contains__(self,n):
        return n in self.__graph_dict
    def addEdge(self,f,t,cost=0):
        if f not in self.__graph_dict:
            nv = self.addVertex(f)
        if t not in self.__graph_dict:
            nv = self.addVertex(t)
            self.__graph_dict[f].addNeighbor(self.__graph_dict[t], cost)
    def getVertices(self):
        return self.__graph_dict.keys()
    def __iter__(self):
        return iter(self.__graph_dict.values())
    
    def find_path(self, start_vertex, end_vertex, path=None): 
        if path == None:
            path = []
            graph = self.__graph_dict
            path = path + [start_vertex]
        if start_vertex == end_vertex:
            return path
        if start_vertex not in graph:
            return None
        for vertex in graph[start_vertex]:
            if vertex not in path:
                extended_path = self.find_path(vertex, end_vertex, path)
                if extended_path:
                    return extended_path
        return None

    def find_all_paths(self, start_vertex, end_vertex, path=[]):
        graph = self.__graph_dict
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return [path]
        if start_vertex not in graph:
            return []
        paths = []
        for vertex in graph[start_vertex]:
            if vertex not in path:
                extended_paths = self.find_all_paths(vertex, end_vertex, path)
                for p in extended_paths:
                    paths.append(p)
        return paths

    def profundidad(self,eleccion): #recorrido en profundidad
        visitados=[] 
        pila=[]
        imprimir=[]
        pila.append(eleccion) 
        visitados.append(eleccion) 
        if eleccion in self.__graph_dict: 
            while pila: 
                x = pila[-1]
                print ("Pila:",pila)
                imprimir.append(x)
                pila.remove(pila[-1])
                for key in self.__graph_dict[x]:
                    if key not in visitados:
                        visitados.append(key)
                        pila.append(key)

    def anchura(self, eleccion): #recorrido en anchura
        visitados = []
        cola = []
        imprimir = []
        cola.append(eleccion)
        visitados.append(eleccion)
        if eleccion in self.__graph_dict:  
            while cola:
                x = cola[0]
                imprimir.append(x)
                cola.pop(0)
                for key in self.__graph_dict[x]:
                    if key not in visitados:
                        visitados.append(key)
                        cola.append(key)

    def find_camino(self,start_vertex,end_vertex,path=[]):
        text = "Aeropuertos a tomar:\n"
        graph = self.__graph_dict
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            print(path)
            #return path
            for item in range(0,len(path)):
                print (item)
                if item != len(path)-1:
                    text += path[item] + " hacia "
                else:
                    text += path[item]
            return [text]
        if start_vertex not in graph:
            return []
        paths = []
        for vertex in graph[start_vertex]:
            for dest in vertex:
                if type(dest) == str: 
                    if dest not in path:
                        extended_paths = self.find_camino(dest, end_vertex, path)
                        for p in extended_paths:
                            paths.append(p)
        return paths
 

'''class Graph(object):
    def _init_(self,graph_dict=None):
        if graph_dict == None:
            graph_dict = []            
        self.__graph_dict = graph_dict

    def vertices(self):
        return list(self.__graph_dict.keys())   

    def edges(self):
        return self.__generate_edges()         

    def add_vertex(self,vertex): #agregar un vertice
        if vertex not in self.__graph_dict:     
            self.__graph_dict[vertex] = []      

    def add_edge(self,edge): #agregar una arista
        edge = set(edge)
        vertex1 = edge.pop()
        if edge:
            vertex2 = edge.pop()
        else:
            vertex2 = vertex1
        if vertex1 in self.__graph_dict:
            self.__graph_dict[vertex1].append(vertex2)
        else:
            self.__graph_dict[vertex1] = [vertex2]
    
    def remove_edge(self,edge): #eliminar una arista
        edge = set(edge)
        vertex1 = edge.pop() #es el origen
        if edge:
            vertex2 = edge.pop() #es el destino
        else:
            vertex2 = vertex1
        if vertex1 in self.__graph_dict:
            if vertex2 in vertex1.values(): 
                self.__graph_dict[vertex1].pop(vertex2)
        else:
            print ("No existe el origen")

    def __generate_edges(self): #generar arista entre dos vertices
        edges = []
        for vertex in self.__graph_dict:
            for neighbour in self.__graph_dict[vertex]:
                if (neighbour, vertex) not in edges:
                    edges.append({vertex,neighbour})
        return edges

    def _str_(self):
        res = "vertices: "
        for k in self.__graph_dict:
            res += str(k) + " "
        res += "\nedges"
        for edge in self.__generate_edges():
            res += str(edge)+" "
        return res
        
    def find_isolated_vertices(self):
 
        graph = self.__graph_dict
        isolated = []
        for vertex in graph:
            print(isolated, vertex)
            if not graph[vertex]:
                isolated += [vertex]
        return isolated

    def is_connected(self,vertices_encontrados = None,start_vertex = None): #determinar conectividad del grafo
        if vertices_encontrados is None:
            vertices_encontrados = set()
        gdict = self.__graph_dict
        vertices = list(gdict.keys())
        if not start_vertex:
            start_vertex = []
        vertices_encontrados.add(start_vertex)
        if len(vertices_encontrados) != len(vertices):
            for vertex in gdict[start_vertex]:
                if vertex not in vertices_encontrados:
                    if self.is_connected(vertices_encontrados,vertex):
                        return True
        else:
            return True
        return False

    def vertex_degree(self, vertex):
        adj_vertices = self.__graph_dict[vertex]
        degree = len(adj_vertices) + adj_vertices.count(vertex)
        return degree

    def find_path(self, start_vertex, end_vertex, path=None): 
        if path == None:
            path = []
            graph = self.__graph_dict
            path = path + [start_vertex]
        if start_vertex == end_vertex:
            return path
        if start_vertex not in graph:
            return None
        for vertex in graph[start_vertex]:
            if vertex not in path:
                extended_path = self.find_path(vertex, end_vertex, path)
                if extended_path:
                    return extended_path
        return None

    def find_all_paths(self, start_vertex, end_vertex, path=[]):
        graph = self.__graph_dict
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return [path]
        if start_vertex not in graph:
            return []
        paths = []
        for vertex in graph[start_vertex]:
            if vertex not in path:
                extended_paths = self.find_all_paths(vertex, end_vertex, path)
                for p in extended_paths:
                    paths.append(p)
        return paths

    def profundidad(self,eleccion): #recorrido en profundidad
        visitados=[] 
        pila=[]
        imprimir=[]
        pila.append(eleccion) 
        visitados.append(eleccion) 
        if eleccion in self.__graph_dict: 
            while pila: 
                x = pila[-1]
                print ("Pila:",pila)
                imprimir.append(x)
                pila.remove(pila[-1])
                for key in self.__graph_dict[x]:
                    if key not in visitados:
                        visitados.append(key)
                        pila.append(key)

    def anchura(self, eleccion): #recorrido en anchura
        visitados = []
        cola = []
        imprimir = []
        cola.append(eleccion)
        visitados.append(eleccion)
        if eleccion in self.__graph_dict:  
            while cola:
                x = cola[0]
                imprimir.append(x)
                cola.pop(0)
                for key in self.__graph_dict[x]:
                    if key not in visitados:
                        visitados.append(key)
                        cola.append(key)'''

