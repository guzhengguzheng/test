import os  #这是常量 存储各个文件的路径 一般是config和excel 因为需要读取config和excel的时候 才会用到路径
#总思想是从contants.py所在位置开始 用os.path.dirname 一层层往上返回到根目录
#再从根目录用os.path.join 往下一级级拼接到所需文件的路径 注意只能一级级的多次拼接，不可跨级拼接
#总原则是 先上再下 只有这样才能实现不同目录下的文件相互调用


#根目录
base_dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
base_dir2=os.path.dirname(os.getcwd())


#config路径
config_dir=os.path.join(base_dir2,'config')
global_conf_dir=os.path.join(config_dir,'global.conf')
test1_conf_dir=os.path.join(config_dir,'test1.conf')
test2_conf_dir=os.path.join(config_dir,'test2.conf')

#excel路径
data_dir=os.path.join(base_dir2,'data')
excel_dir=os.path.join(data_dir,'data_load.xlsx')

#log路径
log_dir=os.path.join(base_dir2,'log')
caselog_dir=os.path.join(log_dir,'case.log')

#用例路径
case_dir=os.path.join(base_dir2,'case')

#报告路径
reports_dir=os.path.join(base_dir2,'reports')
report_dir=os.path.join(reports_dir,'report.html')
