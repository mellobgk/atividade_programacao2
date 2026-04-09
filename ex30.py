valor = input("digite um valor: ")

try:
    num1 = int(valor)

    if num1 % 2 == 0 and num1 > 100:
        print("par alto")
    elif num1 % 2 == 0 and num1 <= 100:
        print("par baixo")
    else:
        print ("ímpar")

except:
    print("entrada inválida")