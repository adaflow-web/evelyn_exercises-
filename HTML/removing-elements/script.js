const content = document.getElementById("content");
const enterText = document.getElementById("enterText");
const addPara = document.getElementById("addPara");
const delPara = document.getElementById("delPara");


function addPararaph() {
    const newParagraph = document.createElement("p");
    newParagraph.innerText = enterText.value;
    newParagraph.className = "para";
    content.appendChild(newParagraph); 
}

function removeLastPara() {
    const paragraphs = document.getElementsByClassName("para");
    if (paragraphs.length > 0) {
        const lastPara = paragraphs.length - 1;
        content.removeChild(paragraphs[lastPara]);
        
    }
    
}
addPara.addEventListener("click", addPararaph);
delPara.addEventListener("click", removeLastPara);