# Write your MySQL query statement below
select s.user_id,
    round(sum(case when c.action ='confirmed' then 1 else 0 end)/count(s.user_id),2) as confirmation_rate
from confirmations c Right join signups s
    on c.user_id = s.user_id
group by s.user_id


