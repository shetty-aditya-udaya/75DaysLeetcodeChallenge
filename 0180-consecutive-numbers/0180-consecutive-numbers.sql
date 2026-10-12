# Write your MySQL query statement below
select distinct log1.num as ConsecutiveNums
from logs as log1,logs as log2,logs as log3
where log1.id + 1 = log2.id AND
log2.id + 1 = log3.id AND
log1.num = log2.num AND
log2.num = log3.num;