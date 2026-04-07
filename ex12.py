num1 = float(input("digite um número:"))
num2 = float(input("digite um número: "))

soma = num1 + num2

if num1 > num2: 
    print ("a soma é: ", soma, " e o número maior é: ", num1)
elif num2 > num1:
    print ("a soma é: ", soma, " e o número maior é: ", num2)
else: 
    print ("a soma é: ", soma, " e os números são iguais: ", num1)