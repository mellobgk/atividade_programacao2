num = int(input("digite um número: "))

if num >= 1 and num <= 10:
    print ("pequeno")
elif num > 10 and num <= 100:
    print ("médio")
elif num > 100:
    print ("grande")
else:
    print ("negativo ou zero")