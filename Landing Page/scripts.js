
const findOutMoreBtn = document.getElementById("findOutMoreBtn");
const emailFormPopup = document.getElementById("emailFormPopup");
const closePopup = document.getElementById("closePopup");


findOutMoreBtn.addEventListener("click", function() {
    emailFormPopup.style.display = "block";
});

closePopup.addEventListener("click", function() {
    emailFormPopup.style.display = "none";
});

let emailForm = document.getElementById("emailForm");
let emailInput = document.getElementById("email");
let successAlert = document.createElement("div");

successAlert.className = "alert alert-success";
successAlert.textContent = "Thank you! Please check your email: ";
successAlert.style.display = "none";

emailForm.addEventListener("submit", function(event) {
    event.preventDefault(); 

    const email = emailInput.value;
    console.log("Email:", email);
    successAlert.textContent += email


    emailForm.style.display = "none";
    const findOutMoreBtn = document.getElementById("findOutMoreBtn");
    console.log(findOutMoreBtn.nextSibling)
    findOutMoreBtn.parentNode.insertBefore(successAlert, findOutMoreBtn.nextSibling);
    successAlert.style.display = "block";
    emailFormPopup.style.display = "none";
});

emailForm.appendChild(successAlert);