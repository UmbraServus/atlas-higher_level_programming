#!/usr/bin/node

if (process.argv.length < 3) {
    console.log("No argument");
} else if (process.argv.length < 4) {
    console.log(process.argv[2])
} else {
    for (let i = 2; i < process.argv.length; i++) {
        console.log(process.argv[i]);
    }
}