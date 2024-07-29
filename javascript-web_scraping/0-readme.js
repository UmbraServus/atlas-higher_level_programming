#!/usr/bin/node
/*
script that reads a file and prints the data to std out.
*/
const fs = require('fs');
const path = require('path');

const filePath = process.argv[2];

if (!filePath) {
  console.error('Missing filepath');
  return;
}

const absolutePath = path.resolve(filePath);

fs.readFile(absolutePath, 'utf8', (err, data) => {
  if (err) {
    console.error('Error:', err);
    return;
  }

  console.log(data);
})
