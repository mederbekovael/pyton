# -*- coding: utf-8 -*-
from random import randint
chislo = randint(1,10)
play = True;
print "komputer zagodal chislo.Ugadaite ego."
while play:
	    
    answer = raw_input("> ")
    if int(answer) == chislo:
	    print "Pravilno! Vy ugodali!"
	    play = False 
    else:
        print" Vy ne ugodali! Poprobuite eshe raz"
        if int(answer) < chislo:
            print "vashe chislo menshe togo, chto zagadal komputer"
        else:
            print "Vashe chislo to, chto zagadal komputer"
