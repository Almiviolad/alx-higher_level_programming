#!/usr/bin/node
const str = 'C is fun';
const times = parseInt(process.argv[2]);
if (times) {
  for (let i = 0; i < times; i++) {
    console.log(str);
  }
} else { console.log('Missing number of occurrences'); }
