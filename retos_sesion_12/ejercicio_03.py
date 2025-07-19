autos_jhon = {'Ferrari', 'Lamborghini', 'Porsche', 'Bugatti', 'McLaren'}
autos_jess = {'Ferrari', 'Lamborghini', 'Tesla', 'Ford', 'Chevrolet'}

autos_en_comun = autos_jhon & autos_jess

if len(autos_en_comun) > 0:
    print("Los autos en comun entre Jhon y Jess son :", autos_en_comun)
else:
    print("No hay autos en común entre Jhon y Jess.")