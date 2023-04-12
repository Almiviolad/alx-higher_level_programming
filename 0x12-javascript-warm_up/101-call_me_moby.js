#!/usr/bin/node
module.callMeMoby = function (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
};
