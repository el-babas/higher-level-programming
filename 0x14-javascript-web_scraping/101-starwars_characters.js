#!/usr/bin/node
const axios = require('axios').default;

// Example: 3 = “Return of the Jedi”.
const api = 'https://swapi-api.hbtn.io/api/films/';

async function getData (url) {
  try {
    const response = await axios.get(url);
    if (response.status === 200) {
      return response.data;
    }
  } catch (err) {
    console.log(err.message);
  }
}

async function showCharacters (url) {
  const film = await getData(url);
  const characters = film.characters;
  for (let i = 0; i < characters.length; i++) {
    const character = await getData(characters[i]);
    console.log(character.name);
  }
}

showCharacters(api.concat(process.argv[2]));
