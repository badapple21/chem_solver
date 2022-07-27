let element1 = document.querySelector("#element1");
let charge1 = document.querySelector("#charge1");
let element2 = document.querySelector("#element2");
let charge2 = document.querySelector("#charge2");

input.addEventListener("#charge2", async function(){
    let response = await fetch("/fetch?q=" + element1 + "&w=" + charge1 + "&e=" + element2 + "&r=" + charge2);
    let answer = await response.text();
    document.getElementById("ans").value = answer;
})