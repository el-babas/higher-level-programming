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
  .catch(function () {
    // handle error
    console.log('code: 404');
  })
  .then(function () {
    // always executed
  });
