num = int(input("digite um número: "))

if num >= 1 and num <= 100 and num % 2 == 0:
    print("par no intervalo")
elif num >= 1 and num <= 100 and num % 2 == 1:
    print ("ímpar no intevalo")
else:
    print ("fora do intevalo")