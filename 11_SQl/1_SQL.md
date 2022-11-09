# Commands
# 0_Run MYSQL in Command Prompt:
```sql
mysql -u root -p
```


# 1_Create Database:
```sql
create database databasename;
```
  
# 2_Show Database:
```sql
show databases;
```
  
# 3_Use database:
```sql
use databasename;
```

# 4_Create Tables:(CREATE)
```sql
CREATE TABLE tablename (stuID int, stuNAME varchar(50), stuAGE int, stuCITY varchar(50));
```
```sql
show tables;
```
## To view table structure:
```sql
desc tablename;
```
           

# 5_Insert in table:(INSERT)
```sql
INSERT INTO tablename (stuID, stuNAME, stuAGE, stuCITY) VALUES (1,'Ammar',20,'Hassanabdal');
```

# 6_View Table:(SELECT)
```sql
SELECT * FROM tablename;    
```  
# Specific view:
```sql
SELECT stuNAME FROM tablename;
SELECT stuAge FROM tablename;
```

# WHERE:
```sql
SELECT stuAGE FROM tablename where stuAGE <21;

SELECT * FROM tablename where stuAGE <21;
```

# 7_Add new column in table: (ALTER)
```sql
ALTER TABLE tablename ADD COLUMN columnname datatype;
```

# 8_Add value in new Column(UPDATE):
```sql
UPDATE tablename set columnname = "name" Where stuID=1;

UPDATE tablename set columnname = "name" Where stuAGE=12;
```

# 9_Delete:
## Delete row:
```sql
DELETE * FROM tablename WHERE stuID=1;
```
## Delete table: 
```sql
DROP table tablename;
```

# 10_Drop Column:(DROP)
```sql
ALTER table tablename DROP columnname;
```

# 11_ Modify Column:
```sql
ALTER table tablename CHANGE columnname newname datatype;

ALTER table tablename MODIFY stuID int UNIQUE;
```

# 12_ DIStINCT: (unique)
```sql
SELECT DISTINCT columnname FROM tablename;
```

# **Constraints:**
# 13_Not Null:
```sql
CREATE TABLE tablename (stuID int not null, stuNAME varchar(50), stuAGE int);
```

# 14_UniQue:
**UNIQUE**(ek value repeat ni hoo skti)
### Two Ways:
```sql
CREATE TABLE tablename (stuID int not null UNIQUE, stuNAME varchar(50), stuAGE int);
```
```sql
CREATE TABLE tablename (stuID int not null , stuNAME varchar(50), stuAGE int, UNIQUE(stuID));
```

# Drop Unique value:
```sql
alter table tablename Drop index stuID;
```

# 15_Primary Key:
(Unique hoo or Null na Hoo)
```sql
CREATE TABLE tablename (stuID int not null , stuNAME varchar(50), stuAGE int, PRIMARY KEY(stuID));
```

# Multiple Primary key:
```sql
CREATE TABLE tablename (stuID int not null , stuNAME varchar(50), stuAGE int not null, PRIMARY KEY(stuID,stuID));
```

# 16_Foreign Key:
(2 tables ko aps ma connect krti ha)
```sql
CREATE TABLE tablename (stuID int not null , Rollno int , stuNAME varchar(50), stuAGE int, PRIMARY KEY(stuID), Foreign Key(Rollno) REFRENCES name (stuID));
```

# 17_Check:
(means kis kis to add krna ha)
```sql
CREATE TABLE tablename (stuID int not null, stuNAME varchar(50), stuAGE int, CHECK (stuAGE >=18));
```

# For Multiple conditions:
```sql
CREATE TABLE tablename (stuID int not null, stuNAME varchar(50),stuCOUNTRY varchar(50), stuAGE int, CONSTRAINT CHK_tablename CHECK (stuAGE >=18 and stuCOUNTRY ='PAKISTAN'));
```

# 18_Default:
```sql
CREATE TABLE tablename (stuID int not null, stuNAME varchar(50),stuCOUNTRY varchar(50) DEFAULT 'PAKISTAN');
```

# 19_INDEX:
(Use to retrieve data faster)
## For whole table:
```sql
CREATE INDEX index_name ON tablename (stuID, stuNAME, stuAGE, stuCITY);
```

## For Column:
```sql
CREATE INDEX index_name ON tablename columnname;
```

# 20_Auto Increment:
```sql
CREATE TABLE tablename (SerialNO int not null AUTO_INCREMENT  , stuNAME varchar(50), stuAGE int, PRIMARY KEY(SerialNO));
```
