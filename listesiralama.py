def en_buyuk_degeri_basa_al(liste): #en buyuk sayiyi liste[0] degeri yapar
	sayac=1
	enb=liste[0]
	denge=False

	while sayac <len(liste):
		if liste[sayac]>enb:
			enb=liste[sayac]
			denge=True
			kayitno=sayac
			sayac=sayac+1	
		else:
			sayac=sayac+1
	
	if denge == True:
		c=liste[0]
		liste[0]=liste[kayitno]
		liste[kayitno]=c
	
	return liste


##############################


def ozylistesirala(liste): #rekursif liste siralama islemi yapar.

	if len(liste) == 1:
		return [liste[0]]

	else:
		liste=en_buyuk_degeri_basa_al(liste)
		return [liste[0]] + ozylistesirala(liste[1:])


print ozylistesirala([5,7,99,5,35,12,3,4])
