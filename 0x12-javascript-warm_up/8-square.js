#!/usr/bin/node
const times = parseInt(process.argv[2]);
let sqr = '';
if (times) {
  for (let i = 0; i < times; i++) {
    sqr = '';
    for (let j = 0; j < times; j++) {
      sqr = sqr + 'X';
    }
    console.log(sqr);
  }
} else { console.log('Missing size'); }
