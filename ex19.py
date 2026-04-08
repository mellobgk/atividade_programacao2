num1 = float(input("digite um número: "))
num2 = float(input("digite outro número: "))

if num1 == num2:
    print("os números são iguais!!")

elif num1 != num2:
    diferenca = abs(num1 - num2)
    print("os números são diferentes!!")
    print("a diferença entre eles é:", diferenca)