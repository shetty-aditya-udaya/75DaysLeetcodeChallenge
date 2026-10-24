# Write your MySQL query statement below
select id, 
case
when p_id is Null then 'Root'
when id in (select p_id from tree) then 'Inner'
else 'Leaf'
END as type
from tree;