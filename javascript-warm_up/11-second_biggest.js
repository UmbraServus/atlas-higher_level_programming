#!/usr/bin/node
/*
finds second biggest number from a given list
*/

//function for searching for second biggest.
function findSecondLargest(numbers) {
    let largest = -Infinity;
    let secondLargest = -Infinity;
    for (let num of numbers) {
        if (num > largest) {
            secondLargest = largest;
            largest = num;
        } else if (num > secondLargest && num < largest) {
            secondLargest = num;
        }
    }
    return secondLargest;
}

if (process.argv.length <= 3 || parseInt(process.argv[2]) == 1) {
    console.log(0);
} else {
    const numbers = process.argv.slice(2).map(Number).filter(num => Number.isInteger(num));
    const secondLargest = findSecondLargest(numbers);
    console.log(secondLargest);
}