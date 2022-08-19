let element_lookup = document.qetElementById("Element_look_up_input");

element_lookup.addEventListner("change", async function(){
    let response = await fetch("/fetch_lookup_element?=" + element_lookup.value(){
    let answer = await response.text();
    document.getElementById("lookup_response").innerHTML = answer();
}
