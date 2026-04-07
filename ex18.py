num = int ( input( "digite um número: "))

if num % 2 == 0 and num > 0:
    print (num, "é par e positivo")

elif num % 2 == 0 and num < 0:
    print (num, "é par e negativo")

elif num % 2 != 0 and num > 0: 
    print (num, "é ímpar e positivo")

elif num % 2 != 0 and num < 0:
    print (num, "é ímpar e negativo")

else:
    print (num, "é neutro")