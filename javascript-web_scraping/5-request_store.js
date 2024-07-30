#!/usr/bin/node
// using what I learned in writeme and the swapi tasks I was able to 
// get the data and write the data to a given file pathname.
 
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const filePath = process.argv[3];
if (!filePath) {
  console.error('No filepath');
  process.exit(1);
}
request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    process.exit(1);
  }
  // console.log(body);
  fs.writeFile(filePath, body, 'utf8', (err) => {
    if (err) {
      console.error(err);
      process.exit(1);
    }
    // console.log('file written succefully')
  });
});
