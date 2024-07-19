document.addEventListener("DOMContentLoaded", function () {
    const consentCheckbox = document.getElementById("consent");
    const submitButton = document.getElementById("submit-btn");

    consentCheckbox.addEventListener("change", function () {
        submitButton.classList.remove("cursor-not-allowed") = !this.checked;
    });
});
