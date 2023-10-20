import re
# 1 caractere especial x
# 1 maiuscula x
# 1 minuscula x
# 1 numero  x
# minimo 8 caractere x

senha = input("digite a senha")



numero_de_caracteres = len(senha)
count_minuscula = 0
count_espaço = 0
count_maiuscula = 0
count_numero = 0

for letra in senha:

  if letra.isupper():
    count_maiuscula+= 1
  if (letra.islower()) == True:
    count_minuscula+= 1
  if (letra.isspace()) == True:
    count_espaço+= 1
  if letra.isdigit():
    count_numero+= 1



if count_maiuscula >= 1:
  if count_minuscula >= 1:
    if numero_de_caracteres in range(8,24):
      if count_espaço == 0:
        if count_numero >= 1:
          if re.search(r'[^\w\s]', senha):
            print("="*20+'senha aprovada'+"="*20)
else:
   print("="*20+'senha invalida'+"="*20)

if count_maiuscula == 0:
  print('senha temque conter pelo menos uma letra maiuscula')
if count_minuscula == 0:
  print('a senha temque conter pelo menos uma letra minuscula')
if not numero_de_caracteres in range(8,24):
  print('a senha temque conter entre 8 e 24 caracteres')
if count_espaço >= 1:
  print('não são permitidos espaço na senha')
if count_numero == 0:
  print('a senha temque conter no minimo um numero')
if not re.search(r'[^\w\s]', senha):
  print('a senha temque conter pelo menos um caractere especial')

