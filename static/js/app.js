let switchEn = document.getElementById("switch-en")
let wordEn = document.getElementsByClassName("wordEn")

switchEn.addEventListener("click", function () {
        for (let i = 0; i < wordEn.length; i++) {
            wordEn[i].style.display = (wordEn[i].dataset.toggled ^= 1) ? "block" : "none"
        }
    }
);

let switchRu = document.getElementById("switch-ru")
let wordRu = document.getElementsByClassName("wordRu")

switchRu.addEventListener("click", function () {
        for (let i = 0; i < wordRu.length; i++) {
            wordRu[i].style.display = (wordRu[i].dataset.toggled ^= 1) ? "block" : "none"
        }
    }
);

let switchTr = document.getElementById("switch-tr")
let wordTr = document.getElementsByClassName("wordTr")

switchTr.addEventListener("click", function () {
        for (let i = 0; i < wordTr.length; i++) {
            wordTr[i].style.display = (wordTr[i].dataset.toggled ^= 1) ? "block" : "none"
        }
    }
);

// let formEn = document.getElementById("form_en")
// console.log(formEn)

//
// let form = document.querySelector(".translate-form");
//
// form.addEventListener("submit", function (e) {
//     e.preventDefault() // This prevents the window from reloading
//
//     let formdata = new FormData(this);
//     let input = formdata.get("translation");
//     let translateForm = document.getElementById("form_en")
//     let green = "green"
//
//     for (let i = 0; i < wordEn.length; i++) {
//         console.log(wordEn[i])
//         if (wordEn[i].includes(input)) {
//             translateForm.style.border =  `1px solid ${green}`
//         }
//     }
// });
//
//






