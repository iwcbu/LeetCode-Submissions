# Write your MySQL query statement below
SELECT Email
FROM Person
GROUP BY email
HAVING Count(Email) > 1

