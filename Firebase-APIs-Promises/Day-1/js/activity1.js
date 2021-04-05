
const catUrl = 'https://cat-fact.herokuapp.com/facts'
let catList = document.getElementById('catList')
let request = new XMLHttpRequest()

request.addEventListener('load', function() {
    let result = JSON.parse(this.responseText)
    let output = result.map(function(cat) {
        return`
        <li>${cat.text}</li>
        `
    });
    catList.innerHTML = output.join('')
})

request.open('GET', catUrl)
request.send()