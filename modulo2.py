# FUNCIONES DE ORDEN SUPERIOR

from socket import ALG_SET_AEAD_ASSOCLEN


suma = lambda x: x+100
suma(20)

# EJERCICIO 1: Superior
# Cree una función llamada “superior”, que reciba por argumento una función y una lista. La función que se pasa por argumento a superior debe elevar al cubo un número y retornarlo. Para que luego al aplicarla en la de orden superior, esa operación se realice miembro a miembro de la lista. Para finalizar la función “superior” debe de devolver una nueva lista.

def superior(func,milista):
    resultado=[]
    for n in milista:
        resultado.append(func(n))
    print(resultado)
    return(resultado)

print(f"Mi lista al cubo es : {superior(lambda x:x**3,[1,2,3])}")

## Capturar excepciones https://docs.python.org/es/3/library/exceptions.html
# Existen varios tipos de excepciones:
# ValueError: Tipo de valor, int, str, etc
# TypeError: Tipo de objeto
# RuntimeError
# KeyError: Acceder a una clave de diccionario que no existe
# IndexError: se quiere acceder un indice inexistente
# ZeroDivisionError: Se quiere dividir por cero

# Es importante aclarar que, si una excepción se propaga sin que ningún bloque de código la capture, el programa finaliza inmediatamente sin concluir las líneas de código siguientes si las hubiera.

# Ejercicio 2: Calculadora
# Crear un programa que solicite dos números en consola e imprima el resultado de las cuatro operaciones aritméticas aplicadas sobre ellos.
# Teniendo en cuenta lo siguiente:
# ● Si el usuario ingresa cualquier otra cosa que no sea un número, debe volver a preguntar, en ambos casos.
# ● Contemplar que el segundo número puede ser cero y, por ende, llegado el momento de la división el programa debe imprimir “No se puede dividir por cero”.Como restricción, no se pueden usar condicionales (if)

def calculadora():
    print("Se solicita a continuacion dos numeros para las variables a y b /n a:")
    a=input()
    b=input()
    try:
        a=float(a)
        b=float(b)
        print(f"Los numeros son a={a} y b={b}")
        print(f"a+b={a+b}/n a*b={a*b}/n a-b={a-b}/n a/b={a/b}/n")  
    except (TypeError,ValueError):
        print("El tipo de valor y dato incorrecto")
    except ZeroDivisionError:
        print("No se puede dividir por cero")
    

calculadora()

# Ejercicio 3: Países
# Crear un script que solicite al usuario el código de un país e imprima su nombre, de acuerdo con el siguiente diccionario:
# # Diccionario código: país.
paises = {
 "ar": "Argentina",
 "es": "España",
 "us": "Estados Unidos",
 "fr": "Francia"
}
# Si el código ingresado no se encuentra en el diccionario, debe imprimir un mensaje en pantalla y volver a preguntar. Si el usuario escribe “salir”, el programa debe terminar.

while True:
    print("Por favor ingrese el código de un país")
    cpais = input()
    if cpais.lower()=="salir":
        print("Gracias por usar nuestro programa")
        break
    try:
        print(f"El pais es:{paises[cpais]}")
    except KeyError:
        print("Ingrese un codigo de país valido")


print("FIN")

# Ejercicio 4: Mayúsculas

# Se tiene una lista de personas como la siguiente

personas= ["juan salvo","henry courtney","elizabeth bennet","marge simpson"]

# Se desea crear una función que ponga mayúscula solo en la primera letra, tanto del nombre como del apellido, y que devuelva la lista con esta modificación. Se puede usar funciones de orden superior para resolver el ejercicio, no hay limitaciones.

personas= map(lambda x:x.title(), personas)

print(list(personas))



## Entrada y salida de archivos

# Ejercicio 5: Guardar datos

#Cree un algoritmo para guardar cada una de las personas del diccionario personas en un txt.
personas = {"Juan":20,"Romina":32,"Tamara":25,"Melanie":19}
#El nombre se tiene que guardar en minúsculas y cada persona debe quedar en un renglón con un guión del medio separando el nombre y la edad. Ejemplo dentro del personas.txt se tendría que ver:
#roberto-20
#romina-32

f= open("personas.txt","w")
personas = {"Juan":20,"Romina":32,"Tamara":25,"Melanie":19}
for p in personas:
    print(f"{p} - {personas[p]}")
    f.write(f"{p.lower()} - {personas[p]} \n")
f.close()


# Ejercicio 6: Rescatar datos

# Cree un algoritmo para volver al diccionario original desde el archivo personas.txt creado en el ejercicio anterior. El nombre se tiene que recuperar en mayúsculas y cada valor debe volver a ser del tipo entero. El diccionario tendría que volver a verse como: 
personas={}
f=open("personas.txt","r")

temp=f.readline().strip().split(" - ")
personas[temp[0]]=int(temp[1])
print(personas)
print(personas.split(" - "))

pepe=f.readlines()

# ALG_SET_AEAD_ASSOCLEN
