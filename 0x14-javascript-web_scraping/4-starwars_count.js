#!/usr/bin/node
const axios = require('axios').default;

// ID Wedge Antilles = 18.
const idCharacter = 'https://swapi-api.hbtn.io/api/people/18/';
// https://swapi-api.hbtn.io/api/films/
const api = process.argv[2];
/**
 * Request status code.
 */
axios.get(api)
  .then((response) => {
    // handle success
    let count = 0;
    const films = response.data.results;
    films.forEach(function (element) {
      if (element.characters.includes(idCharacter)) count++;
    });
    console.log(count);
  })
  .catch((error) => {
    // handle error
    console.log(error.message);
  })
  .then(function () {
    // always executed
  });
