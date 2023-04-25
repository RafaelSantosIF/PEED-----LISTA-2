def main():
    lista = []
    for i in range(5):
        lista.append(int(input("{}° Número: ".format(i+1))))
    conjunto = set(lista)
    if 3 in conjunto:
        print("Há o número 3!")
    else:
        print("Não há o número 3!")
if __name__ == "__main__":
    main()