def main():
    grafo = {}
    max = int(input("Número de Vértices: "))
    for x in range(max):
        vertice = input("Vertice: ")
        grafo[vertice] = []
    print(grafo)
    max = int(input("Número de Arestas: "))
    for y in range(max):
        origem, destino = input("Aresta (X Y): ").split()
        grafo[origem].append(destino)
        grafo[destino].append(origem)
    print(grafo)
if __name__ == "__main__":
    main()
