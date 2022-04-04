# ● Créer un système de tirage au sort en Python. 
# ● Avec le nom des participants dans un tableau et un nombre de vainqueurs maximum.
# ● En faisant en sorte qu’une personne ne soit pas tirer au sort deux fois.
import random
players = ["Fred", "Evelyn",
           "Alessia", "Mara",
           "Maria", "Catia", 
           "Made", "Nino"]
playing = True

while playing:
    
    try: 
        
        ask_user = int(input("Combien de vainqueurs vous voulez avoir?: "))

    except: 
        print("Oups vous pouvez seulement entrer des numéros")
        quit()
        
    if ask_user <= len(players):
      winner = random.sample(players, ask_user)
      print (winner)
      playing = False
    else:
        print("Il y a un maximun de 8 personnes dans la liste de jouers")
            






    


