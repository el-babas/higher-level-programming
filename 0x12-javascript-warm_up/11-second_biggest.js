#!/usr/bin/node
const numbers = [];

for (let i = 2; i < process.argv.length; i++) {
  if (Number.isNaN(parseInt(process.argv[i])) === false) {
    numbers[i - 2] = parseInt(process.argv[i]);
  }
}

numbers.sort(function (a, b) {
  return b - a;
});

if (numbers.length <= 1) {
  console.log(0);
} else {
  console.log(numbers[1]);
}
