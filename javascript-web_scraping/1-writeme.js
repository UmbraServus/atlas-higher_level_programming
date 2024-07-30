#!/usr/bin/node
/*
simple use of the writefile function in fs module.
*/

const fs = require('fs');
const filePath = process.argv[2];
const strData = process.argv[3];

if (!filePath || !strData) {
  console.error('Not enough arguments');
  process.exit(1);
}

fs.writeFile(filePath, strData, 'utf8', (err) => {
  if (err) {
    console.error(err);
  }
  // console.log('File write was successful');
});
