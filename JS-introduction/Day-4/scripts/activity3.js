imgContainer = document.getElementById("imgContainer");
const images = [
  "assets/poster1.png",
  "assets/poster2.png",
  "assets/poster3.png",
  "assets/poster4.png",
  "assets/poster5.png",
];

let index = -1;
let counterID = window.setInterval(function() {
    index++
    imgContainer.innerHTML = `
    <img src="${images[index]}">
    `
    if(index == 4) {
        index = -1
    }
}, 1000)
