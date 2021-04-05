let firstNameBox = document.getElementById('firstNameBox')

let lastNameBox = document.getElementById('lastNameBox')

let fullName = document.getElementById('fullName')

let btnSubmit = document.getElementById('btnSubmit')
btnSubmit.addEventListener('click', function(){
    fullName.innerHTML = `${firstNameBox.value} ${lastNameBox.value}`
})