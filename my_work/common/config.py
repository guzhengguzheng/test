import  configparser
from my_work.common import contants

class ReadConfig():
    def __init__(self):
        self.config=configparser.ConfigParser()
        self.config.read(contants.global_conf_dir,encoding='utf-8')
        self.open=self.config.getboolean('switch','open')

    def get(self,section,option):
        if self.open :
            self.config.read(contants.test1_conf_dir,encoding='utf-8')
            value=self.config.get(section,option)
            return  value
        else:
            self.config.read(contants.test2_conf_dir,encoding='utf-8')
            value = self.config.get(section,option)
            return value

if __name__ == '__main__':
    config=ReadConfig()
    value=config.get('api','pre_url')
    print(value)


#读取配置 一共三个配置
#先根据导入的模块 创建一个对象 然后用这个对象 先去读取总开关 （创建对象 read与getbooolean）
  #读的时候注意 read（路径，中文编译）取的时候注意 用get还是getboolean取，get（section，option）
# 根据总开关读出来的值（open）去判断接下来读取1还是2 然后return value 记住section，option不要写死
# 最终目的是取1或者2的值