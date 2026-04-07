num = int(input("digite um número: "))

if num % 2 == 0 and num > 0:
    print ("par e positivo")
elif num % 2 == 0 and num < 0:
    print ("par e negativo")
else:
    print ("ímpar")