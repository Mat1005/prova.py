print ( "ciao,questo progamma serve a calcolare la media dei voti." )

materia  =  input ( "Dimmi di che materia stiamo parlando?" )
sommatoria  =  0
nvoti = int(input("quanti voti hai preso ?"))


while  True:
	
	votocorrente = int(input( "inserisci un voto:"))
	sommatoria += votocorrente 

	if votocorrente == 0:
		break



media  =  sommatoria/nVoti
print ( 'Fino ad ora in' , materia , 'hai preso' , nVoti , 'voti la cui media è' , media )			
