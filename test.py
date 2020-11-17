materia = input("ciao,di quale materia vuoi che ti calcoli la media dei voti?")

Voti = []
while True:
	voto = float(input("inserisci un voto, per stoppare scrivi 11"))
	if voto == 11:
		break
	else:
		Voti.append(voto)
        
totVoti = len(Voti)
somma = sum(Voti)
media = somma / totVoti
print("In", materia, "hai preso", totVoti, "voti, e la media è", media)			


print("ecco i tuoi voti in",materia,Voti)
