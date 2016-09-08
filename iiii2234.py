from random import randint
chislo = randint(1,10)
play = True;
while play:
	    print "komputer zagodal chislo.Ugadaite ego."
        answer = raw_input("> ")
        if answer == chislo:
	        print "Pravilno! Vy ugodali!"
	        play = False 
         else:
	        print" Vy ne ugodali! Poprobuite eshe raz"
