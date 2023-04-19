import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="imran",
    password="19871944",
    database="wt"
)

mycursor = mydb.cursor()

class Site:
    @staticmethod
    def insert(site,case1,case2,case3,case4,case5):
        sql = "INSERT INTO sites  VALUES (null, %s,%s,%s,%s,%s,%s)"
        val = (site,case1,case2,case3,case4,case5)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "Site inserted.")
    
    @staticmethod
    def clear():
        sql = "TRUNCATE  sites"
        mycursor.execute(sql)
        mydb.commit()
        print(mycursor.rowcount, "Table sites emptied.")

class Request:
    @staticmethod
    def insert(site,url,typ,method,status,location,sharing_technique):
        sql = "INSERT INTO requests  VALUES (null, %s,%s,%s,%s,%s,%s,%s)"
        val = (site,url,typ,method,status,location,sharing_technique)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "Request inserted.")
    
    @staticmethod
    def clear():
        sql = "TRUNCATE  requests"
        mycursor.execute(sql)
        mydb.commit()
        print(mycursor.rowcount, "Table Requests emptied.")

class View:
    @staticmethod
    def request():
        sql = "SELECT * FROM top_requests"
        mycursor.execute(sql)
        result = mycursor.fetchall()
        return result
    
    @staticmethod
    def content_type():
        sql = "SELECT * FROM content_type"
        mycursor.execute(sql)
        result = mycursor.fetchall()
        return result
        
