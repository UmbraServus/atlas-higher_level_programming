-- lists cities ids and names and also gets data for states name.
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = state.id;