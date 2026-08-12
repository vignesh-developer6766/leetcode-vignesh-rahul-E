-- Last updated: 8/12/2026, 12:22:05 PM
DELETE p1
FROM Person p1, Person p2
WHERE p1.email = p2.email
  AND p1.id > p2.id;