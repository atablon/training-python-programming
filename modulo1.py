# MODULO 1

# Laboratorio Adicional 1

# Crear un bucle que almacene en una variable la suma de todos los elementos numéricos de una lista, con excepción del último.

milista = list(range(1,10,1)) 
print(milista)
suma=0
for n in milista[:-1]:
    suma=suma+n
    print(f"La suma actual es = {suma}")


# Laboratorio Adicional 2 : Mostrar y Eliminar

# Utilizando un bucle “while”, elaborar un código que imprima en pantalla cada uno de los elementos de una lista y simultáneamente los elimine, hasta quedar vacía

milista = list(range(5))
listl= len(milista)
print(f"El tamaño de la lista {listl} y la lista {milista}")
i=0

while i<listl:
    print(f"Se elimina -> {milista[0]} /n {milista}")
    milista.remove(milista[0])
    i+=1
print(f"La lista quedo {len(milista)}: {milista}")    

# Con for
for n in milista[:]:
    print(f"Elemento eliminado {n}")
    milista.remove(n)
    print(milista)


# Laboratorio Adicional 3: Sucesión Fibonacci

# Crear una función en Python que tome como argumento un entero que indique la cantidad de términos y retorne una lista como la anterior. Por ejemplo: 
# >>> fib(10)
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

def fib(num):
    output= None
    if num>2:
        output = calculate_fib(num)
    else:
        print("El número ingresado debe ser mayor que 2")
        output=None
    return(output)

def calculate_fib(num):
    i=2
    fibo_list=[0,1]
    while i<num:
        partial=fibo_list[i-1]+fibo_list[i-2]
        fibo_list.append(partial)
        i+=1
    print(f"La lista de fibonacci para {num} es /n {fibo_list} ")
    return(fibo_list)

print(fib(10))

# Laboratorio Adicional 4: Promedio Variable

# Construir una función que se llame “promedio_variable”. Esta función debe tomar un número arbitrario de argumentos numéricos y devolver el promedio.

def promedio_variable(*args):
    pv=0
    lp=len(args)
    for n in args:
        pv+=n
    return(pv/lp)

arreglo=[2,3,4,5]
pv=promedio_variable(2,3,4,5)
print(f"El promedio variable de {arreglo} es /n  {pv}")


# DESAFIO 1

# Ejercio 1: ¿Estás ahí?

# Dada 2 listas con números enteros, crear una tercera con los números que pertenecen a ambas. Pero con la salvedad que en esta tercera no debe tener elementos repetidos.
# primera = [7, 5, 10, 9, 8, 1, 3, 5, 6, 3, 8, 0, 10, 9, 2]
# segunda = [6, 9, 3, 7, 9, 10, 5, 10, 7, 4, 5, 3, 2, 10, 2]

# Usar únicamente sentencias de control: condicionales y bucles. También es probable que tengas que usar el operador de pertenecía.

pra = [7, 5, 10, 9, 8, 1, 3, 5, 6, 3, 8, 0, 10, 9, 2]
sgn = [6, 9, 3, 7, 9, 10, 5, 10, 7, 4, 5, 3, 2, 10, 2]
tra = []
temp = pra + sgn

print(temp)

for n in temp:
    
    if n not in tra:
        tra.append(n)
        print(tra)

print(f"La tercera lista termina quedando: {tra}")


# Ejercicio 2: Contador de ingreso
# Tenemos una lista donde se registran los ingresos del personal a un sistema:
# personas = ["Susana","Tamara","Ana","Susana","Susana","Tomas","Ana"]
# Contar los ingresos en un diccionario. La clave debería de ser el nombre y el valor debería ser la cantidad de ingresos. 


personas = ["Susana","Tamara","Ana","Susana","Susana","Tomas","Ana"]
dicc = []
registro ={}
for n in personas:
    if n not in dicc:
        dicc.append(n)
        registro[n]=0
print(registro)
registro.keys

for n in personas:
    if n in registro.keys():
        registro[n]+=1

print(f"El conteo da {registro}")


# Ejercicio 3: Tic Toc
# Crear una función que reciba un número como argumento, ese número representará los segundos que se quieren convertir a horas, minutos y segundos.
# Por ejemplo, conversion(3600) retornaría el texto “01:00:00” , en cambio si recibe 1000, devolverá “00:16:40”
# No se puede usar ninguna función built-in, ni tampoco ningún módulo que haga la conversión

def tictoc(segundos):
    hhmmss = 0
    min = 0
    hs = 0
    contador = segundos

    while (contador-3600)>=0:
        hs+=1
        contador-=3600
    while (contador-60)>=0:
        min+=1
        contador-=60
    
    print(f"hs= {hs} min= {min} contador={contador}")
    if hs<10:
        hs=f"0{hs}:"
    else:
        hs=f"{hs}:"

    if min<10:
        min=f"0{min}:"
    else:
        min=f"{min}:"

    
    if contador<10:
        contador=f"0{contador}"
    else:
        contador=f"{contador}"
    
    hhmmss=hs+min+contador
    print(f"La hora es {hhmmss}")
    return(hhmmss)

tiempo=tictoc(3661)


diccio