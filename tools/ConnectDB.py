#coding=utf-8
import psycopg2

class DbSomething():
    def __init__(self,url,database,username, password,port=5432):
        self.url = url
        self.database = database
        self.username = username
        self.password = password
        self.port = port
'''如果把connection写到__init__中，每次初始化类就好？可以一试'''
    def connection(self):
        conn = psycopg2.connect(self.database, self.username, self.password, self.port)
        cur = conn.cursor()
        return cur,conn

    '''插入数据
    #table，which table insert to
    #data,what to insert
    '''
    def Insert(self,table, data):
        pass

    '''
    #通过输入查询条件返回查询结果
    #table
    #conditions
    '''
    def search(self,table, conditons):
        pass

    #关闭数据库连接
    def closeDb(self,cur,conn):
        cur.close()
        conn.cloase()
