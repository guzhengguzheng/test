import unittest
from ddt import ddt,data
from my_work.common import do_excel
from my_work.common import contants
from my_work.common.request import Request
from my_work.common import context
from my_work.common import logger

@ddt
class Login(unittest.TestCase):  #创建的对象放在类属性里的话 下面方法调用该对象时 对象前面需要加self  否则会报错找不到该属性
    excel =do_excel.DoExcel(contants.excel_dir, 'login')
    cases = excel.read()
    request = Request()
    logger = logger.get_logger('login')

    @data(*cases)
    def test_login(self,case):
        self.logger.info('开始执行第{}条用例'.format(case.id))  #输出log信息
        case.data=context.replace(case.data)      #使用正则和反射动态替换case.data
        resp = self.request.request(case.method, case.url, case.data)  #获取响应值
        try:
            self.assertEqual(case.expected, resp.text)   #预期值（expected）跟resp.text进行对比
            self.logger.info('第{}条用例结果:pass'.format(case.id))  #输出log信息
            case.result='pass'
        except AssertionError as e:
            case.result='fail'
            self.logger.error('第{}条用例结果:fail'.format(case.id))
            raise e
        finally:
            self.excel.write(resp.text,case.result,case.id + 1)

    def tearDown(self):
        self.request.close()

#单元测试里 只有以test_开头的自定义方法才会被识别 所以不能用def close（）方法 不识别 不运行







