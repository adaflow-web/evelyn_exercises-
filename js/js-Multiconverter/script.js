
function moneyConver(euros) {
    return euros * 1.03;
}

function milesConver(miles) {
    return miles * 1.61;    
}

function tempConver(celsius) {
    return (celsius * 9/5) + 32;   
}

function askUSer() {
    answer = window.prompt("Voulez-vous utiliser le convertisseur? (oui/non)");

    if (answer != "oui" && answer != "non") {
        return window.alert("Vous devez répondre oui/non");

    } else if (answer == "oui") {
        return true;
        
    } else {
        return false;       
    } 
}

function askConver() {
    answer = window.prompt("Qu'est-ce que vous voulez convertir: euros/celsius/milles ");
    return answer; 
}

function enterValue() {
    answer = window.prompt("Entrez la valeur");
    return answer;
}

while (askUSer()) {
    var converType = askConver();
    var converValue = enterValue();
    var message = "Résultat: "
    var result = 0;

    if (converType == "euros") {
        message += moneyConver(Number(converValue)).toString() + " chf";    
    } else if (converType == "celsius"){
        message += tempConver(Number(converValue)).toString() + " Fahrenheit";
    } else if (converType == "milles") {
        message += milesConver(Number(converValue)).toString() + " Kms";
    } else {
       message = " :/ Je ne peux pas vous aider avec cette conversion"; 
    }
    console.log (message);
} 