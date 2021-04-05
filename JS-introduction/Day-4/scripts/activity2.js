const counterInput = document.getElementById("counterInput");
const btnCounter = document.getElementById("btnCounter");
const counterDisp = document.getElementById("counterDisp");
const btnStop = document.getElementById('btnStop')

btnCounter.addEventListener('click', function() {
    let userStock = counterInput.value;
    let refresh = window.setInterval(function() {
        let quote = getStockQuote(userStock);
        counterDisp.innerHTML = `${quote.name} ${quote.price}`
        btnStop.addEventListener('click', function(){
            window.clearInterval(refresh);
        })
    }, 2000) 
})