#!/usr/bin/node
const arg = process.argv[2];
function factorial (n) {
  const par = parseInt(n);
  if (par) {
    if (n === 0) {
      return (1);
    }
    return (n * factorial(n - 1));
  } else { return (1); }
}
console.log(factorial(arg));
