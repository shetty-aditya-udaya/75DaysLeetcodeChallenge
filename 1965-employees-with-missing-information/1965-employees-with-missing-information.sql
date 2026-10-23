# Write your MySQL query statement below
select e.employee_id
from employees e
left join salaries s
on e.employee_id = s.employee_id
where s.employee_id is null
Union
SELECT S.employee_id
FROM Salaries S
LEFT JOIN Employees E
    ON S.employee_id = E.employee_id
WHERE E.employee_id IS NULL
order by employee_id;