from AirportsDatabase import Vertex, Graph
# from Prim import Prime
# from Kruscal import Kruscal
# from FloydWarshall import FloydWarshall
# from dijsktra_graph import Graphdis

opcion=0
opcion1=0
opcion2=0
opcion3=0
opcion4=0
opcion5=0
opcion6=0
opcion7=0
opcion8=0
opcion9=0

grafito={
    1:3, 2:1, 3:2
}
grafo=Graph()
vertice=Vertex(1)
#prim=Prim()
#kruscal=Kruscal()
# graphdis=Graphdis()

while (opcion != 9):
    opcion = int(input("\n-Menú-\n----------\n\t" + 
"1. Agregar un aeropuerto.\n\t"+
"2. Agregar una ruta y su distancia.\n\t"+
"3. Camino más corto desde un aeropuerto en particular hacia todos los demás. \n\t"+ #(dijkstra)
"4. Mostrar rutas de A a B.\n\t"+
"5. Mostrar ruta más corta entre A y B.\n\t"+
"6. Encontrar rutas de A a B según criterio de distancia.\n\t"+
"7. Recorrido en anchura.\n\t"+
"8. Recorrido en profundidad.\n\t"+
"9. Salir.\n\t"+
"Por favor, seleccione una opción ingresando el número de su índice: "))
    
    if (opcion == 1):
        
        while (opcion1 != 2):
            opcion1=int(input("\n\t1. Selecione esta opción para continuar con el ingreso del vértice o aeropuerto.\n\t"+
                          "2.Volver.\n\t"))
            if (opcion1 == 1):
                nuevovertice= input("Ingrese el nombre del aeropuerto: ")
                grafo.addVertex(nuevovertice)
                print(grafo)
            elif (opcion == 2):
                break
            else:
                print("Opción ingresada no válida")

    if (opcion == 2):
        
        while (opcion2 != 2):
            opcion2=int(input("\n\t1.Selecione esta opción para continuar con el ingreso de la arista o ruta\n\t"+
                            "2.Volver.\n\t"))
            if (opcion2 == 1):
                origen= input("Ingrese el origen: ")
                destino= input("Ingrese el destino: ") 
                distancia= input("Ingrese la distancia: ")
                vertice.addNeighbor((origen, destino, distancia))
            elif (opcion2 == 2):
                break
            else:
                print("Opción ingresada no válida")
    
    if (opcion == 3):
        
        while (opcion1 != 2):
            opcion1=int(input("\n\t1. Selecione esta opción para continuar con la búsqueda de rutas.\n\t"+
                          "2.Volver.\n\t"))
            if (opcion1 == 1):
                aerodijkstra= input("Ingrese el aeropuerto del que desea conocer las conexiones: ")
                graphdis.dijsktra(grafito, aerodijkstra)
            elif (opcion == 2):
                break
            else:
                print("Opción ingresada no válida")

    if (opcion == 4):
        
        while (opcion1 != 2):
            opcion1=int(input("\n\t1. Selecione esta opción para continuar con el ingreso de los aeropuertos de los que desea conocer las conexiones disponibles. \n\t"+
                          "2.Volver.\n\t"))
            if (opcion1 == 1):
                aeroorigen= input("Ingrese el aeropuerto origen: ")
                aerodestino= input("Ingrese el aeropuerto destino: ")
                grafo.find_camino(aeroorigen, aerodestino) 
            elif (opcion == 2):
                break
            else:
                print("Opción ingresada no válida")


    