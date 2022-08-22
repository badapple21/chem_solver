let element_lookup = document.querySelector("#Element_lookup_input");
    
element_lookup.addEventListener("input", async function(){
    let response = await fetch("/fetch_lookup_element?q=" + element_lookup.value)
    let answer = await response.text();
    document.getElementById("lookup_response").innerHTML = answer;
    let elements = document.querySelectorAll(".btn");

    elements.forEach(element => {
        element.addEventListener("mouseover", async function(){
            let response = await fetch("/fetch_show_element?q=" + element.id)
            let answer = await response.text();
            document.getElementById("elements_info_div").innerHTML = answer;
        });
    });
});

