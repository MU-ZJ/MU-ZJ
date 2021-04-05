const dogURl = 'https://dog.ceo/api/breeds/image/random'
const imgWrapper = document.getElementById("imgWrapper");
const btnRandom = document.getElementById("btnRandom");
let request = new XMLHttpRequest();

btnRandom.addEventListener("click", function () {
  request.addEventListener("load", function () {
    let result = JSON.parse(this.responseText);
    imgWrapper.innerHTML = `
    <img src=${result.message}>
    `;
  });
  request.open("GET", dogURl);
  request.send();
});
