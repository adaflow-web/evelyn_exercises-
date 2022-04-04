def frais_port():
    montant_total = int(input("Montant total de la commande:"))
    pays_livr = input("Pays de livraison (FR, DE, ES, CH): ")
    calcul_envoie = (5*(montant_total/100))
    result = round(calcul_envoie,3)
    prix_envoie = str(result)+ " fr.-"
    message = "Livraison gratuite"
    message2 = "Cout d'expedition:"
    if montant_total >= 100:
        print(message)
    elif pays_livr == "CH":
        print(message)
    elif pays_livr =="FR" or "DE" or "ES":
        print(message2 + prix_envoie)
    else: 
        print("Cout d'expedition: 5")


frais_port()
frais_port()
