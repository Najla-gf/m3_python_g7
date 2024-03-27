"""
Grupo1:
Felipe Arias
Najla Gatica
Lolett Llanquinao
Jimena Traipe
"""

#Desafío - Estructuras de datos y funciones (I)
#Actividad 3

recordatorios = [
    ['2021-01-01', "11:00", "Levantarse y ejercitar"],
    ['2021-05-01', "15:00", "No trabajar"],
    ['2021-07-15', "13:00", "No hacer nada es feriado"],
    ['2021-09-18', "16:00", "Ramadas"],
    ['2021-12-25', "00:00", "Navidad"]
]

#1 agregamos un nuevo evento
recordatorios.insert(1,['2021-01-02', '06:00', 'Empezar el año'])
print(recordatorios)
#[['2021-01-01', '11:00', 'Levantarse y ejercitar'], 0
# ['2021-01-02', '06:00', 'Empezar el año'], 1
# ['2021-05-01', '15:00', 'No trabajar'], 2
# ['2021-07-15', '13:00', 'No hacer nada es feriado'], 3
# ['2021-09-18', '16:00', 'Ramadas'], 4
# ['2021-12-25', '00:00', 'Navidad']] 5

#2 Cambiamos el día 15 de julio a 16 de julio
recordatorios[3]=['2021-07-16', '13:00', 'No hacer nada es feriado']
print(recordatorios)

#3 Lamentablemente le tocará trabajar el día del trabajo. Elimine el evento del día del trabajo.
recordatorios.pop(2)
print(recordatorios)

#4 Agregue una cena de Navidad y de Año Nuevo cuando corresponda. Ambas a las 22 hrs.
recordatorios.insert(4,['2021-12-24', '22:00', 'Cena de Navidad'])
print(recordatorios)
#[['2021-01-01', '11:00', 'Levantarse y ejercitar'], 0
# ['2021-01-02', '06:00', 'Empezar el año'], 1
# ['2021-07-16', '13:00', 'No hacer nada es feriado'], 2
# ['2021-09-18', '16:00', 'Ramadas'], 3
# ['2021-12-24', '22:00', 'Cena de Navidad'], 4
# ['2021-12-25', '00:00', 'Navidad']] 5

recordatorios.append(['2021-12-31', '22:00', 'Cena de Año Nuevo'])
print(recordatorios)
#[['2021-01-01', '11:00', 'Levantarse y ejercitar'], 
# ['2021-01-02', '06:00', 'Empezar el año'], 
# ['2021-07-16', '13:00', 'No hacer nada es feriado'], 
# ['2021-09-18', '16:00', 'Ramadas'], 
# ['2021-12-24', '22:00', 'Cena de Navidad'], 
# ['2021-12-25', '00:00', 'Navidad'], 
# ['2021-12-31', '22:00', 'Cena de Año Nuevo']]
