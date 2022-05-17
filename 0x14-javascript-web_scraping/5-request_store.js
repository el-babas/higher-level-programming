#!/usr/bin/node
const axios = require('axios').default;
const fs = require('fs');

const api = process.argv[2];
const filePath = process.argv[3];
/**
 * Request status code.
 */
axios.get(api)
  .then(function (response) {
    // handle success
    fs.writeFile(filePath, response.data, 'utf-8', err => {
      if (err) {
        console.log(err.message);
      }
    });
  })
  .catch(function (error) {
    // handle error
    console.log(error.message);
  })
  .then(function () {
    // always executed
  });
