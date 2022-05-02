// const paragraph = document.getElementsByClassName("paragraph");


const myButton = document.getElementById("myButton");
const changeText = document.getElementById("changeText");
const delTitle = document.getElementById("delTitle")
const content = document.getElementById("content");


const getEmail = document.getElementById("getEmail");

console.log(paragraph);

title.innerHTML = "This title has changed thanks to JS";

for (let i = 0; i < paragraph; i++ ) {
    console.log(paragraph[i]);
    }

mySubmit.value = "Send";
getEmail.value = "email here";

function changeTitle() {
    title.innerText = changeText.value;
      
}

myButton.addEventListener("click", changeTitle);






