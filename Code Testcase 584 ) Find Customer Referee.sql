select c.name
from Customer as c
where c.referee_id is null or c.referee_id !=2;
