#!/usr/bin/node
// get starwars data and display each item in an ul as a li.
$(document).ready(function () {
  const url = 'https://swapi-api.hbtn.io/api/films/?format=json'

  $.get(url, function (data) {
    const movies = data.results;
    movies.forEach(function (movie) {
      $('#list_movies').append('<li>' + movie.title + '</li>');
    });
  });
});
