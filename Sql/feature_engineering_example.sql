/*
Original challenge posted by user A.Partridge on Codewars.com
Two tables:
	top_half:
		- id
		- heads
		- arms
	bottom_half:
		- id
		- legs
		- tails
	
	output schema:
		- id
		- heads
		- legs
		- arms
		- tails
		- species
	
	For the species, if the monster has more heads than arms, more tails than legs, or both, it is a 'BEAST' else it is a 'WEIRDO'. 
	This needs to be captured in the species column.
*/

-- my solution (verified)
-- feature engineering, one of the most commonly used techniques during data clean and preparation for Machine Learning model training.
-- adding new features/characteristics to the dataset by combining other columns to give more meaningful analysis
SELECT t.id,
       t.heads,
       b.legs,
       t.arms,
       b.tails,
       CASE
           WHEN t.heads > t.arms then 'BEAST'
           WHEN b.tails > b.legs then 'BEAST'
           ELSE 'WEIRDO'
       END as species
FROM
top_half t
LEFT JOIN bottom_half b ON t.id = b.id
ORDER BY species;