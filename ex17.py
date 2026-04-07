idade = int(input("digite sua idade: "))

if idade < 18: 
    print ("menor de idade")

elif idade >= 18 and idade < 59:
    print ("adulto")

else:
    print("idoso")