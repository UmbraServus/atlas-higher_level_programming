-- displays score, name from second table if name isnt null and orders it descending by score.
SELECT score, name FROM second_table WHERE name IS NOT null
ORDER BY score DESC;