#!/usr/bin/node
const dict = require('./101-data').dict;

const newDict = {};

/**
 * Imports a dictionary of occurrences by user id and computes
 *  a dictionary of user ids by occurrence.
 */
Object.keys(dict).map(function (key) {
  if (newDict[dict[key]] === undefined) {
    newDict[dict[key]] = [];
  }
  newDict[dict[key]].push(key);
  return (true);
});

console.log(newDict);
