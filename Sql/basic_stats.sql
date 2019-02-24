/*
original challenge posted by user matt c on Codewars.com

	table student schema:
		- id
		- name
	table result schema:
		- id
		- student_id
		- score
	
	write a function to find min, median and max score of students
*/

-- my solution (verified) 
SELECT MIN(r.score) as min,
PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY r.score) as median,
MAX(r.score) as max
FROM student s
LEFT JOIN result r ON s.id = r.student_id;