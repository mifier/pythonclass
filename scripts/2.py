#-*-coding:GBK -*-
# �� 0002 ��: �� 0001 �����ɵ� 200 �������루�����Ż�ȯ�����浽 MySQL ��ϵ�����ݿ��С�


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
        #  �������ݿⲢ�����α�
            sql = "insert into %s(Activationcode,used) VALUES ('%s',1)"
            data = (tableName, code)
            self.cursor.execute(sql % data)    #ִ��sql���
            print(str(tableName)+":"+str(i)+" "+ code)
        self.connect.commit()  # �ύ���
        print(str(tableName)+"�����ݲ������")
       


    def create_table(self,name):
        self.cursor.execute('SHOW TABLES IN %s;' % self.db)  # sql��䣬�鿴���
        tables = self.cursor.fetchall()  # fetchall()ִ�в�ѯʱ����ȡ������������У�һ�й���һ��Ԫ�飬�ٽ���ЩԪ��װ��һ��Ԫ�鷵��
        findtables = False  # �����ж����
        for table in tables:
            if name in table:
                findtables = True
                print(str(name)+'����Ѿ�����')
        if not findtables:
           self.cursor.execute('''
                        CREATE TABLE %s(
                        id INT NOT NULL AUTO_INCREMENT,
                        Activationcode VARCHAR(32),
                        used boolean,
                        PRIMARY KEY (id));
            ''' % name)  # SQL��䣬�����������Ĳ�������
           self.connect.commit()  # �ύ���
           print('�ɹ�����' + str(name) + '���')
    
    def close(self):
        self.cursor.close()  # �ر��α�
        self.connect.close()  # �ر�����
        


        
def open_txt(TxtPath):   #��ȡtxt����
    file_handle = open(TxtPath, mode='r+')
    Activationcode_Total = file_handle.read()
    List_Activationcode = Activationcode_Total.split("\n")
    List_Activationcode.pop()  # ����ĩβ�Ŀ���
    file_handle.close()
    return List_Activationcode


if __name__ == '__main__':   
    TxtPath = './soures/List_Activationcode.txt'
    List_Activationcode = open_txt(TxtPath)  # ��ȡtxt����
    mysql = MySQL(host='db4free.net',port=3306,user='wangfei',passwd='12345678',db='wangfei_db')
    mysql.create_table("Activationcode_table")
    mysql.save_to_mysql(List_Activationcode, "Activationcode_table")
    mysql.close




