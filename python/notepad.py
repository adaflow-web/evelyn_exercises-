#Next idea for notepad 1.2 what about keeping track of date and time of each note? 
#create a note
def write_note(content):
    file = open("notes.txt", "a") #my python doesn't create a note. 
    file.write("______\n")                                                        #I had to create it myself and give the path/why????
    file.write(content + "\n")
    file.close()

#searching for a note
def search_note(content):
    file = open("notes.txt")
    text = file.read()
    notes = text.split("______")
    note_found = ""

    for note in notes:
        if note.find(content) != -1:
            note_found += "______\n" + note
    if note_found == "": 
        print("Votre note n'a pas été trouvé")
    else:
        print(note_found)
   
    file.close()

#deleting notes
def erase_note():
   ask_user = input("Voulez vous effacer toutes les notes Y/N: " ).upper()
   
   if ask_user != "Y" and ask_user != "N":
       return " Y or N"
   elif ask_user == "Y":
       file = open("notes.txt" , "w")
       file.close()
   

 # add this function to allow the user to continue using notepad or not      
def quit_notepad():
    ask_continue = input ("Voulez vous continuer à utiliser Notepad? Y/N: ").upper()
    if ask_continue != "Y" and ask_continue != "N":
           return " Y or N"
    elif ask_continue == "Y":
           return True
    else:
           return False


#setup for use
active_notepad = True

while active_notepad:

    try:
        option = int(input("""Qu'est-ce que vous aimeriez faire?
        Tapez 1 pour écrire une note
        Tapez 2 pour chercher des notes\n:"""))
    except:
        print("NameError: Vous pouvez seulement entrer des numéros")
        quit()

    if option != 1 and option != 2:
        print ("Vous devez choisir option 1 ou 2")

    elif option == 1:
       note = input("Entrez votre note:\n") 
       write_note(note)

    elif option == 2:
        text = input("Entrez le text à chercher:\n").strip()    
        search_note(text)

    else: 
        print("Pas de résultats")
    
    erase_note()
    active_notepad = quit_notepad()




