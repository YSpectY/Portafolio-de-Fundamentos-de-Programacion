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
Los tipos de datos que se pueden representar en python son:

Numeros enteros

Numeros de punto flotante

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
Float por otro lado son los numero 
```python
a = 7
b = float(input("ingrese el valor a multiplicar: "))
print(a * b)
```
## String
Y string son las lineas de texto y tambien tiene su funcion str que recoje texto.
```python
mascotas = "perros y gatos"
print(mascotas)
## Casting en Python

## List

## Tuple

## Dictionary

# Tomando decisiones

## Sentencia if

## Ciclo For

## Ciclo While

## Break

## Continue
