#!/usr/bin/node
let count = 0;

/**
 * Function that prints the number of arguments already printed and the new argument value.
 * @param {*} item: Any value.
 */
exports.logMe = function (item) {
  console.log(count + ': ' + item);
  count++;
};
