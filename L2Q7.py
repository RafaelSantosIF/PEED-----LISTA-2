def main():
    lista = []
    for i in range(5):
        lista.append(int(input("{}° Número: ".format(i+1))))
    tupla = tuple(lista)
    print(tupla[0])
if __name__ == "__main__":
    main()