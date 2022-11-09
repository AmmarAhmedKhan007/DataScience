# WHERE :
```sql
select * from customers;
select customerName, phone from 
customers where country='USA';
```
# ORDER BY :
```sql
select * from customers where country='USA' order by 'customerNumber';
```
# AND :   -- isi tarha OR , NOT be han
```sql
select * from customers where country='USA' AND creditLimit > 81700;  
select * from products;
```
# As :
```sql
select productName, productCode, buyPrice, buyPrice*10 AS NewPrice from products;
``` 
# IN :
```sql
select * from products where productLine IN ('Motorcycles','Classic Cars');
```
# NOT IN :
```sql
select * from products where productLine NOT IN ('Motorcycles','Classic Cars');
```
# BETWEEN :
```sql
select * from products where quantityInStock between 1000 AND 5000;
```