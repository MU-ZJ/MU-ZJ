const firstNameInput = document.getElementById("firstNameInput");
const lastNameInput = document.getElementById("lastNameInput");
const btnSubmit = document.getElementById("btnSubmit");
const fullName = document.getElementById("fullName");

btnSubmit.addEventListener("click", function () {
  fullName.innerHTML = `${firstNameInput.value} ${lastNameInput.value}`;
  firstNameInput.value = lastNameInput.value = "";
});
