const fileInput = document.querySelector("#tInput")
const btn = document.querySelector("#okBtn")
const opImage = document.querySelector("#output_image")


const loadIamge = () => {
    let file = fileInput.files[0];
    if(!file) return;
    opImage.src = URL.createObjectURL(file);
    console.log(opImage.src);
}


fileInput.addEventListener("change", loadIamge);
btn.addEventListener("click", ()=> fileInput.click());


