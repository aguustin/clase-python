#print("precio producto")

#precio = 2000
#precioB = 5000
#cantidad = 20
#nombre_producto = "lata de tomate"

# OPERADORES MATEMATICOS: + (suma), - (resta), * (multiplicación), / (división), % (resto de división)

#resultado = (precio + precioB) * 20

#porcentaje = (precio * 35) / 100    #(numeroA * 25) / 100  (esto saca el 25% porciento de numeroA)

#print(resultado, " ", porcentaje)


#FUNCIONES
#def calculador_edad():
  #  edad = 32
  #  nombre = "agustin"
   # print("mi funcion me devolvio: ", edad, " ", nombre)

#calculador_edad()

#ejercicio 1
#numeroA = int(input("Ingresa el primer numero a sumar: "))
#numeroB = int(input("Ingresa el segundo numero a sumar: "))

#resultado = numeroA + numeroB

#print(resultado)


#ejercicio 2
#numero = int(input("numero a chequear: "))
#chequeo = numero % 2

#if chequeo != 0:
#    print("impar")
#else:
#    print("par")

#ejercicio 3
#edad = int(input("ingresa edad: "))
#comparacion = edad >= 18
#print(comparacion)

#ejercicio 4
#numeroA = int(input("ingresa primer numero"))
#numeroB = int(input("ingresa segundo numero"))
#chequear = (numeroA > 0) and (numeroB > 0)
#print(chequear)

#ejercicio 5
#numero = int(input("Ingresa un numero del 1 al 100: "))
#es_divisible = (numero % 3 == 0) and (numero % 5 == 0)
#print("es divisible: ", es_divisible)


#ejercicio 6
#edad = int(input("Escribi tu edad "))
#if edad >= 18:
#    print("Sos mayor de edad")
#else:
 #   print("Sos menor")

#ejercicio 7






#bucles integrador clase 2 a 7
#1
#for numero in range(1, 11):
    #print(numero)


#2
#numero = int(input("Ingresá un número: "))

#while numero >= 0:
    #print(numero)
    #numero = numero - 1


#3
#suma = 0

#for numero in range(1, 21):
    #suma = suma + numero

#print("La suma es:", suma)


#4
#mayor = int(input("Ingresá un número: "))

#for i in range(4):
    #numero = int(input("Ingresá otro número: "))

    #if numero > mayor:
        #mayor = numero

#print("El número mayor es:", mayor)


#5
#for numero in range(1, 51):
  #  if numero % 3 == 0:
      #  print(numero)

       # if numero % 7 == 0:
        #    break



# mayor = int(input("ingresa el numero mayor: "))

# for a in range(4):
#     numero = int(input("ingresa el numero: "))

#     if numero > mayor:
#        mayor = numero

# print("El numero mayor es: ", mayor)










# #listas integrador del 2 al 7
# #1
# comidas = ["pizza", "hamburguesa", "empanadas"]

# print(comidas)

# #2
# comidas = ["pizza", "hamburguesa", "empanadas"]

# comidas.append("asado")

# print(comidas)

# #3
# comidas = ["pizza", "hamburguesa", "empanadas", "asado"]

# print("Primera comida:", comidas[0])
# print("Última comida:", comidas[-1])

#4
# numeros = []

# for i in range(5):
#     numero = int(input("Ingresá un número: "))
#     numeros.append(numero)

# print("El número más grande es:", max(numeros))

# #5
# precios = [1500, 800, 2300, 1200, 950]

# print("Suma total:", sum(precios))
# print("Precios ordenados:", sorted(precios))









#diccionario y tuplas integrador 2 a 7
# 1. Diccionario con nombre, edad y ciudad

# persona = {
#     "nombre": "Juan",
#     "edad": 20,
#     "ciudad": "Mendoza"
# }

# print(persona["nombre"])
# print(persona["edad"])
# print(persona["ciudad"])


# # 2. Agregar una clave nueva al diccionario

# persona["hobby"] = "Jugar videojuegos"

# print(persona)


# # 3. Tupla con 3 colores

# colores = ("celeste", "blanco", "celeste")

# print(colores[0])
# print(colores[-1])


# # 4. Recorrer el diccionario con for y .items()

# for clave, valor in persona.items():
#     print(clave, valor)


# # 5. Diccionario de precios

# precios = {
#     "pan": 1000,
#     "leche": 1500,
#     "arroz": 1200,
#     "fideos": 900
# }

# producto = input("Ingresá el nombre del producto: ")

# if producto in precios:
#     print("El precio es:", precios[producto])
# else:
#     print("El producto no existe.")










# #funciones integrador 2 a 7
# # 1. Función saludar

# def saludar(nombre):
#     print(f"Hola, {nombre}!")


# saludar("Juan")


# # 2. Función sumar

# def sumar(a, b):
#     return a + b


# resultado = sumar(2, 3)
# print(resultado)


# # 3. Función es_par

# def es_par(numero):
#     return numero % 2 == 0


# print(es_par(4))
# print(es_par(7))
# print(es_par(10))


# # 4. Función promedio

# def promedio(lista):
#     return sum(lista) / len(lista)


# numeros = [7, 8, 9, 10]
# print(promedio(numeros))


# # 5. Desafío: clasificar notas y mostrar boletín

# def clasificar_nota(nota):
#     if nota >= 9:
#         return "Excelente"
#     elif nota >= 7:
#         return "Muy bien"
#     elif nota >= 6:
#         return "Aprobado"
#     else:
#         return "Desaprobado"


# def mostrar_boletin(notas):
#     for materia, nota in notas.items():
#         categoria = clasificar_nota(nota)
#         print(materia, ":", nota, "-", categoria)


# notas = {
#     "Matemática": 8,
#     "Lengua": 6,
#     "Programación": 10,
#     "Historia": 5
# }

# mostrar_boletin(notas)





#1. Creá una lista con tus 3 comidas favoritas y mostrala con print().
#Pista: Se escribe entre corchetes: comidas = ["...", "...", "..."].

#comidas = ["ravioles", "milanesa", "sopa"]

#comidas.append("carne")

#print(comidas)

#5. Desafío: dada una lista de precios ya cargada, mostrá la suma total (con sum()) y después
#mostrala ordenada de menor a mayor con sorted().
#Pista: sum(lista) suma todos los números. sorted(lista) devuelve una copia ordenada, sin modificar la
#original.

# total = [60, 20, 30]
# sumatotal = sum(total)
# print(sumatotal)
# listaordenada = sorted(total)
# print(listaordenada)
# personaLista = ["Ana", 25, "Mendoza"]
# personaLista[1]
# personas = {"nombre": "Agustin", "edad": 32, "ciudad": "Mendoza"}

# print(personas["nombre"], " " , personas["edad"], " ", personas["ciudad"])

# for persona in personas:
#     print(persona)

# for clave, valor in personas.items():
#     print(clave, valor)

#personas_tupla = ("Ana", 25, "Mendoza")


# for clave in personas.keys():
#     print(clave)

# for persona in personas.values():
#     print(persona)



# for multiplo in range(1, 51):
#     if multiplo % 3 == 0 and multiplo % 7 == 0: #Evalua primero si "multiplo" es multiplo de 3 y 7 a la vez
#         print("es multiplo de 3 y 7")
#         break #rompe el bucle
#     elif multiplo % 3 == 0: #Evalua si "multiplo" es multiplo de 3 solo si la condición anterior no se cumplio
#         print("es multiplo de 3: ", multiplo)
#     else: #Imprime el numero en caso de no haberse dado ninguna de las dos condiciones anteriores
#         print(multiplo)

# materias = {"biologia": 0, "psicologia": 0}


# def clasificar_nota(nota):
#     for key, value in materias.items():
#         key[nota]

# clasificar_nota(10)
# clasificar_nota(8)

# numeros = []

# for i in range(5):
#     numero = int(input("Ingresá un número: "))
#     numeros.append(numero)

# print("El número más grande es:", max(numeros))


#MANIPULACIÓN DE STRINGS:
#SLICE agarrar una parte de la cadena (string)
#split tomar las palabras de una cadena y transformarlas en una lista
#upper() transforma la cadena en mayuscula
#lower() transforma la cadena en minuscula
#join() une las palabras de una cadena por el caracter que se le indica
#strip()  
#replace() reemplazas una o varias palabras de una cadena (string) 

# frase = "Me encanta programar en Java"
# lista_frase = frase.split()
# # corregida = frase.replace("programar en Java", "Python")
# # print(corregida)
# # print("Python" in corregida) #true
# # print("Ruby" in corregida) #false

# frase_corregida = ''

# for frases in lista_frase:
#     if(frases == "programar"):
#         frase_corregida = frase.replace(frases, " ")

# print(frase_corregida)