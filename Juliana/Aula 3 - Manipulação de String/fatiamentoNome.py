nome_completo = "Juliana Goncalves Silva Lopes"

# primeiro_nome = nome_completo[:7]
# print (primeiro_nome)

# ultimo_nome = nome_completo[-5:]
# print (ultimo_nome)

# ultimo_nome = nome_completo[30:]
# print (ultimo_nome)

# qtd_char = len(nome_completo)
# print (f"Na frase temos {qtd_char} caracteres")


# qtd_letras_a = nome_completo.count ("a")
# print(f"Na frase temos {qtd_letras_a} letras {nome_completo}")

palavra = "Lopes"
posicao_nome = nome_completo.find(palavra)
print(f"Meu último nome {palavra} se inicia na posicao {posicao_nome}")

verifica_nome = palavra in nome_completo or "Silva" or "Souza" or "Santos" in nome_completo
print(f"No sobrenome {nome_completo} esta no texto {verifica_nome}")
print(f"No sobrenome {nome_completo} esta no texto {verifica_nome}")
print(f"No sobrenome {nome_completo} esta no texto {verifica_nome}")