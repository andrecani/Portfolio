s = input("Digite uma frase: ")
print(f"A string '{s}' tem tamanho {len(s)}")
print("Ascendente: ")
for i in range(len(s)):
    if i % 2 == 0: #teste se i é impar ou par
        print(s[i].upper(), end='')
    else:
        print(s[i].lower(), end='')

print("Descendente: ", end='')
for i in range(len(s) -1, -1, -1):
    if i % 2 == 0: #teste se i é impar ou par
        print(s[i].upper(), end='')
    else:
        print(s[i].lower(), end='')


