#!/usr/bin/node
/**
*Define s a square class
*/
const Square1 = require('./5-square.js');
class Square extends Square1 {
  constructor (size) {
      super(size);
  }

    charPrint(c) {
	if (!c) {
	    c = 'x';
	}
	for (let i = 0; i < this.height; i++) {
      let wid = '';
      for (let j = 0; j < this.width; j++) {
          wid += c;
      }
      console.log(wid);
    }
  }

	
}
module.exports = Square;
