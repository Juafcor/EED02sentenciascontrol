

#sentencias de control
#bifurcación

a=50

if a%2 == 0:
    print(f"El valor {a} es un número par")
else:
    print(f"El valor {a} es un número impar")

if a > 50:
    print(f"El valor {a} es mayor que 50")
elif a>50:
    print(f"El valor {a} es menor que 50")
else:
    print(f"El valor {a} es 50")

#bucles 
#scanner

num=input("introduce un valor:") 
#el input SIEMPRE devuelve una cadena de caracteres. Es decir, si escribes 46, no será un número, será un texto "46"

print("Valor introducido", num)

num=int(num)
#bucles while
a=0
while a<num:
    print("a:", a)
    a+=1

#bucle for
sum=0
for a in range(10):
    sum+=a
    print("a:", a, "sum:", sum)




#bucle que solicite números al usuario hasta que se introduzca un número par

parimpar=int(input("dime un numero: "))
parimpar2=1

while parimpar%2!=0 or parimpar2%2!=0:
    
    parimpar=parimpar2

    parimpar2=int(input("dime otro número: "))

