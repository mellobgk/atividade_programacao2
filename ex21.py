num = int(input("digite um número: "))

mut = num % 2 == 0 and num % 3 == 0

if num > 0 and mut:
    print ("mútiplo de 2 e 3")
elif num < 0:
    print ("número inválido")
else:
    print ("não atende")