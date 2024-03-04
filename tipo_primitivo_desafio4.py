valor = input("Digite o valor: ")

print('O seu tipo primitivo é ', type(valor))
print('É um numero  ??:', valor.isnumeric())
print('É uma letra ??: ', valor.isalpha())
print('É uma letra ou numero  ??', valor.isalnum())
print('Esta em maiusculo ?', valor.isupper())