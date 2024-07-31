#!/usr/bin/node
// using jquery add class red to header
$(document).ready(function () {
  $('#red_header').click(function () {
    $('header').addClass('red');
  });
});
