texto = "Curso de Pyton"

setima_posicao_texto = texto[6]
print(setima_posicao_texto)

texto_curso = texto[:5]
print(texto_curso)

texto_pyton = texto[9:15]
print(texto_pyton)

#Contar o numero de caracteres dentro do texto
qtd_char = len(texto)
print (f"Na frase temos {qtd_char} caracteres")

#Contar um número específico de caracteres dentro do texto
letra = "o"
qtd_letras_o = texto.count ("o")
print(f"Na frase temos {qtd_letras_o} letras {letra}")

#Contar um número específico de letras dentro do texto

qtd_letras_o = texto.count ("o" or "O")
print(f"Na frase temos {qtd_letras_o} letras {letra}")

#Identifica a posição onde inicia uma palavra
palavra = "Pyton"
posicao_palavra = texto.find(palavra)
print(f"A palavra {palavra} inicia na posicao {posicao_palavra}")

#Identificar se existe a palavra no texto
verifica_palavra = palavra in texto
print(f"A palavra {palavra} esta no texto {verifica_palavra}")

#Identificar se existe a palavra no texto
verifica_palavra = palavra in texto or "São Paulo" in texto
print(f"A palavra {palavra} esta no texto {verifica_palavra}")