select p2.name as Employee
from Employee as p1
join Employee as p2
on p2.managerId=p1.id and p2.salary>p1.salary
