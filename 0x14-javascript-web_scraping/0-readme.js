#!/usr/bin/node
/**
*reads and prints the content of a file.
*/
const filePath = process.argv[2];
const fs = require('fs');
fs.readFile(filePath, 'utf8', (err, data) => {
  if (err) {
    console.err(err);
    return;
  }
  console.log(data);
});
