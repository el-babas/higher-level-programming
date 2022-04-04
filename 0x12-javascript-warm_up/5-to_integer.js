#!/usr/bin/node
const my_number = parseInt(process.argv[2]);
if (Number.isNaN(my_number)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + my_number);
}
