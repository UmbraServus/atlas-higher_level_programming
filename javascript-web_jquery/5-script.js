#!/usr/bin/node
// append onto an ul a new li using jquery
$(document).ready(function () {
  $('#add_item').click(function () {
   $('.my_list').append('<li>Item</li>') 
  });
});
