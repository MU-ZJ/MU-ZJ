const cityName = document.getElementById('cityName')
const stateCode = document.getElementById('stateCode')
const btnSubmit = document.getElementById('btnSubmit')
const contentWrapper = document.getElementById('contentWrapper')



function outputWeather(onLoad) {
    let nameInputRaw = cityName.value
    let nameInput = nameInputRaw.toLowerCase()
    let stateInputRaw = stateCode.value
    let stateInput = stateInputRaw.toLowerCase()
    let weatherUrl = `https://api.openweathermap.org/data/2.5/weather?q=${nameInput},${stateInput}&appid=414297432d3490ba76da3fa9502c6bb9&units=imperial`
    fetch(weatherUrl)
    .then((response) => {
        return response.json()
    }).then((data) => {
        onLoad(data)
    })
}

btnSubmit.addEventListener('click', function(e) {
    e.preventDefault()
    contentWrapper.innerHTML = ''
    outputWeather((data) => {
        contentWrapper.innerHTML = `<div>
        <ul>
        <li>City: ${data.name}</li>
        <li>Temp: ${data.main.temp}\xB0F</li>
        <li>Feel Like: ${data.main.feels_like}\xB0F</li>
        <li>Humidity: ${data.main.humidity}%</li>
        <li>Wind Speed: ${data.wind.speed}mph</li>
        <li>Pressure: ${data.main.pressure}hPa</li>
        </ul>
        </div>`
    })    
})