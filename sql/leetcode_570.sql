SELECT employee1.name
FROM Employee employee1
JOIN (
    SELECT managerId, COUNT(*) 
    FROM Employee 
    GROUP BY managerId 
    -- HAVING managerId IS NULL
    HAVING COUNT(*) >= 5
) employee2 ON employee1.id = employee2.managerId

SELECT name From Employee
WHERE id in
(SELECT managerId FROM Employee
GROUP BY managerId
Having COUNT(*) >= 5)