#!/usr/bin/node

const request = require('request');
const filmId = process.argv[2];
if (!filmId) {
  console.log('Need film id.');
  process.exit(1);
}

const url = `https://swapi-api.hbtn.io/api/films/${filmId}`;

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  const jsonData = JSON.parse(body);
  const { title } = jsonData;
  console.log(title);
})
