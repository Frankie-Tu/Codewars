/* Original challenge created by user matt c on Codewars.com
	Two tables:
		people table schema:
			-id
			-name
		sales table schema:
			-id
			-people_id
			-sale
			-price
	Rank people by number of sales
*/

-- my solution (verified)
SELECT
p.id,
p.name,
COUNT(s.sale) as sale_count,
ROW_NUMBER() OVER (ORDER BY COUNT(s.sale) desc) as sale_rank
FROM people p
LEFT JOIN sales s ON s.people_id = p.id
GROUP BY p.id, p.name
ORDER BY count(s.sale) desc;
