#!/usr/bin/node
/**
*prints all character of a movie
*/
const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + id + '/';
const request = require('request');
request.get(url, (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }
  const movieData = JSON.parse(body);
  let character = [];
  character = movieData.characters;
  let i = 0;
  while (i < character.length) {
    request.get(character[i], (err, response, body) => {
      if (err) {
        return;
      }
      const charData = JSON.parse(body);
      console.log(charData.name);
    });
    i++;
  }
});
