from random import randint
chislo = randint(1,10)

print "komputer zagodal chislo.Ugadaite ego."
answer = raw_input("> ")
if answer == chislo:
	print "Pravilno! Vy ugodali!"
else:
	print" Vy ne ugodali! Komputer zagadal chislo - %d" % chislo