def main():
    lista = []
    cont = 0
    for i in range(3):
        lista.append(input("{}° Nome: ".format(i + 1)))
    tupla = tuple(lista)
    while True:
        if 'Maria' in tupla:
            cont += 1
            lista = list(tupla)
            lista.remove('Maria')
            tupla = tuple(lista)
        elif 'maria' in tupla:
            cont += 1
            lista = list(tupla)
            lista.remove('maria')
            tupla = tuple(lista)
        else:
            break
    print("{} Marias estão presentes!".format(cont))
if __name__ == "__main__":
    main()