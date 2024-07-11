-- first return the employees where employees' id does match up with the employeeUNI id
-- SELECT IF(unique_id, employeeUNI.unique_id, null), name FROM employees
-- JOIN employeeUNI
-- WHERE employees.id = employeeUNI.id
-- # then write a statement to make the unique_id NULL

-- solution from leetcode:
SELECT eu.unique_id AS unique_id, e.name
FROM Employees e
LEFT JOIN EmployeeUNI eu USING(id)