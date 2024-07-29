#!/usr/bin/node
/*
simple use of the writefile function in fs module.
*/

const fs = require('fs');
const filePath = process.argv[2];
const str_data = process.argv[3];

if (!filePath || !str_data) {
  console.error('Not enough arguments');
  process.exit(1);
}

fs.writeFile(filePath, str_data, 'utf8', (err) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log('File write was successful');
})