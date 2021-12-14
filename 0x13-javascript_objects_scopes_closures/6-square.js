#!/usr/bin/node

const SquareS = require('./5-square');

class Square extends SquareS {
  constructor (size) {
    super(size, size);
    this.size = size;
  }

  charPrint (c) {
    if (c) {
      for (let i = 0; i < this.size; i++) {
        let string = '';
        for (let j = 0; j < this.size; j++) {
          string += c;
        }
        console.log(string);
      }
    } else {
      super.print();
    }
  }
}
module.exports = Square;
