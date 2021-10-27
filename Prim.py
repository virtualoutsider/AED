
import os

def Prime(self, grafo):
  print("Hola :)")
  listaVisitados = []
  grafoResultante = {}
  listaOrdenada = []

  #1.- ELEGIR NODO ORIGEN AL AZAR O PEDIRLO AL USUARIO
  origen = input("\nIngresa el nodo origen: ")
  #2.- AGREGARLO A LA LISTA DE VISITADOS
  listaVisitados.append(origen)

  #3.- AGREGAR SUS ADYACENTES A LA LISTA ORDENADA
  for destino, peso in grafo[origen]:
    listaOrdenada.append((origen, destino, peso))
  pos=0
  act=0
  listAux=[] 
  for i in range(len(listaOrdenada)):
      listAux=listaOrdenada[i]
      act=listaOrdenada[i][2]
      pos=i
      while pos> 0 and listaOrdenada[pos-1][2] > act:
          listaOrdenada[pos] = listaOrdenada[pos-1]
          pos=pos-1
      listaOrdenada[pos]=listAux

  #4.- MIENTRAS LA LISTA ORDENADA NO ESTE VACIA, HACER:
  while listaOrdenada:
    #5.-TOMAR VERTICE DE LA LISTA ORDENADA Y ELIMINARLO
    vertice = listaOrdenada.pop(0)
    d = vertice[1]

    #6.-SI EL DESTINO NO ESTA EN LA LISTA DE VISITADOS
    if d not in listaVisitados:
      #7.- AGREGAR A LA LISTA DE VISITADOS EN NODO DESTINO
      listaVisitados.append(d)
      #8.- AGREGAR A LA LISTA ORDENADA LOS ADYACENTES DEL NODO DESTINO 
      #"d" QUE NO HAN SIDO VISITADOS
      for key, lista in grafo[d]:
        if key not in listaVisitados:
          listaOrdenada.append((d, key, lista))
      #####ORDENAMIENTO APLICADO A LA LISTA :
      listaOrdenada = [(c,a,b) for a,b,c in listaOrdenada]
      listaOrdenada.sort()
      listaOrdenada = [(a,b,c) for c,a,b in listaOrdenada]
      #9.-AGREGAR VERTICE AL GRAFO RESULTANTE
      # PARA COMPRENDER MEJOR, EN LAS SIGUIENTES LINEAS SE TOMA EL "VERTICE", QUE EN ESTE CASO
      # ES UNA TUPLA QUE CONTIENE TRES VALORES; EL VERTICE EN SU POSICI�N 0 ES EL VALOR DEL NODO ORIGEN
      # EL V�RTICE EN SU POSICI�N 1 ES EL NODO DESTINO, Y EL V�RTICE EN SU POSICI�N 2 ES EL PESO DE LA ARISTA ENTRE AMBOS NODOS,
      # Y A CONTINUACI�N SE AGREGAN ESOS VALORES AL GRAFO
      origen  = vertice[0]
      destino = vertice[1]
      peso    = vertice[2]

      if origen in grafoResultante: #SI AMBOS NODOS EXISTEN EN EL GRAFO, SE AGREGAN A LA LISTA
        if destino in grafoResultante:
          lista = grafoResultante[origen]
          grafoResultante[origen] = lista + [(destino, peso)]
          lista = grafoResultante[destino]
          lista.append((origen, peso))
          grafoResultante[destino] = lista
        else: 
          grafoResultante[destino] = [(origen, peso)]
          lista = grafoResultante[origen]
          lista.append((destino, peso))
          grafoResultante[origen] = lista
      elif destino in grafoResultante:
        grafoResultante[origen] = [(destino, peso)]
        lista = grafoResultante [destino]
        lista.append((origen, peso))
        grafoResultante[destino] = lista
      else:
        grafoResultante[destino] = [(origen, peso)]
        grafoResultante[origen] = [(destino, peso)]
        
  print("\n\nGrafo resultante:\n")
  for key, lista in grafoResultante.items():
    print(key)
  print(lista)

'''PRIM VS KRUSCAL:
-Prim: 1. Seleccione un nodo arbitrario del gráfico y agréguelo al árbol T 
(que será el primer nodo)
2. Considere los pesos de cada borde conectado a los nodos en el árbol y seleccione el mínimo. 
Agregue el borde y el nodo en el otro extremo del árbol T y elimine el borde del gráfico. 
(Seleccione cualquiera si existen dos o más mínimos)
3. Repita el paso 2, hasta que se agreguen n-1 bordes al árbol.
-Kruscal: 1. Seleccione el arco con el menor peso de todo el gráfico, añádalo al árbol y elimínelo..
2. Del resto, seleccione el borde menos ponderado, de manera que no forme un ciclo. 
Agregue el borde al árbol y elimínelo del gráfico. 
(Seleccione cualquiera si existen dos o más mínimos)
3. Repita el proceso en el paso 2. COMO TRABAJA CON LAS ARISTAS, PARA APLICAR KRUSCAL EL GRAFO NO NECESITA ESTAR CONECTADO.
ENTONCES, LAS DIFERENCIAS SON: 
• El algoritmo de Prim se inicializa con un nodo, mientras que el algoritmo de Kruskal se inicia con un borde.
• Los algoritmos de Prim abarcan desde un nodo a otro, mientras que el algoritmo de Kruskal selecciona los bordes de manera que la posición del borde no se base en el último paso.
• En el algoritmo de prim, el gráfico debe ser un gráfico conectado, mientras que el de Kruskal también puede funcionar en gráficos desconectados.'''

