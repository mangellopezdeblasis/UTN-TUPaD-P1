Ejercicio = int(input("Ingrese el número del ejercicio: "))
#Ejercicio 1
if Ejercicio == 1:
    edad = int(input("Ingrese su edad: "))
    if edad < 18:
        print("Eres menor de edad")
    else:
        print("Eres mayor de edad")

#Ejercicio 2
elif Ejercicio == 2:
    nota = int(input("Ingrese su nota: "))
    if nota >= 6:
        print("Aprobado")
    else:
        print("Desaprobado")

#Ejercicio 3
elif Ejercicio == 3:
    num = int(input("Ingrese un número: "))
    if num % 2 == 0:
        print("Ha ingresado un número par")
    else:
        print("Por favor, ingrese un número par")
#Ejercicio 4
elif Ejercicio == 4:
    edad = int(input("Ingrese su edad: "))
    if edad <12:
        print("Eres un niño")
    elif edad >= 12 and edad < 18:
        print("Eres un adolescente")
    elif edad >= 18 and edad < 30:
        print("Eres un Adulto joven")
    else:
        print("Eres un adulto")
#Ejercicio 5
elif Ejercicio == 5:
    password = input("Ingrese su contraseña: ")
    if password and len(password) >= 8 and len(password) <= 14:
        print("Ha ingresado una contraseña correcta")
    else:
        print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")
#Ejercicio 6
elif Ejercicio == 6:
    import random
    from statistics import mode, median, mean
    numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
    print("Lista de números aleatorios:", numeros_aleatorios)
    moda = mode(numeros_aleatorios)
    mediana = median(numeros_aleatorios)
    media = mean(numeros_aleatorios)
    if moda < mediana and mediana < media:
        print("Tiene sesgo positivo")
    elif moda > mediana and mediana > media:
        print("Tiene sesgo negativo")
    else:
        print("No tiene sesgo")
#Ejercicio 7
elif Ejercicio == 7:
    palabra = input("Ingrese una palabra o frase: ")
    if palabra[-1].lower() in 'aeiou':
        palabra += '!'
        print(palabra)
    else:
        print(palabra)
#Ejercicio 8
elif Ejercicio == 8:
    nombre = input("Ingrese su nombre: ")
    opcion =int(input("Si quiere su nombre en mayúsculas ingrese 1, si quiere su nombre en minúsculas ingrese 2 o si quiere su nombre con la primera letra mayúscula ingrese 3: "))
    if opcion == 1:
        print(nombre.upper())
    elif opcion == 2:
        print(nombre.lower())
    elif opcion == 3:
        print(nombre.capitalize())
    else:
        print("Opción no válida")
#Ejercicio 9
elif Ejercicio == 9:
    magnitud = float(input("Ingrese la magnitud del terremoto: "))
    if magnitud < 3:
        print("imperceptible")
    elif magnitud >= 3 and magnitud < 4:
        print("ligeramente perceptible")
    elif magnitud >= 4 and magnitud < 5:
        print("sentido  por personas, pero generalmente no causa daños")
    elif magnitud >= 5 and magnitud < 6:
        print("(puede causar daños en estructuras débiles")
    elif magnitud >= 6 and magnitud < 7:
        print("puede causar daños significativos")
    elif magnitud >7:
        print("puede causar graves daños a gran escala")
    else:
        print("Valor no válido")
#Ejercicio 10
elif Ejercicio == 10:
    hemisferio = input("Ingrese el hemisferio (N/S): ").upper()
    mes = int(input("Ingrese el mes (1-12): "))
    dia= int(input("Ingrese el día (1-31): "))
    if hemisferio == 'N':
        if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
            print("Es invierno")
        elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
            print("Es primavera")
        elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
            print("Es verano")
        elif (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <= 20):
            print("Es otoño")
    elif hemisferio == 'S':
        if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
            print("Es verano")
        elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
            print("Es otoño")
        elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
            print("Es invierno")
        elif (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <= 20):
            print("Es primavera")
        else:
            print("Hemisferio no válido")
            
#n° de ejercicio no válido
else:
    print("Ejercicio no válido")