# ¿Qué es Python?
Python es un lenguaje de programación interpretado fácil de aprender, esta dinámica de este lenguaje de programación hace de python un lenguaje muy atractivo para las personas que quieran aprender a programar por primera vez.
# ¿Qué es una variable?
Una variable en Python es un símbolo o palabra de referencia a la cual podemos añadir un valor que la variable va a almacenar dentro, así cuando queramos utilizar ese valor no es necesario escribirlo de nuevo y solo debemos escribir la variable a la que está unida.
## Nombrando una variable
Para asignarle un nombre a una variable tenemos que tener en cuenta que cualquier letra ya sea mayúscula o minúscula sirve como una variable.
En Python existe "palabras reservadas" las cuales nos pueden dar conflictos si las intentamos usar como variables, es por eso que esas palabras son evitadas para no causar errores en el código.
## Asignando valores a una variable
Para colocar un valor a una variable utilizamos =, es importante mencionar que la variable tiene que ir a la derecha del = y el valor a la izquierda así.
```python
x = 1
```
En Python existen diferente formas para asignar variables como:
Asignación en la misma línea:
```python
x = 3; y = 7; z = 10
```
Asignación múltiple:
```python
dia,mes,anho = "lunes" , "marzo", 2022
```
Asignación del mismo valor:
```python
valor1 = valor2 = 5
```
Asignación de intercambio:
```python
base = 10; altura = 20
base,altura = altura,base
```
## Operadores básicos
En Python podemos usar símbolos para realizar operaciones básicas como la suma (+) y la resta(-).
### Suma
Para la suma usamos el simbolo + :
```python
num1 = 3
num2 = 7
resultado = num1 + num2
#Print es una funcion en Python que permite mostrar el contenido dentro de los () en el terminal.
print(resultado)
```
### Resta
La resta se representa con - :
```python
num1 = 10
num2 = 7
resultado = num1 - num2
print(resultado)
```
### Multiplicación
La multiplicación se representa con un solo * :
```python
num1 = 5
num2 = 2
resultado = num1 * num2
print(resultado)
```
### División
La división se la representa con un solo / :
```python
num1 = 8
num2 = 2
resultado = num1 / num2
print(resultado)
```
### Módulo
El módulo es la representación del residuo de una división y se lo representa con % :
```python
num1 = 8
num2 = 2
resultado = num1 % num2
print(resultado)
```
# Tipos de datos en Python
Los tipos de datos que se pueden representar en Python son:

Números enteros

Números de punto flotante

Texto (cadenas de caracteres)

Booleanos (verdadero y falso)
## Integer
Interger son todos los numeros enteros y tiene como función int.
```python
a = 7
b = int(input("Ingrese un numero entero: "))
print(a * b)
#El int nos sirve en este caso como un filtro para que el ingreso del usuario (input) tenga que ser un numero entero.
```
## Float
Float por otro lado son números decimales y su función es float.
```python
a = 7
b = float(input("ingrese el valor a multiplicar: "))
print(a * b)
```
## String
Y string son las líneas de texto y también tiene su función str que recoge texto.
```python
mascotas = "perros y gatos"
print(mascotas)
```
## Casting en Python
El casting es la conversión de un dato a otro tipo de dato.
```python
int a str: str(12)

str a int: int("12")

float a int: int(12.5)
```
## List
Las listas son una forma de almacenar múltiples valores en una sola variable y son actualizables con lo cual podemos añadir más valores a la lista.
```python
lista = ["manzana", "naranja", "pera", "kiwi"]
print(lista)
```
## Tuple
Una tupla al igual que las listas recogen múltiples valores en una sola variable con la diferencia que las tuplas no son actualizables, es decir, que no se le pueden agregar más valores.
```python
tupla = ("manzana", "naranja", "pera")
print(tupla)
```
## Dictionary
Los diccionarios recogen múltiples valores en pares en una sola variable y se pueden agregar mas valores a estos después.
```python
diccionario = {
  "Rojo": "manzana",
  "Anaranjado": "naranja",
  "Verde": "pera"
}
print(diccionario)
```
# Tomando decisiones
Aqui encontraremos funciones condicionales y de ciclos con sus palabras clave.
## Sentencia if
If es una función condicional que como su nombre dice las líneas de código se ejecutaran si cumple con la condición dada.
Else se utiliza con if y elif para dar un resultado final si las condiciones anteriores dadas no se cumplen y elif es por así decir una condición más que podemos agregarle a la lista de condiciones.
```python
num =int(input('Ingrese un numero entero:'))

if num > 0:
    print(num, 'es positivo')
elif num < 0:
    print(num,'es negativo')
else:
    print ('el numero es =', num)
```
## Ciclo For
For es un bucle que repite el código que tiene por las veces que sea especificado.
```python
n = 7
suma = 0
for i in range(n):
    nota = float(input('Ingrese nota ' + str(i+1) + ':'))
    suma = suma + nota

promedio = suma/n

print('Promedio:', promedio)
```
## Ciclo While
While también es un bucle, pero cuya activación es una condición y será ejecutado hasta que ya no cumpla con la condición o tope con un break.
```python
num = 11

while not(num >= 10 and num <20 and num%2 == 0):
    num= int(input('num ingreso: '))
#En este codigo la condicion para que se active while deben ser numero que no sean mayor o igual a 10 y menor o igual a 20 y numeros pares.
#Al introducir numeros como 1,2,3,4,5,11,13,,15,21,22,23,90 se va a ejecutar el bucle hasta que se ingrese un valor entre 10 y 20 que sea par como 12.
```
## Break
La palabra clave break se utiliza para terminar ciclos que están sosteniendo a esta palabra dentro de su código dado.
```python
j = 0

for i in range (10):
    j += 2
    print('i:', i, 'j:', j)
    if j == 10:
        break
```
## Continue
Continue es otra palabra clave para bucles, pero la función de esta es de omitir las siguientes partes que siguen del código y continuar con el bucle hasta que termine.
```python
contador=0
for i in range (10):
    for j in range (10):
        contador +=1
        print ("i:",i,"j:",j)
        if contador == 50:
            continue
print ("contador:",contador)
```
