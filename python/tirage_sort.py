# ● Créer un système de tirage au sort en Python. 
# ● Avec le nom des participants dans un tableau et un nombre de vainqueurs maximum.
# ● En faisant en sorte qu’une personne ne soit pas tirer au sort deux fois.
import random
players = ["Fred", "Evelyn",
           "Alessia", "Mara",
           "Maria", "Catia", 
           "Made", "Nino"]
end_game = False

def winner_message():      #pour un résultat user-friendly
        if ask_user == 1:
           return "Voici le vainqueur de ce tirage au sort: "
        else:
           return "Voici les " + str(ask_user) + " vainqueurs de ce tirage au sort: " 

def keep_playing():   # avec cette function je veux demander aux users s'ils veulent continuer à jouer 
    
    question_user = input("On joue à nouveau? oui/non: ")

    while question_user != "oui" and question_user != "non":
        return "Oups, vous pouvez seulement répondre oui ou non!"
    
    if question_user == "Oui":
        return True 
    else:
        return False   # ce truc ne marche pas!!!!!  aarrrrgggg
        

while end_game != True:
    
    try: 
        
        ask_user = int(input("Combien de vainqueurs vous voulez avoir?: "))

    except: 
        print("Oups vous pouvez seulement entrer des numéros")
        quit()
  
        
    if ask_user <= len(players):
      winner = random.sample(players, ask_user)
      print (winner_message())           
      for win in winner:
        print (win)
        end_game = True   # J'ai essayé en appelant la function keep_playing() au lieu de end_game = True 
      # J'essayé en dehors de la boucle For mais ne marche pas non plus. 
    else:
        print("Il y a un maximun de 8 personnes dans la liste de jouers")

# si j'appelle la function ici ça fait NADA


         






    


