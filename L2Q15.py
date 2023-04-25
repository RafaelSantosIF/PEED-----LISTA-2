def main():
    grafo = {}
    max = int(input("Número de Vértices: "))
    for x in range(max):
        vertice = input("Vertice: ")
        arestas = list(input("Vertices Adjascentes: "))
        grafo[vertice] = arestas
    if 'C' in grafo['A']:
        print("Aresta AC existe!")
    else:
        print("Aresta AC não existe!")
if __name__ == "__main__":
    main()
