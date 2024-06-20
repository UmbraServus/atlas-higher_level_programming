-- lists genre and count of shows in the genre as long as they have a show. 
SELECT DISTINCT name
AS genre, count(show_id)
AS number_of_shows
FROM tv_genres
INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY genre ORDER BY number_of_shows DESC;