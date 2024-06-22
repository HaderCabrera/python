palabra = input("ingrese la palabra")
palabra2 = palabra[::-1]
contador = 0
for i in range(len(palabra)):
    if palabra[i] == palabra2[i]:
        contador += 1
if contador == len(palabra):
    print("la PALABRA ES PALINDROME")
else:
    print("la palabra NO es palindrome")       
    
       