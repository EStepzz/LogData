#coding=utf-8
import psycopg2
import datetime
import time

class DbSomething():
    def __init__(self,ip,database,username, password,port=5432):
        self.ip = ip
        self.database = database
        self.username = username
        self.password = password
        self.port = port
    '''如果把connection写到__init__中，每次初始化类就好？可以一试'''
    def connection(self):
        conn = psycopg2.connect(host=self.ip,
                                database=self.database,
                                user=self.username,
                                password=self.password,
                                port=self.port)
        cur = conn.cursor()
        return cur, conn

    '''创建表操作'''
    def creatTable(self, sql):
        cur, conn = self.connection()
        cur.execute(sql)
        print ("table is created")
        conn.commit()
        cur.close()
        conn.close()

    '''插入数据
    #table，which table insert to
    #data,what to insert
    '''
    def Insert(self,sql):
        pass

    '''
    #通过输入查询条件返回查询结果
    #table
    #conditions
    '''
    def search(self):
        v1 =[]
        v2=[]
        '''sql = select ctime ,count(*)
                from qps
                group by ctime order by ctime
              '''
        sql = 'select ctime ,count(*) from qps group by ctime order by ctime'
        cur, conn = self.connection()
        cur.execute(sql)
        data = cur.fetchall()
        #data list type

        for i in data:
            date = datetime.datetime.strftime(i[0], '%Y-%m-%d %H:%M:%S')
            print (type(date),type(i[1]))
            v1.append(date)

            v2.append(i[1])
        cur.close()
        conn.close()
        return v1,v2