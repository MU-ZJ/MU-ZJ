// Palindrome

userWord = prompt("Enter a word");
word = userWord.toLowerCase();

function palindrome(string) {
  string = string.split("").reverse().join("");
  return string;
}

if (palindrome(word) == word) {
  console.log("Word is a palindrome");
} else {
  console.log("Word is not a palindrome");
}

// Duplicates

let list = ["John", "Mary", "Alex", "Steve", "Mary", "John"];
console.log(list);

list = list.filter(function (item, index, array) {
  return array.indexOf(item) == index;
});

console.log(list);

// Item in array

class Vowel {
  constructor(input, vowels) {
    this.input = prompt("Enter a letter");
    this.vowels = ["a", "e", "i", "o", "u", "y"];
  }

  search() {
    return this.vowels.some((letter) =>
      this.input.toLowerCase().includes(letter.toLowerCase())
    );
  }
}

let vowel = new Vowel();

console.log(vowel.search());

// Largest number

let numbers = [1, 2, 3, 4, 5];

largest = Math.max.apply(null, numbers);
console.log(largest);

//Smallest number

smallest = Math.min.apply(null, numbers);
console.log(smallest);

//FizzBuzz

let userNumber = parseFloat(prompt("Enter a number"));

if (userNumber % 5 === 0 && userNumber % 3 === 0) {
  console.log("FizzBuzz");
} else if (userNumber % 5 === 0) {
  console.log("Buzz");
} else if (userNumber % 3 === 0) {
  console.log("Fizz");
} else console.log("Not divisible by 3 or 5");

// Even or odd

if (userNumber % 2 === 0) {
  console.log("Even");
} else console.log("Odd");

// Array sort

let presetNumbers = [3, 4, 56, 7, 8, 1];
console.log(presetNumbers);

presetNumbers.sort(function (a, b) {
  return a - b;
});
console.log(presetNumbers);

presetNumbers.sort(function (a, b) {
  return b - a;
});
console.log(presetNumbers);