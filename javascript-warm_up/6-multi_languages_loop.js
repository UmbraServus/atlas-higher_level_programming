#!/usr/bin/node
/*
stores strings in an array of strings and iterates thru it put to std out.
*/
const array_var_strings = ["C is fun", "Python is cool", "JavaScript is amazing"];
let i = 0;
while (array_var_strings[i] != undefined) {
    console.log(array_var_strings[i]);
    i++
}
