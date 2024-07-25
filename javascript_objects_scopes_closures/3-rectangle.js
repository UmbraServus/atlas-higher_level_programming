#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w >= 0 && h >= 0) {
      this.width = w;
      this.height = h;
    }
  }

  print() {
    let rectangle = '';
      for (let rows = 0; rows < this.height; rows++) {
        for (let columns = 0; columns < this.width; columns++) {
            rectangle += 'X';
        }
        if (rows < this.height - 1) {
            rectangle += '\n';
        }
    }
    console.log(rectangle);
  }
}

module.exports = Rectangle;
