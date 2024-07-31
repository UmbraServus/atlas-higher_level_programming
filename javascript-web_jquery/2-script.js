#!/usr/bin/node
// using jquery add click to div to change header text color to red
$(document).ready(function () { 
  $('#red_header').click(function () { 
    $('header').css('color', 'red');
  });
});
