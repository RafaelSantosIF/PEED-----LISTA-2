def main():
    dicionario = {}
    while True:
        chave = input("Nome da Chave: ")
        dicionario[chave] = int(input("Valor da Chave: "))
        agree = input("CONTINUAR? [Y]SIM [N]NÃO\n:")
        if agree != 'Y' and agree != 'y':
            break
    dicionario['cidade'] = input("Sua Cidade de Origem: ")
    print(dicionario)
if __name__ == "__main__":
    main()