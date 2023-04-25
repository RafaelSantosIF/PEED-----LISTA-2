def main():
    lista = []
    for i in range(5):
        lista.append(int(input("{}° Número: ".format(i+1))))
    conjunto = set(lista)
    print("Este conjunto possui {} elementos.".format(len(conjunto)))
if __name__ == "__main__":
    main()