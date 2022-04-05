#!/usr/bin/node

/**
 * Function that returns the number of occurrences in a list.
 * @param {array} list Array of elements.
 * @param {*} searchElement Item to search.
 * @returns The number of occurrences in the list.
 */
exports.nbOccurences = function (list, searchElement) {
  const count = list.reduce((acc, value) => value === searchElement ? acc + 1 : acc, 0);
  return count;
};
