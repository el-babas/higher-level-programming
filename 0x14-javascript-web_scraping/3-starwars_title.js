#!/usr/bin/node
const axios = require('axios').default;

const api = 'https://swapi-api.hbtn.io/api/films/';
/**
 * Request status code.
 */
axios.get(api.concat(process.argv[2]))
  .then(function (response) {
    // handle success
    console.log(response.data.title);
  })
  .catch(function (error) {
    // handle error
    console.log(error.message);
  })
  .then(function () {
    // always executed
  });
