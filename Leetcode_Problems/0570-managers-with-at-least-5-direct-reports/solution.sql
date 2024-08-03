# Write your MySQL query statement below
Select name
    from Employee 
    where id in
    (SELECT 
            ManagerId
        FROM Employee
        GROUP BY ManagerId
        HAVING COUNT(ManagerId) >= 5
    )
