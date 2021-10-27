parent = dict()
rank = dict()

def make_set(vertice): #inicializamos cada componente para obtener componentes conexas iniciales
    parent[vertice] = vertice
    rank[vertice] = 0

def find(vertice): #buscamos el vertice que corresponde a la arista minima
    if parent[vertice] != vertice:
        parent[vertice] = find(parent[vertice])
    return parent[vertice]

def union(vertice1, vertice2): #UNE LOS DOS VERTICES QUE NO SE ENCUENTREN EN UNA MISMA COMPONENTE CONEXA 
    root1 = find(vertice1)
    root2 = find(vertice2)
    if root1 != root2: #no se encuentran en la misma componente conexa
        if rank[root1] > rank[root2]: #no existen ciclos
            parent[root2] = root1
        else:
            parent[root1] = root2 #si ya son conexos, no se crea la union
            if rank[root1] == rank[root2]: rank[root2] += 1

def kruskal(graph):
    for vertice in graph['vertices']:
        make_set(vertice)

    minimum_spanning_tree = set() #creo un set vacio que sera mi nuevo grafo minimo
    edges = list(graph['edges'])
    edges.sort() #ordeno de menor a mayor segun el peso de las aristas
    for edge in edges:
        weight, vertice1, vertice2 = edge
        if find(vertice1) != find(vertice2): #no estan en la misma componente conexa
            union(vertice1, vertice2) #llamo a union para confirmar la arista
            minimum_spanning_tree.add(edge) #agrego esa arista a mi set minimo
    return minimum_spanning_tree #mi nuevo grafo minimo

graph = {
        'vertices': ['A', 'B', 'C', 'D', 'E', 'F'],
        'edges': set([
            (1, 'A', 'B'),
            (5, 'A', 'C'),
            (3, 'A', 'D'),
            (4, 'B', 'C'),
            (2, 'B', 'D'),
            (1, 'C', 'D'),
            ])
        }
minimum_spanning_tree = set([
            (1, 'A', 'B'),
            (2, 'B', 'D'),
            (1, 'C', 'D'),
            ])
assert kruskal(graph) == minimum_spanning_tree
print(kruskal(graph))

'''Creo una lista con los conjuntos de vértices por un lado y el peso de sus aristas por el otro.
 Kruscal se fija primero en el peso de las aristas, que están ordenadas de menor a mayor, y luego pasa a la parte
 de vertices a verificar que esos dos vértices unidos por la arista que le interesa no estén ya conectados por
 otra arista (componente conexa). Si no lo están, agrega esa arista a la nueva lista paras formar el arbol de expansion
 minima, si si lo están, simplemente no lo agrega. Así sucesivamente hasta recorrer todos los vertices.
 Finalmente, debemos obtener un arbol de expansion minima conexo y sin ciclos para que el algoritmo haya sido eficiente, 
 para verificar esto, basta con comparar el tamaño de mi nuevo árbol con la cantidad de vertices originales.
 Si nuevoarbol=vertices-1 es válido.
 Si nuevoarbol tiene menor cantidad que vertices-1, no es conexo
 Si nuevoarbol tiene mayor cantidad que vertices-1, posee ciclos'''