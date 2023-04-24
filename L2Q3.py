def main ():
    dicionario = {}
    chave = input("Nome do Item: ")
    valor = int(input("Valor do Item: "))
    dicionario[chave] = valor
    print(dicionario)
    chave = input("Nome do Item: ")
    valor = int(input("Valor do Item: "))
    dicionario[chave] = valor
    print(dicionario)

if __name__ == "__main__":
    main()