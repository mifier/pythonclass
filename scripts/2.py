#-*-coding:GBK -*-
# 第 0002 题: 将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中。


import pymysql

class MySQL:
    def __init__(self, host, port,user,passwd,db):
        connect = pymysql.Connect(
            host=host,
            port=port,
            user=user,
            passwd=passwd,
            db=db,
            charset='utf8'
        )
        self.connect=connect
        self.cursor = self.connect.cursor()
        self.db=db

    def save_to_mysql(self,DataList,tableName):
        
        for i,code in enumerate(DataList):        
        #  链接数据库并设置游标
            sql = "insert into %s(Activationcode,used) VALUES ('%s',1)"
            data = (tableName, code)
            self.cursor.execute(sql % data)    #执行sql语句
            print(str(tableName)+":"+str(i)+" "+ code)
        self.connect.commit()  # 提交语句
        print(str(tableName)+"的数据插入完成")
       


    def create_table(self,name):
        self.cursor.execute('SHOW TABLES IN %s;' % self.db)  # sql语句，查看表格
        tables = self.cursor.fetchall()  # fetchall()执行查询时，获取结果集的所有行，一行构成一个元组，再将这些元组装入一个元组返回
        findtables = False  # 辅助判断语句
        for table in tables:
            if name in table:
                findtables = True
                print(str(name)+'表格已经创建')
        if not findtables:
           self.cursor.execute('''
                        CREATE TABLE %s(
                        id INT NOT NULL AUTO_INCREMENT,
                        Activationcode VARCHAR(32),
                        used boolean,
                        PRIMARY KEY (id));
            ''' % name)  # SQL语句，创建表格，里面的参数设置
           self.connect.commit()  # 提交语句
           print('成功创建' + str(name) + '表格')
    
    def close(self):
        self.cursor.close()  # 关闭游标
        self.connect.close()  # 关闭连接
        


        
def open_txt(TxtPath):   #获取txt数据
    file_handle = open(TxtPath, mode='r+')
    Activationcode_Total = file_handle.read()
    List_Activationcode = Activationcode_Total.split("\n")
    List_Activationcode.pop()  # 弹出末尾的空行
    file_handle.close()
    return List_Activationcode


if __name__ == '__main__':   
    TxtPath = './soures/List_Activationcode.txt'
    List_Activationcode = open_txt(TxtPath)  # 获取txt数据
    mysql = MySQL(host='db4free.net',port=3306,user='wangfei',passwd='12345678',db='wangfei_db')
    mysql.create_table("Activationcode_table")
    mysql.save_to_mysql(List_Activationcode, "Activationcode_table")
    mysql.close




