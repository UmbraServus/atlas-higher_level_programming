#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w >= 0 && h >= 0) {
      this.width = w;
      this.height = h;
    }
  }
}

  print() {
    let rectangle = ''
        for (let x = 0; x < this.height; x++) {
        for (let i = 0; i < this.width; i++) {
            rectangle += 'X';
        }
        if (x < this.height - 1) {
            rectangle += '\n';
        }
    }
    console.log(rectangle);
  }

}

module.exports = Rectangle;
