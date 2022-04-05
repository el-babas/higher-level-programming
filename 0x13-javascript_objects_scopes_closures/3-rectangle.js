#!/usr/bin/node

/**
 * Class Rectangle that defines a rectangle.
 */
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const simbol = 'X';
    for (let i = 0; i < this.height; i++) {
      console.log(simbol.repeat(this.width));
    }
  }
}

module.exports = Rectangle;
