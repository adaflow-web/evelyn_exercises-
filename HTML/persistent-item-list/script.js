const content = document.getElementById("content");
const enterText = document.getElementById("enterText");
const addItem = document.getElementById("addItem");
const delItem = document.getElementById("delItem");
const clearAll = document.getElementById("clearAll");



function createList() {
    const newItem = document.createElement("p");
    newItem.innerText = enterText.value;
    if (newItem.innerText == "") {
        return false
     
    }else {
        newItem.className = "para";
        content.appendChild(newItem);
        const itemStorage = content.children.length - 1;
        localStorage.setItem(`element-${itemStorage}`, enterText.value )
    }
    
    
}

function removeLastItem() {
        const items = document.getElementsByClassName("para");
        if (items.length > 0) {
        const lastItem = items.length - 1;
        content.removeChild(items[lastItem]);
        const itemStorage = content.children.length;  
        localStorage.removeItem(`element-${itemStorage}`);
            
    }
    
}

function clearList() {
    content.innerHTML = "";
    localStorage.clear();
 }


addItem.addEventListener("click", createList);
delItem.addEventListener("click", removeLastItem);
clearAll.addEventListener("click", clearList);