var randomNumber = Math.floor(Math.random(1)*101);
console.log (randomNumber);
var userWins = false;
var attemps = 0;
word = "";


while (userWins != true) {

    guessNumber = window.prompt("Rentrez un numéro entre 1 et 100: ");
    attemps += 1;

    if(isNaN(guessNumber)){
        console.error("Oups, vous pouvez seulement rentrer des numéros!");
                
    } else {

        if (guessNumber < 1 || guessNumber > 100) {
            console.log("Petit rappel! Le numéro secret se trouve entre 1 et 100");
        }
        else if (randomNumber < guessNumber) {
            console.log("Piste: Le numéro secret est inférieur");  
    
        }
        else if (randomNumber > guessNumber){
            console.log("Piste: Le numéro secret est supérieur");
        }
        else {
        userWins = true;
        console.log ("Bravo! Le numéro secret est " + randomNumber.toString());
            
        }
    }


}

if(userWins){
    if (attemps == 1){
        word = " essai";
    }else {
        word = " essais";
    }
    console.log(" Vous avez trouvez le résultat en " + attemps.toString() + word);

}











// import random
// random_number = random.randint(1,101)
// user_wins = False                    
// attemps = 0
// word = ""
// print ("DEVINEZ LE NUMERO SECRET")

// while user_wins != True:
//     try:
//          guess_number = int(input("Rentrez un numéro entre 1 et 100: "))
                 
//     except:
//         print("Oups, vous pouvez seulement rentrer des numéros!") 
//         quit()  
    
//     attemps += 1

//     if guess_number < 1 or guess_number > 100:
//         print ("Petit rappel! Le numéro secret se trouve entre 1 et 100")
      
//     elif random_number < guess_number: 
//         print("Piste: Le numéro secret est inférieur")
      
//     elif random_number > guess_number:
//         print("Piste: Le numéro secret est supérieur")
      
//     else: 
//         user_wins = True 
//         print("Bravo! Le numéro secret est " + str(random_number))
       
// if attemps == 1:
//     word = " essai"
// else:
//     word = " essais"

// print("Vous avez trouvé le résultat en " + str(attemps) + word)
   
    
    