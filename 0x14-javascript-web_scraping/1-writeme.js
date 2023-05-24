#!/usr/bin/node
/**
*writes to a file
*/
const filePath = process.argv[2];
const content = process.argv[3];
const fs = require('fs');
fs.writeFile(filePath, content, 'utf8', (err) => {
  if (err) {
    console.error(err);
  }
});
