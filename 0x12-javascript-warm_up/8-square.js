#!/usr/bin/node
const size = parseInt(process.argv[2]);
if (Number.isNaN(size)) {
  console.log('Missing size');
} else {
  for (let i = 0, simbol; i < size; i++) {
    simbol = '';
    for (let j = 0; j < size; j++) {
      simbol += 'X';
    }
    console.log(simbol);
  }
}
