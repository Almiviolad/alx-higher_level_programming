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
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let wid = '';
      for (let j = 0; j < this.width; j++) {
        wid += 'X';
      }
      console.log(wid);
    }
  }

  rotate () {
    const temp = this.height;
    this.height = this.width;
    this.width = temp;
  }

  double () {
    this.height *= 2;
    this.width *= 2;
  }
} module.exports = Rectangle;
