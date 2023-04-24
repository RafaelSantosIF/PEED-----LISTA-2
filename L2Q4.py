def main():
    lista = []
    for i in range(5):
        lista.append(int(input("Numero {}: ".format(i+1))))
    conjunto = set(lista)
    print(conjunto)
    conjunto.remove(int(input("REMOVER NUMERO: ")))
    print(conjunto)
if __name__ == "__main__":
    main()
