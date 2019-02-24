/*
Original challenge posted by user matt c on Codewars.com
you want to count how many people have the same age and return the groups with 10 or more people who have that age.

people table schema
	id
	name
	age
return table schema
	age
	total_people
*/

-- my solution (verified)
-- Having is a simple yet powerful function used in data analysis to filter grouped data on condtion.
SELECT 
age,
COUNT(*) as total_people
FROM
people
GROUP BY age
HAVING COUNT(*) >=10;
