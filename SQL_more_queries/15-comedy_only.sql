-- displays all shows linked to comedy genre by joining 
-- tv show genres to tv shows then tv genres to tv show genres.
SELECT title
FROM tv_shows
INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
INNER JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE name = 'Comedy'
ORDER BY title;