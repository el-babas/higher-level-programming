#!/usr/bin/node
const axios = require('axios').default;

/**
 * Request status code.
 */
axios.get(process.argv[2])
  .then(function (response) {
    // handle success
    console.log('code:', response.status);
  })
  .catch(function (error) {
    // handle error
    if (error.response) console.log('code:', error.response.status);
    else console.log(error.message);
  })
  .then(function () {
    // always executed
  });
