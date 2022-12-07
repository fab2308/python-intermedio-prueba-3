#Este es un juego de adivinar el número
import random

intentos=0

print('¡Hola! ¿Cuál es tu nombre?')
nombre = input()

numero=random.randint(1,100)
print('Bueno, '+nombre+', piensa un número entre 1 y 100.')

while intentos<10:
    print ('¡Adivínalo! Tienes 10 intentos')
    adivina=input()
    adivina=int(adivina)

    intentos=intentos+1
   
    if adivina<numero:
        print ('¡Demasiado pequeño!')

    if adivina>numero:
        print('¡Demasiado grande!')

    if adivina==numero:
        break

if adivina==numero:
    intentos=str(intentos)
    print('Fabuloso, '+nombre+', acertaste el número en '+intentos+' intentos. ¡Estarás orgulloso-a!')

if adivina!=numero:
    numero=str(numero)
    print('¡Qué fatalidad '+nombre+' ! Yo estaba pensando en el número '+numero)

if __name__ == "__main__":
    main()
    