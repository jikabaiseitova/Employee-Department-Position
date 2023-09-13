---Department---
SELECT * FROM employee_department;

INSERT INTO employee_department
(name, address)
VALUES
('sales_department', 'Isanova,24'),
('it_department', 'Moscovskaya,13'),
('accounting_department', 'Kievskaya,100'),
('customer_service_department', 'Gogolya,5');

SELECT * FROM employee_department;

---Position---
SELECT * FROM employee_position;

INSERT INTO employee_position
(name)
VALUES
('Active Sales Manager'),
('Direct Sales Manager'),
('Web Designer'),
('It recruiter'),
('Accountant'),
('Chief Accountant'),
('Account Manager'),
('Head Of Sales Department');

SELECT * FROM employee_position;

---Employee---
SELECT * FROM employee_employee;

INSERT INTO employee_employee
(fullname, birth_date, salary, receipt_date, department_id, position_id)
VALUES
('Asan Asanov', '1977-12-12', 80000, '2000-06-13', 1, 8),
('Roza Abenova', '1996-01-22', 40000, '2020-06-13', 1, 6),
('Maksat Dairov', '1988-02-15', 30000, '2022-04-15', 1, 2),
('Ayana Temirova', '1989-03-26', 20000, '2022-06-13', 1, 4),

('Bilal Adenov', '1996-02-24', 50000, '2020-06-13', 2, 3),
('Gulya Sultanova', '1996-07-17', 40000, '2020-06-13', 2, 4),
('Roman Ten', '1978-01-29', 30000, '2012-04-15', 2, 5),
('Diana Kim', '1979-03-28', 20000, '2010-06-13', 2, 5),

('Dair Ernst', '1986-07-24', 50000, '2020-06-12', 3, 5),
('Aida Amanova', '1986-08-17', 40000, '2020-06-12', 3, 6),
('Sultan Nasyrov', '1987-09-29', 30000, '2022-04-14', 3, 7),
('Irina Hakamada', '1987-10-28', 20000, '2022-06-12', 3, 1),

('Vlada Vilena', '1977-04-04', 50000, '2017-05-12', 4, 8),
('Aya Nasyr', '1989-05-02', 40000, '2023-01-12', 4, 7),
('Dastan Pak', '1970-07-01', 30000, '2015-02-14', 4, 6),
('Mars Kazybaev', '1970-11-27', 20000, '2011-03-12', 4, 5);


SELECT * FROM employee_employee;

---a---
SELECT 
	fullname,
	salary
FROM 
	employee_employee AS e
ORDER BY 
	salary DESC;

---b---
SELECT 
	fullname,
	birth_date,
	receipt_date
FROM 
	employee_employee AS e
ORDER BY 
	birth_date DESC,
	receipt_date ASC;
	
---c---
SELECT 
	fullname, 
	salary 
FROM 
	employee_employee AS e 
WHERE 
	salary > 20000 
	AND 
	salary < 50000;

---d---
SELECT 
	fullname
FROM 
	employee_employee AS e 
WHERE 
	department_id = 4
ORDER BY
	fullname ASC;
	

---e---
SELECT * FROM employee_employee;
--OBSHEE KOLICHESTVO	
SELECT * FROM employee_employee  WHERE department_id = 1;
--count
SELECT COUNT(*) FROM employee_employee  WHERE department_id = 1;

SELECT 
	DISTINCT name,
	(
        SELECT COUNT(id) FROM employee_employee 
    WHERE department_id = d.id
    ) AS employee_count
FROM 
	employee_department AS d
INNER JOIN employee_employee AS e
	ON d.id = e.department_id
ORDER BY 
	name ASC;

---f---
SELECT 
	 DISTINCT name,
	(
        SELECT AVG(salary) FROM employee_employee 
    WHERE department_id = d.id
    ) AS salary_count
FROM 
	employee_department AS d
INNER JOIN employee_employee AS e
	ON d.id = e.department_id
ORDER BY 
	name ASC;
	
---g---
SELECT * FROM employee_employee;

SELECT 
	fullname,
	d.name AS department,
	p.name AS position
FROM
	employee_employee AS e
INNER JOIN employee_department AS d
	ON e.department_id = d.id
INNER JOIN employee_position AS p
	ON e.position_id = p.id;




