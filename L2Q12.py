def main():
    lista = []
    for i in range(3):
        lista.append(input("{}° Nome: ".format(i + 1)))
    tupla = tuple(lista)
    if 'Maria' in tupla or 'maria' in tupla:
        print("Maria está presente!")
    else:
        print('Sem Marias')
if __name__ == "__main__":
    main()
