#!/usr/bin/node
// adds new text to header
$(document).ready(function () {
  $('#update_header').click(function () {
    $('header').text("New Header!!!")
  });
});
