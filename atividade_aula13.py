print("\nDigite uma mentira com uma palavra que, se for substituída, transforme tudo em verdade. Em seguida, aperte Enter.")
frase = input()
print("\nDigite a palavra que precisa ser substituída e aperte Enter.")
palavra_mentirosa = input()
print("\nDigite uma palavra que substitua a anterior, tornando a frase verdadeira, e aperte Enter.")
palavra_verdadeira = input()
frase_verdadeira = frase.replace(palavra_mentirosa,palavra_verdadeira)
print("\nMentira:\n",frase)
print("\nVerdade:\n",frase_verdadeira)
separacao_por_palavras = frase_verdadeira.split(" ")
contagem = len(separacao_por_palavras)
print("\nA quantidade de palavras que você digitou foi:",contagem)


