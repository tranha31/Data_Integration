/**
 * Hiển thị list option
 * @param {Number} i số hiệu id
 */
function setEvent(i) {
    var main = document.getElementById("options-container"+i);
    var selectIcon = document.getElementById("selected-"+i);
    if(main.classList.contains("active")){
        main.style.display = "none";
        main.classList.remove("active");
        selectIcon.classList.remove("icon-selected");
    }
    else{
        main.style.display = "block";
        main.classList.add("active")
        selectIcon.classList.add("icon-selected");
        var option = main.querySelectorAll(".option")
        var value = document.getElementById("content-selected"+i).value;
        option.forEach(element => {
            var label = element.querySelector("label");
            if(label.textContent == value){
                element.classList.add("option-selected");
            }
            else{
                element.classList.remove("option-selected");
            }
        });
    }
}

