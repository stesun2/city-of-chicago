-- Find the employee being paid the most
SELECT * FROM employees WHERE annual_salary = (SELECT MAX(annual_salary) FROM employees);

-- Find the employee being paid the least
SELECT * FROM employees WHERE annual_salary = (SELECT MIN(annual_salary) FROM employees) LIMIT 1;

-- Find the department with the highest average salary
SELECT
  department, AVG(annual_salary) as average_salary
FROM
  employees
GROUP BY
  department
ORDER BY
  average_salary DESC
LIMIT
  1;

-- Find the department with the lowest average salary
SELECT
  department, AVG(annual_salary) as average_salary
FROM
  employees
GROUP BY
  department
ORDER BY
  average_salary ASC
LIMIT
  1;

-- Find the average salary difference between full time and part time workers
SELECT
  (SELECT ROUND(AVG(annual_salary)) FROM employees WHERE employees.full_or_part_time = 'F') -
  (SELECT ROUND(AVG(annual_salary)) FROM employees WHERE employees.full_or_part_time = 'P') as difference;

-- Find the most common first name
SELECT
  first_name, COUNT(first_name)
FROM
  employees
GROUP BY
  first_name
ORDER BY
  COUNT(first_name) DESC
LIMIT 1;

-- Find the most common last name
SELECT
  last_name, COUNT(last_name)
FROM
  employees
GROUP BY
  last_name
ORDER BY
  COUNT(last_name) DESC
LIMIT 1;

-- If there are people with the same name, find what their job titles, departments, and annual salaries are
SELECT
  first_name, last_name, job_title, department, annual_salary, COUNT(*)
FROM
  employees
GROUP BY
  first_name, last_name, job_title, department, annual_salary
HAVING
  COUNT(*) > 1
ORDER BY
  COUNT(*) DESC
LIMIT 5;
