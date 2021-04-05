const contentWrapper = document.getElementById("contentWrapper");
const submitWrapper = document.getElementById("submitWrapper");
const miscWrapper = document.getElementById("miscWrapper");
const emailInput = document.getElementById("emailInput");
const typeInput = document.getElementById("typeInput");
const sizeInput = document.getElementById("sizeInput");
const priceInput = document.getElementById("priceInput");
const btnSubmit = document.getElementById("btnSubmit");
const emailSearch = document.getElementById("emailSearch");
const emailSubmit = document.getElementById("emailSubmit");
const emailResult = document.getElementById("emailResult");
const emailDelete = document.getElementById('emailDelete')
const dataUrl = "https://troubled-peaceful-hell.glitch.me/orders";
const email = emailSearch.value;

fetch(dataUrl)
  .then((response) => response.json())
  .then((data) =>
    data.map(function (data) {
      contentWrapper.innerHTML += `
    <div class='itemWrapper'>
    <ul>
    <li>Email: ${data.email}</li>
    <li>Type: ${data.type}</li>
    <li>Size: ${data.size}</li>
    <li>Price: ${data.price}</li>
    </ul
    </div>
    `;
    })
  );

btnSubmit.addEventListener("click", function (e) {
  e.preventDefault();
  let inputDataRaw = {
    email: emailInput.value,
    type: typeInput.value,
    size: sizeInput.value,
    price: parseFloat(priceInput.value),
  };
  let inputData = JSON.stringify(inputDataRaw);

  fetch(dataUrl, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: inputData,
  })
    .then((response) => response.json())
    .then((data) => {
      console.log("Success:", data);
      window.location.reload()
    })
    .catch((error) => {
      console.error("Error:", error);
    });
});

emailSubmit.addEventListener("click", function () {
    fetch(dataUrl + '/' + email)
    .then((response) => response.json())
    .then(data => {
        emailResult.innerHTML = 
        `
        <div class='itemWrapper'>
        <ul>
        <li>Email: ${data.email}</li>
        <li>Type: ${data.type}</li>
        <li>Size: ${data.size}</li>
        <li>Price: ${data.price}</li>
        </ul>
        </div>
        `
      });
});

emailDelete.addEventListener('click', function(e) {
    e.preventDefault()
    fetch(dataUrl + '/' + email, {
        method: "DELETE",
      })
        .then((response) => response.json())
        .then((data) => {
          console.log("Success:", data);
          window.location.reload()
        })
        .catch((error) => {
          console.error("Error:", error);
        });
})