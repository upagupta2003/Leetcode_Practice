# Write your MySQL query statement below
select s.student_id, s.student_name, 
    sub.subject_name, 
    IFNULL(grouped.Attended_exams,0) as Attended_exams
from
    students s
cross join
    subjects sub
Left join
(
select e.student_id, e.subject_name, count(*) as Attended_exams 
from
    examinations e 
group by 
    e.student_id, e.subject_name
) grouped

on s.student_id = grouped.student_id and sub.subject_name = grouped.subject_name
order by s.student_id, sub.subject_name
