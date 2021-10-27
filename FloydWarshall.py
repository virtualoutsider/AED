'''INF = 999999999

class Floyd_Warshall (object):
    
    def printSolution(self, distGraph): #muestra la matriz de caminos 
        string = "inf"
        nodes =distGraph.keys()
        for n in nodes:
            print ("\t%6s"%(n)),
        print (" ")

        for i in nodes:
            print("%s"%(i)),
            for j in nodes:
                if distGraph[i][j] == INF: #si la interseccion es infinita no se hace nada
                    print ("%10s"%(string)),
                else:
                    print ("%10s"%(distGraph[i][j])),
            print(" ")


    def floydWarshall(self, graph):
        nodes = graph.keys()

        distance = {}

        for n in nodes: #todos los vertices, inicializa para cada nodo
            distance[n] = {}

            for k in nodes: #longitud en cada vuelta, agrega un enlace mas que permite aumentar en uno la longitud con k, que representa la longitud
                distance[n][k] = graph[n][k]

        for k in nodes: #construye la matriz de caminos, para cada matriz construida
            for i in nodes: #vertice inicio
                for j in nodes: #vertice final
                    distance[i][j] = min (distance[i][j], distance[i][k] + distance[k][j]) #aca se construye la matriz de caminos
        printSolution(distance)

    '''if __name__ == '__main__':
        graph = {   u'node_10': {   u'node_10': 0,
                    u'node_4': 1,
                    u'node_5': 0,
                    u'node_6': 0,
                    u'node_7': 0,
                    u'node_8': 0,
                    u'node_9': 0},
    u'node_4': {   u'node_10': 0,
                u'node_4': 1,
                u'node_5': 1,
                u'node_6': 0,
                u'node_7': 0,
                u'node_8': 0,
                u'node_9': 0},
    u'node_5': {   u'node_10': 0,
                u'node_4': 0,
                u'node_5': 0,
                u'node_6': 1,
                u'node_7': 0,
                u'node_8': 1,
                u'node_9': 0},
    u'node_6': {   u'node_10': 0,
                u'node_4': 0,
                u'node_5': 0,
                u'node_6': 1,
                u'node_7': 1,
                u'node_8': 0,
                u'node_9': 0},
    u'node_7': {   u'node_10': 0,
                u'node_4': 0,
                u'node_5': 0,
                u'node_6': 0,
                u'node_7': 1,
                u'node_8': 1,
                u'node_9': 0},
    u'node_8': {   u'node_10': 0,
                u'node_4': 0,
                u'node_5': 0,
                u'node_6': 0,
                u'node_7': 0,
                u'node_8': 0,
                u'node_9': 1},
    u'node_9': {   u'node_10': 1,
                u'node_4': 0,
                u'node_5': 1,
                u'node_6': 0,
                u'node_7': 0,
                u'node_8': 0,
                u'node_9': 0}}'''

    #floydwarshall (graph)'''


class FloydWarshall(object):
    def floyd_warshall(self): #se crea la primera version de la matriz
                              #utilizando dos ciclos para llenarlos con las aristas
                              #establecidas del grafo y los ceros (o tres si rellenamos con infinitos)
                              #este bloque crea la primera matriz con un solo ciclo
        nodes = list(self.graph.nodes)

        for i in nodes: 
            dict_i = {}
            for j in nodes: 
                if i == j:
                    dict_i[j] = 0
                    continue
                try:
                    dict_i[j] = self.graph[i][j]['weight']#se compara la suma de las filas y columnas con la interseccion
                except:
                    dict_i[j] = float("inf") #puede ser infinita

            self.distances[i] = dict_i

        for i in nodes:
            for j in nodes:
                for k in nodes:
                    ij = self.distances[i][j]
                    ik = self.distances[i][k]
                    kj = self.distances[k][j]

                    if ij > ik + kj:
                        self.distances[i][j] = ik + kj #aqui se realiza el intercambio que me determina el camino a recorrer

        return self.distances
    def print_distances(self): #metodo para imprimir el diccionario resultado
        printt = ""
        for i in self.distances:
            printt = printt + str(i) + ": \t"
            for j in self.distances[i]:
                printt = printt + str(self.distances[i][j]) + "\t"
            printt = printt + "\n"
        print("\n------------------------------------")
        print(printt)
        return