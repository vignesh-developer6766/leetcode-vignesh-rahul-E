-- Last updated: 8/12/2026, 12:21:41 PM
SELECT *
FROM Cinema
WHERE id % 2 = 1
  AND description <> 'boring'
ORDER BY rating DESC;