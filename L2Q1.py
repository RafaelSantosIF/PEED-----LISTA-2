def main():
    na = input("Nome: ")
    nb = input("Nome: ")
    nc = input("Nome: ")
    nd = input("Nome: ")
    ne = input("Nome: ")
    lista = [na, nb, nc, nd, ne]
    print(lista)
    lista.append(input("Novo Nome: "))
    print(lista)

if __name__ == "__main__":
    main()