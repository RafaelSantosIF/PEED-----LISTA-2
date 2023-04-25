def main():
    lista, lista2 = [], []
    for i in range(10):
        lista.append(int(input("{:02}° Número: ".format(i+1))))
    for x in range(10):
        lista2.append(lista[x]*2)
    print(lista)
    print(lista2)

if __name__ == "__main__":
    main()
