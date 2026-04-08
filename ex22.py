valor = input( "digite um valor: ")

try:
    valorin = int (valor)
    if valorin > 10 :
        print ("alto")
    else:
        print ("baixo")
except:
    print ("entrada inválida")
