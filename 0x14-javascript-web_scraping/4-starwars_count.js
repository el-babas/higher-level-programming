#!/usr/bin/node
const axios = require('axios').default;

// https://swapi-api.hbtn.io/api/films/
const api = process.argv[2];
/**
 * Request status code.
 */
axios.get(api, {
}).then((response) => {
  // handle success
  let count = 0;
  const films = response.data.results;
  films.forEach(res => {
    res.characters.forEach(char => {
      // ID Wedge Antilles = 18.
      if (char.includes('18')) count++;
    });
  });
  console.log(count);
}).catch((error) => {
  // handle error
  console.log(error.message);
});
