edad = int(input("Digame su edad: "))
ingresos = int(input("Muestreme tus ingresos mensuales: "))
if edad > 16 and ingresos > 1000:
    print("Tienes que tributar por ser mayor de 16 e ingresar más de 1000 euros al mes.")
else:
    print("No tienes que tributar nada.")
