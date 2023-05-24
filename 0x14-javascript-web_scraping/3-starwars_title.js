#!/usr/bin/node
/**
*prints status code of a get request
*/
const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + id;
const request = require('request');
request.get(url, (err, response, body) => {
  if (err) { return; }
  const movieData = JSON.parse(body);
  console.log(movieData.title);
});
