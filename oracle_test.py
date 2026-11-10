# SQL :

import oracledb

connection = oracledb.connect(
    user = 'SCOTT',
    password = 'TIGER',
    dsn = 'localhost:1521/orcl'
)
print("Oracle connection sucessful!")
connection.close()