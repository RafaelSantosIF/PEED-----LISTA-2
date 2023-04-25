def main():
    grafo = {}
    max = int(input("Número de Vértices: "))
    for x in range(max):
        vertice = input("Vertice: ")
        arestas = list(input("Vertices Adjascentes: "))
        grafo[vertice] = arestas
    print(grafo)
    ver, are = input("Aresta a Remover (X Y)\n: ").split()
    grafo[ver].remove(are)
    print(grafo)
if __name__ == "__main__":
    main()