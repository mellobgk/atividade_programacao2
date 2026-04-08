valor = input("digite um valor: ")

try:
    valorf = float(valor)
    valorint = int(valor)

    if valorint :
        print(type(valorint), valorint * 2)
    elif valorf:
        print(type(valorf), valorf / 2)

except:
    print("tipo inválido")