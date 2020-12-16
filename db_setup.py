import dbconfig
import mysql.connector as mysql


connection=mysql.connect(host='locahost', user=dbconfig.db_user, password=dbconfig.db_password)


try:
    with connection.cursor() as cursor:
        _SQL="""CREATE DATABASE IF NO EXISTS crimemap"""
        cursor.execute(_SQL)
        _SQL="""CREATE TABLE IF NOT EXISTS crimemap.crimes(
        id int NOT NULL AUTO_INCREMENT,
        latitude FLOAT(10, 6),
        longitude FLOAT(10, 6),
        date DATETIME,
        category VARCHAR(50),
        description VARCHAR(1000),
        update_at TIMESTAMP,
        PRIMARY KEY (id))"""
        cursor.execute(_SQL)
    connection.commit()
finally:
    connection.close()