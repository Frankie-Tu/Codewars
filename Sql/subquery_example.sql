/*
Original challenge posted by user pmatseykanets on Codewars.com
Three tables:
	film_actor:
	 Column     | Type                        | Modifiers
	------------+-----------------------------+----------
	actor_id    | smallint                    | not null
	film_id     | smallint                    | not null
	last_update | timestamp without time zone | not null
	
	film:
 	 Column     | Type                        | Modifiers
	------------+-----------------------------+----------
	title       | character varying(255)      | not null
	film_id     | smallint                    | not null
	
	actor:
	 Column     | Type                        | Modifiers
	------------+-----------------------------+----------
	actor_id    | integer                     | not null 
	first_name  | character varying(45)       | not null
	last_name   | character varying(45)       | not null
	last_update | timestamp without time zone | not null
	
list the movies in alphabetical order(asc) where actor_id 105 and actor_id 122 casted together

desired ouput:
	title
-------------
Film Title 1
Film Title 2
...
*/

-- my solution (verified)
SELECT y.title FROM
(SELECT x.title, COUNT(*) as count
 FROM
	(SELECT f.title,
 	        fa.actor_id
	 FROM film f
	 LEFT JOIN film_actor fa ON f.film_id = fa.film_id
	 WHERE fa.actor_id  = 122 OR fa.actor_id = 105
	 GROUP BY f.title, fa.actor_id
	)x -- find films casted by the actors (distinct result)
 GROUP BY x.title
 )y -- since it was only showing distinct <film, actor> pairs from subquery x, now group by film name
WHERE y.count = 2 -- if the count is 2, it means both actors casted in the film.
ORDER BY y.title;