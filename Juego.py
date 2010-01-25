import random,sys
import sys
def main():
    try:
        numero = random.randint(int(sys.argv[1]), int(sys.argv[2]))
        a=str(numero)
	return a
    except IndexError:
        print "Se necesitan 2 parametros, un numero desde, y un numero hasta, para adivinar un numero entre dos valores"
        print "Ejemplo: $python elegirEjercicio.py 1 100"

if __name__ == '__main__':
    main()
b=main()
print "Bienvenido al juego de adivinar el numero que pienso"
print "Prueba suerte"
x=raw_input(">>>")
if x < b:
	print "Mi numero es mayor"
if x==b:
	print "Has acertado.Que raro"
	sys.exit()
if x>b:
	print "Te has pasado"
print "Introduce otro numero.Te quedan 4 intentos"
y=raw_input(">>>")
if y < b:
	print "Todavia mayor"
if y==b:
	print "Acertaste"
	sys.exit()
if y>b:
	print "Menor"
print "Introduce otro numero.3 intentos"
z=raw_input(">>>")
if z < b:
	print "Mas"
if z==b:
	print "Siii"
	sys.exit()
if z>b:
	print "Aun menor"
print "Otro numero.2 intentos"
w=raw_input(">>>")
if w < b:
	print "Mi numero sigue siendo mayor"
if w==b:
	print "Siiiiiiii"
	sys.exit()
if w>b:
	print "Menos menos"
print "Solo te queda un intento"
t=raw_input(">>>")
if t < b:
	print "Mas, mas, mas"
if t==b:
	print "Por los pelos acertaste"
if t>b:
	print "Era todavia menor....Fallaste,prueba de nuevo"

