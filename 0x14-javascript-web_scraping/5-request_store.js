#!/usr/bin/node
/**
*write the webpage requested to a file
*/
const url = process.argv[2];
const filePath = process.argv[3];
const request = require('request');
const fs = require('fs');
request.get(url, (err, response, body) => {
  if (err) { return; }
  fs.writeFile(filePath, body, 'utf8', (err) => {
    if (err) { console.log(err); }
  });
});
