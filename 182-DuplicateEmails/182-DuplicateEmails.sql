-- Last updated: 8/12/2026, 12:22:10 PM
SELECT email AS Email
FROM Person
GROUP BY email
HAVING COUNT(email) > 1;