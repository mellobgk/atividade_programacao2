valor = input("digite um valor: ")

try:
    valorf = float(valor)
    valorint = int(valorf)

    if valorint == valorf:
        print(type(valorint), valorint * 2)
    else:
        print(type(valorf), valorf / 2)

except:
    print("tipo inválido")