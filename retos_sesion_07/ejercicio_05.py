frase = "Anita lava la tina"

frase_limpia = frase.replace(" ", "").lower()
frase_invertida = frase_limpia[::-1]
es_palindromo = frase_limpia == frase_invertida
print(f"{frase_limpia} = {frase_invertida}")
print(f"{frase} es palíndromo?\n{es_palindromo}")