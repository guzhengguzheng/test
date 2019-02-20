#我们主要做项目的接口测试 接口测试的原理就是发送请求，查看响应是否一致 这个py用来检测 equro这个判断
#case运行 就是发送请求 case运行结束 就是接收响应
#发送请求时 传的参数值（method,url,data) 就是从excel里获取的 接收的响应 就是获得的数据（resp） 要写入excel的
# cookies 是从服务器返回的字符串信息 保存在客户端（浏览器）下一次发送请求的时候跟着发过去
import requests
import json
from my_work.common import do_excel
from my_work.common.config import ReadConfig
from my_work.common import  contants   #注意一层层目录之间用点连接

#总思想 带参数请求 两种清请求方式 最终目的获取响应数据 供case执行时 实际结果使用
class Request:

    def __init__(self):  #注意是init 不是int
        self.session = requests.sessions.session()  # 创建session对象，用session去发送请求 可保持cookie


    def request(self,method,url,data):  #参数的值在case模块再传入 先处理下参数格式
        method=method.lower()  # method统一处理成大写或小写，方便后面条件判断有个统一的判断值 （这个是防止粗心大小写混着写）
        config = ReadConfig()
        url=config.get('api','pre_url') +url #excel里的url只是部分，要拼接成完整的  注意拼接的顺序 pre要放在前面
        data = json.loads(data)
        if method=='get':   #接口的话 两种传参方式都会用到 写个条件判断 灵活选择传参方式 因为不同的传参方式要使用不同的请求
            resp=self.session.request(method,url,data)  #请求跟响应是在同一个python语句里
            return resp
        elif method=='post':
            resp = self.session.request(method,url,data)
            return resp
        else:
            print('method错误')

    def close(self):
            self.session.close()       #全部运行完一个接口的所有用例时，要记得关闭session  不然耗内存


if __name__ == '__main__':
    request=Request()
    resp=request.request('post','/member/register','{"mobilephone":"18021561255","pwd":"12345"}')
    print(resp.text)
    request.close()

#此处注意excel里不能有空格 空格都要去掉 否则会数据报错



