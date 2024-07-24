#!/usr/bin/node
/*
stores strings in an array of strings and iterates thru it put to std out.
*/
const arrayVarStrings = ['C is fun', 'Python is cool', 'JavaScript is amazing'];
let i = 0;
while (arrayVarStrings[i] !== undefined) {
  console.log(arrayVarStrings[i]);
  i++;
}
