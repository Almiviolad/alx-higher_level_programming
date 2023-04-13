#!/usr/bin/node
/**
*esrever: returns reversed list
*@list: list
*/
exports.esrever = function (list) {
  const length = list.length;
  const array = [];
  for (let i = 0; i < length; i++) {
    array.unshift(list[i]);
  }
  return array;
};
