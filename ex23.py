num1 = int(input("digite um número:"))
num2 = int(input("digite outro número: "))
num3 = int(input("digite mais um número: "))

r1 = num1 % 3
r2 = num2 % 3
r3 = num3 % 3

resto = [r1, r2, r3]  # o "[]" faz uma lista
resto.sort(reverse=True) # o "reverse=True" ordena a lista em ordem decrescente, se fosse "reverse=False" seria em ordem crescente

print("o resto em ordem decresente é: ", resto)