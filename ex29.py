num = int(input("digite um número: "))

if num % 5 == 0 and num > 50 :
    print ("mútiplo alto")

elif num % 5 == 0 and num < 50 :
    print ("múltiplo baixo")

else:
    print ("número não é mútiplo")