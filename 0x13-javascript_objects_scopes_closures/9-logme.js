#!/usr/bin/node
exports.logMe = (function (item) {
  let count = 0;
  return function con (item) {
    console.log(count + ': ' + item);
    return (count++);
  };
}());
