#!/usr/bin/node
const fs = require('fs');

/**
 * Read file 'utf8' and show content.
 */
fs.readFile(process.argv[2], 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
