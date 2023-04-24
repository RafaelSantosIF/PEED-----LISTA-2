def main():
    na = input("Nome: ")
    nb = input("Nome: ")
    nc = input("Nome: ")
    tupla = (na, nb, nc)
    sub = int(input("ESCOLHA UM NOME PARA SUBSTITUIR: \n[1] {} [2] {} [3] {}\n: ".format(na, nb, nc)))
    nw = input("Novo Nome: ")
    lista = list(tupla)
    lista[sub - 1] = nw
    tupla = tuple(lista)
    print(tupla)


if __name__ == "__main__":
    main()
