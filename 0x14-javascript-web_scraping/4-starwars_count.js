#!/usr/bin/node
const axios = require('axios').default;

// let count = 0;
// ID Wedge Antilles = 18.
const idCharacter = 'https://swapi-api.hbtn.io/api/people/18/';
// https://swapi-api.hbtn.io/api/films/
const api = process.argv[2];
/**
 * Request status code.
 */
axios.get(api)
  .then(function (response) {
    // handle success
    // const films = response.data.results;
    // films.forEach(function (element) {
    //   console.log(element.characters)
    //   if (element.characters.includes(idCharacter)) count++;
    // });
    // console.log(count);
    const films = response.data.results.filter(film => film.characters.includes(idCharacter));
    console.log(films.length);
  })
  .catch(function (error) {
    // handle error
    console.log(error.message);
  })
  .then(function () {
    // always executed
  });
