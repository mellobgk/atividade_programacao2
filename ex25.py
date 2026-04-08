valor = input("digite um valor: ")

try:
    valorflot = float(valor)
    print(type(valorflot), valorflot / 2)

except:
    print("não númérico")