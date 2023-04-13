#!/usr/bin/node
/**
* nbocurrence: returns number of ocurrence in alist
*@list: tge array to search
*@searchelment: the element to look for
*/
exports.nbOccurences = function (list, searchElement) {
  let occurence = 0;
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      occurence++;
    }
  }
  return (occurence);
};
