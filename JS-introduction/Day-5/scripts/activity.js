const firstName = document.getElementById("firstName");
const lastName = document.getElementById("lastName");
const emailInput = document.getElementById("email");
const password = document.getElementById("password");
const submit = document.getElementById("submit");

function validateEmail(email) {
  const re = /[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?/;
  return re.test(email);
}

submit.addEventListener("click", () => {
  console.log(firstName.value);
  console.log(lastName.value);
  console.log(password.value);
  let emailValue = emailInput.value;

  if (validateEmail(emailValue)) {
    console.log(emailValue);
  } else console.log(validateEmail());
  firstName.value = ''
  lastName.value = ''
  emailInput.value = ''
  password.value = ''
});
