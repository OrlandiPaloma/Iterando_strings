"Iterando strings com while em python"

minha_string = "O rato roeu a roupa do rei de roma."
tamanho_string = len(minha_string)

c = 0

while c < tamanho_string:
    print (c, minha_string[c])
    c = c+1

#exercicio2:

string = "Apenas testando"

c = 0
while c < len(string):
    print(string[c])
    c += 1

#exercicio 3: note que neste exercicio a frase é montada aos poucos. Tambem é possível montar de uma vez só, utilizando o print fora da condicional if.

minha_string = "O rato roeu a roupa do rei de roma."
tamanho_string = len(minha_string)

c = 0

nova_string = ""

while c < tamanho_string:
    if minha_string[c] == "r":
        nova_string = nova_string + minha_string[c].upper()
    else:
        nova_string = nova_string + minha_string[c] 
        print(nova_string) #Aqui imprime a frase sendo montada linha a linha.
    c += 1

print('')

print(nova_string) #Aqui imprime a frase inteira.

