const counterInput = document.getElementById("counterInput");
const btnCounter = document.getElementById("btnCounter");
const counterDisp = document.getElementById("counterDisp");

btnCounter.addEventListener("click", function () {
  let counter = 0;
  let userTime = parseInt(counterInput.value);
  if(!isNaN(userTime)) {
  let countDown = userTime;
  let timerId = window.setInterval(function () {
    counter++;
    countDown--;
    console.log(counter);
    counterDisp.innerHTML = `${countDown}`;

    if (counter === userTime) {
      window.clearInterval(timerId);
    }
  }, 1000);
  console.log(timerId);
  counterInput.value = "";
  }else return
});
