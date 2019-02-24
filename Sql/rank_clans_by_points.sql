/*
Original challenge posted by matt c on Codewars.com
	people table schema:
		- name
		- points
		- clan
		
	output table should follow this:
		- rank
		- clan
		- total_points
		- total_people
*/

-- my solution (verified answer)
WITH
cte
as(
SELECT  
      CASE
          WHEN clan = '' then '[no clan specified]'
          ELSE clan
      END as clan,
      SUM(points) as total_points,
      COUNT(name) as total_people
FROM people
GROUP BY clan
ORDER BY 2 desc
)

SELECT ROW_NUMBER() OVER (ORDER BY total_points desc) as rank,
        *
FROM cte;
