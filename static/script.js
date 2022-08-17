let element1 = document.querySelector("#element1");
let charge1 = document.querySelector("#charge1");
let element2 = document.querySelector("#element2");
let charge2 = document.querySelector("#charge2");
let amount1 = document.querySelector("#amount1");
let amount2 = document.getElementById("amount2");
let form = document.querySelector("#main_form");
let element_lookup = document.querySelector("#Element_look_up_input");

amount2.addEventListener("change", async function(){
    let response = await fetch("/fetch?q=" + element1.value + "&w=" + charge1.value + "&e=" + element2.value + "&r=" + charge2.value + "&t=" + amount1.value + "&y=" + amount2.value);
    let answer = await response.text();
    document.getElementById("ans").innerHTML = answer;
})
