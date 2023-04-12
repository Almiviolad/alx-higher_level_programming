#!/usr/bin/node
/**
*Defines a recatngle class
*@h: height
*@w: weught
*/
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
      this.print = function () {
        for (let i = 0; i < h; i++) {
          let wid = '';
          for (let j = 0; j < w; j++) {
            wid += 'X';
          }
          console.log(wid);
        }
      };
    }
  }
} module.exports = Rectangle;
