def main():
    lista = []
    for i in range(10):
        lista.append(int(input("{}° Número: ".format(i+1))))
    conjunto = set(lista)
    print(conjunto)
    aux = set(conjunto)
    for j in conjunto:
        if j % 2 == 0:
            aux.remove(j)
    conjunto = set(aux)
    print(conjunto)
    
if __name__ == "__main__":
    main()

