-- displays score and how many scores are the same and lists them in descending order of score count.

SELECT score, count(score) AS number FROM second_table
GROUP BY score
ORDER BY count(score) DESC;
