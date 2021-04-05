// const vowels = ['a', 'e', 'i', 'o', 'u', 'y']

function Vowel(input, vowels) {
  this.input = prompt("Enter a letter")
  this.vowels = ["a", "e", "i", "o", "u", "y"]
  return this.vowels.some((letter) => this.input.toLowerCase().includes(letter.toLowerCase())
  );
}

console.log(Vowel());
