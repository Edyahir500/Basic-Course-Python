#   TIPOS DE DATOS

#Strings

"Hola hoy repasaremos ecuaciones diferenciales:"

print("String--cadena de caracteres por ejemplo:")
print("Hello world")
print('Hello world')
print("""Hello world""")
print('''Hello world''')
print(type("Hello world"))
print("Hello"+"world") # Unir strings -- es un proceso de concatenacion.
print("2+3")    # Es un proceso de SUMA.

#   Numeros

# Intiger (entero)
print("30 Es un numero entero int")

# Float (decimal)
print("30.5 Es un tipo de dato float")

# Boolean (Boleanas)
True
False

# List (Lista)  Cualquier tipo de dato se ocupa
[10, 20, 30, 40]
['Hola', 'Bye','Adios']
[10, 'Hello', False, 30.5]
[] # Se puede dejar vacia para despues definir un dato ya que no cuenta con ningun dato.

# Tuples (Tuplas) Para datos que no cambian,a si mismo en la lista.
#  El no poder cambiar un dato se le llama inmutable 
(10, 20, 30, 50)
()

# Dictionaries
{
    "name":"Edyahir",
    "lastname": "Vargas",
    "nickname": "Jairo"
}
{
    "latitud": 103412, # Key(clave): value(valor)
    "longitud":204948
}

print(type({
    "name":"Edyahir",
    "lastname": "Vargas",
    "nickname": "Jairo"
}))
