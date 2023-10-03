diasemana = input("Ingrese día de la semana con minúsculas: ")
if diasemana == "lunes":
    print("Es lunes.")
elif diasemana == "viernes":
    print("Es viernes.")
elif diasemana == "sábado" or diasemana == "domingo":
    print("Es fin de semana.")
else:
    print("El día no es de los indicados en la tarea")
