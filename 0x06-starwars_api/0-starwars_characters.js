#!/usr/bin/node
const axios = require('axios');

function getMovieCharacters(movieId) {
  const url = `https://swapi.dev/api/films/${movieId}/`;

  return axios.get(url)
    .then(response => {
      const movieData = response.data;
      const characterUrls = movieData.characters;
      const characterNames = [];

      const characterPromises = characterUrls.map(characterUrl => {
        return axios.get(characterUrl)
          .then(characterResponse => {
            characterNames.push(characterResponse.data.name);
          });
      });

      return Promise.all(characterPromises)
        .then(() => characterNames);
    })
    .catch(error => {
      console.error(`Error: Unable to fetch movie data for Movie ID ${movieId}`);
      process.exit(1);
    });
}

if (process.argv.length !== 3) {
  console.log('Usage: node script.js <movie_id>');
  process.exit(1);
}

const movieId = process.argv[2];
getMovieCharacters(movieId)
  .then(characters => {
    for (const character of characters) {
      console.log(character);
    }
  });
