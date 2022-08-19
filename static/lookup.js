
let element_lookup = document.qetElementById("Element_lookup_input");

element_lookup.addEventListener("change", async function(){
    let response = await fetch("/fetch_lookup_element?q=" + element_lookup.value )
    let answer = await response.text();
    document.getElementById("lookup_response").innerHTML = answer;
})
