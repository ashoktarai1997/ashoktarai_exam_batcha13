"""SQL"""
# SQL1. Explain about the DML, DDL, TCL, DQL commands?

"""DML (Data Manipulation Language):it is used for manage data in  tables
Commands: INSERT, UPDATE, DELETE, MERGE.
DDL (Data Definition Language):it is Used for defining and managing all database objects.
Commands: CREATE, ALTER, DROP, TRUNCATE, COMMENT, RENAME.
TCL (Transaction Control Language): Manages changes made by DML statements.
Commands: COMMIT, ROLLBACK, SAVEPOINT, SET TRANSACTION.
DQL (Data Query Language): Used to select and retrive propose omly data from the database.
Commands: SELECT."""

# 2. What is a join? Explain all joins.
"""join: A SQL operation that combines rows from two or more tables based on a related column between them.
Inner Join: Returns records with matching values in both tables.
ON table1.common_column = table2.common_column;
Left Join (Left Outer Join): Returns all records from the left table and matched records from the right table; returns NULL for unmatched rows in the right table.

Right Join (Right Outer Join): Returns all records from the right table and matched records from the left table; returns NULL for unmatched rows in the left table.
Full Join (Full Outer Join): Returns records when there is a match in either left or right table records; returns NULL for unmatched rows in either table.
Cross Join: Returns the Cartesian product of the two tables.
Self Join: A table is joined with itself."""
# 3. Difference between Joins vs Subquery?
"""Joins:combine data from multiple tables into a single result set by matching columns between them
Subqueries:are nested queries executed separately before the outer query uses the result. Subqueries can be used for complex filtering and calculation.
"""
# 4. Find 3rd Highest Salary Of employee table ?
"""select * from emp where salary=>(select max(sal) from salary where salary =>(select max(sal) from salary))
SELECT DISTINCT salary
FROM employee
ORDER BY salary DESC
LIMIT 1 OFFSET 2;"""

# 5. Find the top seller in this month, according to date in customer table?
"""SELECT seller_id, SUM(amount) AS total_sales
FROM sales
WHERE MONTH(sale_date) = MONTH(CURRENT_DATE)
AND YEAR(sale_date) = YEAR(CURRENT_DATE)
GROUP BY seller_id
ORDER BY total_sales DESC;"""

# 6. Difference between Rank vs Dense_rank?
"""Rank: Provides ranks with gaps. If two rows are tied, the next rank will have a gap.
Dense_Rank: Provides ranks without gaps. If two rows are tied, the next rank will continue without a gap."""
"""unix"""

# 1. Copy a file one directory to another directory?

# 2. How do you find the process IF(PID) of a running process.
"""for finding the PID we use ps command for checking the the pid number after tha we can use
ps -ef | grep process_name."""
# 3. difference between chown vs chmod?
"""
chown: Changes the ownership of files or directories.
syntax:chown user:group filename
chmod: Changes the file('s permissions (read, write, execute).'
Syntax: chmod w/r/x filename
chown: in this command used for changing the owner ship.
chmod:in this command used for giving the permission who can access the file and modify.
"""
# 4. In a directory a find a file name abc.txt?
"""find <directory_location> <file_name>
"""
# 5. Why we are using sed command?

"""sed command basically used for find , replace ,search ,insert and delete word and lines in text file"""
# 6. How to list directories in Unix?
"""ls  -ltr
ls -al |grep d
ls -la
ls -al"""


"""python"""
# Difference between List vs tuple vs set vs dictionary?
"""Lists

It is enclosed with Square Bracket
Elements are stored in a specific order.
Elements can be added, removed, or modified after creation.
Elements can be accessed using their index.
Example: my_list = [1, 2, 3, "treenetra"]

Tuples

It Enclosed with
Similar to lists, but elements are stored in a specific order.
Elements cannot be modified after creation.
Elements can be accessed using their index.
It is Immutable.
Example: my_tuple = (1, 2, 3, "treenetra")


Sets

Elements are stored without a specific order.
Elements can be added or removed, but not modified.
Sets cannot contain duplicate elements.
removing duplicates, and mathematical operations like union, intersection.
Example: my_set = {7, 8, 9, "treenetra"}


Dictionaries

It is Collection of Key and value pair.
It is enclosed with Curli Bracket {}.
It is Mutable in nature.
Key must be unic.
Example: my_dict = {"name": "Ashok", "age": 29,}"""

"""garbage collection
 it can help up for free space means which object we no need any longer it free that space.it is a automatic memory managment."""

""" 10. Difference between Moudle and Packages
# module: module is a single file .
# packages:package can have multiple file."""
#
# 11.What is exception handling , how handel the exception in python , explain with each
# blo
# exception haldling is the process where we can avoid the abnormal termination of the program.

"Q1"
"What is decorator , write a decorator?"
"""DECORE"""
def is_prim(is_prime):
    def even_odd(num):
        if num % 2 == 0:
            return (num, "even")
        else:
            return is_prime(num)
    return even_odd
@is_prim
def is_prime(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return (num, "not a prime number")
        return (num, "its prime")
    else:
        return (num, "not a prime")
print(is_prime(3))
print(is_prime(10))


"Q7"
Li = [1,2,3,4], Li2 = [10,20,30]
Result = {1:10,2:20,3:30}

def dict_lists(list1, list2):
    result = {}
    length = len(list1) if len(list1)<len(list2) else len(list2)
    for i in range(length):
        result[list1[i]] = list2[i]
    return result
Li = [1, 2, 3, 4]
Li2 = [10, 20, 30]
result = dict_lists(Li, Li2)
print(result)

"Q8"
"""Handel a csv file, write first_name , email, phn_no, insert 5 data in this csv, then read
the csv and print in console bar"""

import  csv
data_col=["first_name" , "email", "phn_no"]
data_cols=[["ashok","abc@mail.com",2287887677],["ashok","zyx@mail.com",993375],["subhu","abc@mail.com",2287887677],["tapan","abc@mail.com",2287887677],["sanju","abc@mail.com",2287887677]]
with open("output.csv",mode="w") as file:
    csv_writer=csv.writer(file)
    csv_writer.writerow(data_col)
    csv_writer.writerows(data_cols)
with open("output.csv",mode="r") as file:
    csv_reader=csv.reader(file)
    for i in csv_reader:
        print(i)

# what is break,pass and continue

"break"
for i in range(10):
    if i == 5:
        break
    print(i)

"continue"
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

"pass"
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

"""selenium"""
# what is webdriver?
a webdriver is a tool that manage automating web browser
it allow to control and manage the web broswer.

# How to handel selective dropdown, write a snippet for it?
To handle a selective dropdown , you can use the Select class locater.
        driver.find_elements
from selenium import webdriver
from selenium.webdriver.support.ui import Select
driver = webdriver.Chrome()
driver.get("https:url.com")
driver.find_element(by.id,"dropdown_id")
select = Select(dropdown_element)
select.select_by_visible_text("Option 1")
# how many locaters in seleneium?
"""there are locates are 8 types
1.id
2.name
3.tagename
4.xpath
    absolute xpath
    relative xpath
5.css selector
6.link text
7.partial link text"""

# Explain the wait mechanism, write syntax and snippet for it
there are are two types of wait mechanism
.implicit wait
driver.implicitly_wait(10)
.explacit wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.get("https://example.com")
wait = WebDriverWait(driver, 10)  # seconds
element = wait.until(EC.(element_to_visible(By.ID, 'some_id')))
"""q10
import time 
from selenium import webdriver
from selenium.webdriver.common.by import by
from selenium.webdriver.common.actionchains import actionchains
driver = webdriver.Chrome()
driver.get("https:url.com")
actions = ActionChains(driver) 
actions. perform() ...
time. sleep(5)
driver.find_element(by.xpath,"//*[@class='container-fluid d-none d-sm-block']/div/div/ul/li[3]/a").click

//table[@id='livePreTable']/tbody/tr[2]/td[3]"""


actions = ActionChains(driver)
actions = actions. click(main_element) ...
actions. perform() ...
time. sleep(5)



