import re
from my_work.common import config
# 同一个py里，类和方法是平级的，引用的话直接引用即可，不需要通过类或者对象调用

class Context:
    config = config.ReadConfig()
    admin_mobilephone= config.get('info', 'admin_mobilephone')
    admin_pwd = config.get('info', 'admin_pwd')
    admin_user = config.get('info', 'admin_user')


def replace(s):
    p='\s\{(.*?)}'
    while re.search(p,s):
        m=re.search(p,s)
        key=m.group(1)
        if hasattr(Context, key):   #只是作为考虑 Context是否有key的方式，并且有的话 就动态赋值
            value=getattr(Context, key)
            s= re.sub(p, value,s,count=1)
        else:
            return None
    return s

