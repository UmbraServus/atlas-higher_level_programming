#!/usr/bin/node

// get the request module 
const request = require('request');
// get the id or dfault to 18
const charId = process.argv[3] || 18;
// get the base url
const url = process.argv[2];
if (!url) {
  console.error('Need URL');
}
// get request to base url
request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  // get data and parse it for needed char info.
  let jsonData = JSON.parse(body);
  let charUrl = null;
  for (const film of jsonData.results) {
    for (const charsUrl of film.characters) {
      // get character URL
      if (charsUrl.endsWith(`/${charId}/`)) {
        charUrl = charsUrl;
        break;
      }
    }
    if (charUrl) {
      break;
    }
  }
  // request for data of character to count length of films parameter.
  if (charUrl) {
    request(charUrl, (error, response, body) => {
      if (error) {
        console.error('request failed', error);
        return;
      }

      // console.log(response.statusCode);
      const charData = JSON.parse(body);
      const { films } = charData;
      console.log(films.length);

    });
  }
});
