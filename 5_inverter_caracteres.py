string = input("Digite uma string: ")
string_invertida = ""

for i in range(len(string)-1, -1, -1):
    string_invertida += string[i]


print(f"String invertida: {string_invertida}")