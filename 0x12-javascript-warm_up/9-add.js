#!/usr/bin/node

/**
 * Prints the addition of 2 integers.
 * @param {int} a
 * @param {int} b
 */
function add (a, b) {
  console.log(parseInt(a) + parseInt(b));
}

add(process.argv[2], process.argv[3]);
