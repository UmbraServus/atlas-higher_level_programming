#!/usr/bin/node
/*
uses a variable x to take the first argv passed and prints x times "C is fun"
*/
const arg = process.argv[2];
let x = parseInt(arg);
if (isNaN(x)) {
  console.log("Missing number of occurences");
}
else {
  for (i = 0; i < x; i++) {
    console.log("C is fun");
    }
}
