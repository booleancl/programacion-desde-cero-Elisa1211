# Las variables en python se declaran y asignan en una linea
# la declaracion entrega su nombre y la asignación su valor

num_one = 1
num_two = 2

num_three = num_one + num_two

print (num_three)

# ¿Podrems re asignar una variable?
# Si, aca un ejemplo 
num_two =5

num_four = num_one + num_two

print(num_four)


# Tambien podemos asignas texto a variables

word_one = "Hola"
space = " "
word_two = "Inmundo"

word_three = word_one + space + word_two

print(word_three)

# ¿Podremos sumar números con texto?







print(5/2)
print(5.0/2)
print(5+2*5)
print(5**2)
print(2**5)
print(5%2)
print(1/0.3)

#¿Qué es la verdad realmente?

true_value = True
false_value = False
zero = 0

one = 1

two = 2.0 

three = -3

zero = 0.0
empty_text = ""

if empty_text:
    print("Esto se ejecutara")
else:
    print("Entonces esto se ejecutará")
    print("Esto es parte del if")
print("Esto no es parte del if")

points = 100

if points > 100:
    print("eres lo max")
elif points >=100 and points > 70:
    print("eres muy bueno en esto")
else:
    print("vas por buen camino, pero puedes mejorar")
