#!/usr/bin/node

/**
 * Function that returns the reversed version of a list.
 * @param {list} list
 */
exports.esrever = function (list) {
  const newList = [];
  list.forEach(element => { newList.unshift(element); });
  return newList;
};
