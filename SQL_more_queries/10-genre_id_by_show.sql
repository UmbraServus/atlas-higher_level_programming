-- selects shows, genre id and in order first by show then also by genre id in ascending.
SELECT title, genre_id FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id ORDER BY title ASC, genre_id ASC;