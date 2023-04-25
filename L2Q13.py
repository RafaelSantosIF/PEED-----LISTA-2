def main():
    dicionario = {}
    while True:
        chave = input("Nome da Chave: ")
        dicionario[chave] = int(input("Valor da Chave: "))
        agree = input("CONTINUAR? [Y]SIM [N]NÃO\n:")
        if agree != 'Y' and agree != 'y':
            break
    if 'profissão' in dicionario:
        print("Profissão: ", dicionario['profissão'])
    else:
        print("Não há profissão!")
if __name__ == "__main__":
    main()