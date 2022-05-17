#!/usr/bin/node
const axios = require('axios').default;

// Example: 3 = “Return of the Jedi”.
const api = 'https://swapi-api.hbtn.io/api/films/';

axios.get(api.concat(process.argv[2]))
  .then(function (response) {
    // handle success
    const characters = response.data.characters;
    characters.forEach(function (element) {
      // Request API characters.
      axios.get(element)
        .then(function (response) {
          console.log(response.data.name);
        })
        .catch(function (error) {
          console.log(error.message);
        })
        .then(function () {
        });
    });
  })
  .catch(function (error) {
    // handle error
    console.log(error.message);
  })
  .then(function () {
    // always executed
  });
