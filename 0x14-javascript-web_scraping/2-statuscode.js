#!/usr/bin/node
/**
*prints status code of a get request
*/
const url = process.argv[2];
const request = require('request');
request.get(url, (err, response, body) => {
  if (err) { return; }
  console.log('code: ' + response.statusCode);
});
