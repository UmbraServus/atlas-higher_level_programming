#!/usr/bin/node
// using jquery get some data and display it
$(document).ready(function () {
  const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';

  $.get(url, function (data) {
    const charName = data.name;
    $('#character').text(charName);
  });
});
