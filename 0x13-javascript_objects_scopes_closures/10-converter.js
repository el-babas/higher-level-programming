#!/usr/bin/node

/**
 * Function that converts a number from base 10 to another base passed as argument.
 * @param {*} base Base convert.
 * @returns New number convert to base.
 */
exports.converter = function (base) {
  return function (num) {
    return num.toString(base);
  };
};
