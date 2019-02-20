#这是注册接口的用例
import unittest
from ddt import ddt,data
from my_work.common.do_excel import DoExcel
from my_work.common import contants
from my_work.common.config import ReadConfig
from my_work.common.mysql import Mysql
from my_work.common.request import Request


@ddt
class Register_login(unittest.TestCase):
    #类属性和类方法 没什么区别 但是ddt只能用类属性
    # 关于接口的类里 新建对象 都放在类属性里 （excel和request对象）
    doexcel = DoExcel(contants.excel_dir, 'register')
    cases = doexcel.read()
    dorequest = Request()
    max_mysql = Mysql()

    def setup(self,sql):
        self.max_mobilephone=self.max_mysql.fetch_one(sql)[0]

    @data(*cases)
    def test_register(self,case):
        print('开始执行第{}条用例'.format(case.id))
        if case.data['mobilephone']=='${admin_mobilephone}':
            case.data['mobilephone']=int(self.max_mobilephone)+1
        else:
            print('报错啦')
            resp = self.dorequest.request(case.method, case.url, case.data)  #方法里访问类属性，可通过对象（self）
            # 和类（Register_login）来访问
            try:
                self.assertEqual(case.data,resp.text)
                self.doexcel.write(resp.text,'pass',case.id+1)
            except AssertionError as e:
                self.doexcel.write(resp.text, 'fail', case.id + 1)
                raise e


    def cloese(self):
        self.dorequest.close()
        self.max_mysql.close()


#
#
#
