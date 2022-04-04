def eurostofranc(euros):
    return euros * 1.04

def milestokms(miles):
    return miles * 1.60934

def celsiustofahr(celsius):
    return (celsius * 9/5) + 32

def ask_user(): 
    answer = input("Voulez-vous utiliser le convertisseur? (oui/non): ")

    while answer != "oui" and answer != "non":
        answer = input("Vous devez répondre (oui/non): ")
            
    if answer == "oui":
        return True

    else:
        return False  

def ask_conver():
    answer = input ("Qu'est-ce que vous voulez convertir: euros/celsius/milles ")   
    return answer

def ask_value():
    answer = int(input("Entrez la valeur à convertir: "))
    return answer 

while ask_user(): 
    conver_type = ask_conver()
    conver_value = ask_value()
    message = "Résultat: "
    
    if conver_type == "euros":
        message += str(eurostofranc(conver_value)) + " chf"    
    elif conver_type == "celsius":
        message += str(celsiustofahr(conver_value)) + " Fahrenheit"
    elif conver_type == "milles":
        message += str(milestokms(conver_value)) + " Kms"
    else:
       message = " :/ Je ne peux pas vous aider avec cette conversion"; 
   
    print(message)
 
    

