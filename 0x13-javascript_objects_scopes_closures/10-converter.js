#!/usr/bin/node
/**
*converts from base 10 to anoyher base
*/
exports.converter = function (base) {
  return function (number) {
    return (number.toString(base));
  };
};
