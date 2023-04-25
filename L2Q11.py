def main():
    lista = []
    for i in range(10):
        lista.append(int(input("{}° Número: ".format(i+1))))
    print("Valores nos Índices Pares: ")
    for j in range(10):
        if j % 2 == 0:
            print("- ", lista[j])
if __name__ == "__main__":
    main()