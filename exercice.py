def cesar(msg, clef=0): 
	alphabet="abcdefghijklmnopqrstuvwxyz" 
	chiffre="" 
  
	# On prend chaque lettre du mot (converti en minuscules) 
	for l in msg.lower(): 
		# On recherche la position de la lettre dans l'alphabet 
		pos=alphabet.find(l) 
  
		# Gestion du chiffrement selon la présence ou pas de la lettre 
		chiffre+=alphabet[(pos+clef) % len(alphabet)] if pos != -1 else l 
	# for 
	return chiffre 
# cesar() 
  
message="Hello World !!!" 
chiffre=cesar(message, 5) 
dechiffre=cesar(chiffre, -5) 
print(message) 
print(chiffre) 
print(dechiffre)