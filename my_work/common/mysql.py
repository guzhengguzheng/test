import pymysql
from my_work.common.config import ReadConfig
class Mysql:
    def __init__(self):
        config = ReadConfig()
        host=config.get('db', 'host')
        port=int(config.get('db', 'port'))  #从配置里读出来是字符串 需要转化成数值
        user=config.get('db', 'user')
        password=config.get('db', 'password')

        self.mysql=pymysql.connect(host=host,port=port,user=user,password=password)
        self.cursor=self.mysql.cursor()


    def fetch_one(self,sql):
        self.cursor.execute(sql)
        result=self.cursor.fetchone()
        return result


    def close(self):
        self.cursor.close()
        self.mysql.close()


if __name__ == '__main__':
    sql='select max(mobilephone) from future.member'
    mysql=Mysql()
    result=mysql.fetch_one(sql)
    print(result[0])
    mysql.close()
