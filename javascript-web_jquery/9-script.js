#!/usr/bin/node
// fetches data from given url and displays the value of hello from
// the fetch in the html tag div#hello.
$(document).ready(function () {
  const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
  
  $.get(url, function (data) {
    const greet = data.hello;
    $('#hello').text(greet);
  });
});
