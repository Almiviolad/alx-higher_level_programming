#!/usr/bin/node
const length = process.argv.length;
let greatest = 0;
let formerGreatest = 0;
if (length === 2 || length === 3) {
  console.log(0);
} else {
  for (let i = 2; i < length; i++) {
    if (parseInt(process.argv[i]) > greatest) {
      formerGreatest = greatest;
      greatest = process.argv[i];
    }
  }
  console.log(formerGreatest);
}
