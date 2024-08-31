#Trocando uma palavra dentro de um texto
texto = "JULIANA LOPES"
troca_palavra = texto.replace("JULIANA GONÇALVES SILVA LOPES" , "JULIANA LOPES")
print(troca_palavra)

#Deixando todos os caracteres em maiúsculo
texto = "JugsLopes@Gmail.Com"
texto_maiusculo =  texto.upper()
print(texto_maiusculo)

#Deixando todos os caracteres em minúsculo
texto_minusculo = texto.lower()
print (texto_minusculo)

#Deixando a primeira letra de cada palavra Maiúsculo
texto = "Meu primeiro curso no Senai"
texto_title = texto.title()
print (texto_title)

#Deixando a primeira letra de texto em Maiúsculo
texto_capitalize = texto.capitalize()
print (texto_capitalize)

#Elimina Espaços inúteis
texto = "       SENAI         "
print(f'A palavra {texto} tem {len(texto)} caracteres')

texto_strip = texto.strip()
print(f'A palavra {texto_strip} tem {len(texto_strip)} caracteres')
