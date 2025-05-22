total_segundos = 1000000
semanas = total_segundos // (7 * 24 * 3600)
resto = total_segundos % (7 * 24 * 3600)

dias = resto // (24 * 3600)
resto = resto % (24 * 3600)

horas = resto // 3600
resto = resto % 3600

minutos = resto // 60
segundos = resto % 60
print(total_segundos, "segundos = ", semanas, "semanas,", dias, "dias,", horas, "minutos,", segundos,"segundos")