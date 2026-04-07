valor = input("digite algo: ")

try: 
    num = float(valor) 
    print (type(num))
    print (num ** 2)

except ValueError:
    print (type(valor))