#!/usr/bin/node
/*
*/

let squareSize = parseInt(process.argv[2]);
let square = '';
if (isNaN(squareSize)) {
    console.log("Missing size");
}

else {
    for (let x = 0; x < squareSize; x++) {
        for (let i = 0; i < squareSize; i++) {
            square += 'X';
        }
        if (x < squareSize - 1) {
            square += '\n';
        }
    }
    console.log(square);
}