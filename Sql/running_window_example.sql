/*
Original challenge posted by user pmatseykanets on Codewars.com
table posts schema:
	- created_at

required return table schema:
	- date(DATE)
	- count(INT)
	- total(INT) cumulative of previous count, running total
should be order by date asc

Example output:
date       | count | total
-----------+-------+-------
2017-01-26 |    20 |    20
2017-01-27 |    17 |    37
2017-01-28 |     7 |    44
2017-01-29 |     8 |    52
...
*/

-- my solution (verified)

WITH cte
as(
SELECT CAST(created_at as date) as date,
COUNT(*) as count
FROM posts
GROUP BY CAST(created_at as date)
ORDER BY 1
)

-- apply running window on sum of count over date(asc) and cast running total to int
SELECT *, 
CAST(SUM(count) OVER ( ORDER BY date rows between unbounded preceding and current row) as int) as total 
FROM cte;
