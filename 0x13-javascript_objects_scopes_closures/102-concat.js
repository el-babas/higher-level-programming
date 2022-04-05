#!/usr/bin/node
const fs = require('fs');

const fileOne = fs.readFileSync(process.argv[2]).toString();
const fileTwo = fs.readFileSync(process.argv[3]).toString();
fs.writeFileSync(process.argv[4], fileOne + fileTwo);
