# Crear el diccionario desde la tupla
especies = dict((
    ('canino', '🐶'),
    ('felino', '🐱'),
    ('aves', ['🐦', '🦅'])
))
print("Diccionario original")
print(especies)

aves = especies.pop('aves')
print("Diccionario eliminando 'aves'")
print(especies)

# modificando felino
especies['felino'] = '🐈'

especies['caninos'] = ['🐶', '🐕']
del especies['canino']

# Mostrar el diccionario final
print("Diccionario final:")
print(especies)