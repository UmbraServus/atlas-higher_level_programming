#!/usr/bin/node
/*
factorial function that pulls from the input of cmd line.
*/

//function for factorial
function factorial(a) {
    if (a === 0) {
        return 1
    } else if (a < 0) {
        return 'cant be negative'
    } else {
        return a * factorial(a - 1);
    }
}

//get num and check if it is an int
const num = parseInt(process.argv[2]);
if (isNaN(num)) {
    console.log(1);
}

//results of factorial(num)
else {
    const result = factorial(num);
    console.log(result);
}
