print ( "ciao" )
materia  =  input ( 'Dimmi di che materia stiamo parlando?' )


sommatoria  =  0
nVoti  =  0


mentre  True :
	votoCorrente  =  float ( input ( 'inserisci un voto:' ))

	elif  votoCorrente  ==  0 :
		rompere
	altro :
		nVoti  + =  1
		sommatoria  + =  votoCorrente


media  =  sommatoria  /  nVoti
print ( 'Fino ad ora in' , materia , 'hai preso' , nVoti , 'voti la cui media è' , media )			
