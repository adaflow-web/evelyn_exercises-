import random


playing = True



def user_wins(user, computer):

    if user == computer:

        print("Il y a égalité!")

    #p > m /c > p / m > c  

    elif (user == "p" and computer == "m") or (user == "c" and computer == "p") or (user == "m" and computer == "c"):

        print ("Tu as gagné :)")
        
    else:

        print ("Tu as perdu :(")
   

def play_again(): 

    ask_user = input("On joue à nouveau? oui/non: ")
        
    if ask_user != "oui" and ask_user != "non":
        return "Oups, vous pouvez seulement répondre oui ou non!"
        
    elif ask_user == "oui":
        
        return True 
    else:

        return False  


while playing:


    user = input ("Quelle est votre choix? (p) pour papier, (m) pour marteau, (c) pour ciseaux: ")


    while user != "p" and user != "m" and user != "c":

        print ("Je ne comprends pas votre choix. Le jeu s'arrête. ")

        quit()
        

    computer = random.choice(["p", "m", "c"])

    print ("Choix de l'ordinateur: " + computer)

    user_wins(user, computer)

    playing = play_again()
    
    

     



