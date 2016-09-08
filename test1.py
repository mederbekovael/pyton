print "vy doljny vybrat shkatulku gde est podskazka kak spasti planetu ot zombi 1 ili 2"
shkatulka = raw_input("> ")
if shkatulka == "1":
    print" tam zagadka"
    print" 1.otgadaete zagadku"
    print" chto razgovarivaet na vsex yazykax"
    print" 2.ne otgadaete zagadku"    
    vyberete = raw_input("> ")	
    if vyberete == "1":
    	print" to poluchute kluch"
    elif vyberete == "2":
        print" vy umrete"
    else:
        print" to vy sposete planetu"
elif shkatulka=="2":
    print " to shiphr predlojeniya"
    print "1.otgadaete predlojeniya"
    print "2.ne otgadaete predlojeniya"
    otgadaete = raw_input("> ")
    if otgadaete == "1":
        print" vashe telo ne dneet"
    else:
    	print" vash mozg razlagaetsya"
else:
	print" vy upali v propost i vas poimali zombi"
