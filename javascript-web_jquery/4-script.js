#!/usr/bin/node
// toggles between classes in the header using jquery
$(document).ready(function () {
  $('#toggle_header').click(function () {
    $('header').toggleClass('red').toggleClass('green')
  });
});
