#!/usr/bin/node
const length = process.argv.length;
const first = parseInt(process.argv[2]);
let greatest = first;
let diff = Infinity;
let secg = first;
if (length === 2 || length === 3) {
  console.log(0);
} else {
  for (let i = 2; i < length; i++) {
    const current = parseInt(process.argv[i]);
    if (current > greatest) {
      secg = greatest;
      greatest = current;
    } else if ((greatest - current) < diff && greatest - current !== 0) {
      diff = greatest - current;
    }
  }
  if ((greatest - diff === -Infinity) || (greatest - diff < secg && secg !== greatest)) {
    console.log(secg);
  } else {
    console.log(greatest - diff);
  }
}
