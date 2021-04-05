numbers = []

firstNumber = prompt('Enter first number: ', '0')
secondNumber = prompt('Enter second number: ', '0')

numbers.push(firstNumber, secondNumber)

for(let index = 0; index < numbers.length; index++) {
    numbers[index] = parseInt(numbers[index]);
}

let sum = numbers.reduce(function(a,b) {
    return a+b;
}, 0)

console.log(sum)

if(sum > 50 && sum < 80) {
    console.log(65)
} else if(sum > 80) {
    console.log(80)
}