#!/usr/bin/node
/*
Simple addition function that pulls from the input of cmd line.
*/

//function for addition
function add(a, b) {
    return a + b;
}

//get num1 and 2 and check if they are numbers
const num1 = parseFloat(process.argv[2]);
const num2 = parseFloat(process.argv[3]);
if (isNaN(num1) || isNaN(num2)) {
    console.log('NaN');
}

    //results of adding num1 and num2
else {
    const result = add(num1, num2);
    console.log(result);
}
