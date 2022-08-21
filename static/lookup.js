let element_lookup = document.querySelector("#Element_lookup_input");
console.log(element_lookup);

element_lookup.addEventListener("input", async function(){
    let response = await fetch("/fetch_lookup_element?q=" + element_lookup.value)
    let answer = await response.text();
    document.getElementById("lookup_response").innerHTML = answer;
})
