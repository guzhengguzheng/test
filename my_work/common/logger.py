import logging
from my_work.common import contants
import logging.handlers
from my_work.common.config import ReadConfig
config = ReadConfig()
#级别排序:CRITICAL > ERROR > WARNING > INFO > DEBUG
#debug : 打印全部的日志,详细的信息,通常只出现在诊断问题上
#nfo : 打印info,warning,error,critical级别的日志,确认一切按预期运行
#warning : 打印warning,error,critical级别的日志,一个迹象表明,一些意想不到的事情发生了,或表明一些问题在不久的将来(例如。磁盘空间低”),这个软件还能按预期工作
#error : 打印error,critical级别的日志,更严重的问题,软件没能执行一些功能
#critical : 打印critical级别,一个严重的错误,这表明程序本身可能无法继续运行

def get_logger(logger_name):
    logger=logging.getLogger(logger_name)
    logger.setLevel('DEBUG')
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s - [%(filename)s:%(lineno)s]'
    format=logging.Formatter(format)

    filename=contants.caselog_dir
    file_handle=logging.handlers.RotatingFileHandler(contants.caselog_dir,encoding='utf-8',maxBytes=20 * 1024 * 1024, backupCount=10)
    config = ReadConfig()
    file_level = config.get('log', 'file_handle')
    file_handle.setLevel(file_level)
    file_handle.setFormatter(format)

    console_handle = logging.StreamHandler()
    console_level = config.get('log', 'console_handle')
    console_handle.setLevel(console_level)
    console_handle.setFormatter(format)

    logger.addHandler(file_handle)
    logger.addHandler(console_handle)

    return logger

if __name__ == '__main__':
    logger=get_logger('login')
    logger.info('this is a error')



