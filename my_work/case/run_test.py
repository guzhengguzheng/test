#执行case，并出报告
#discover；发现的用例 在目录里发现含有test_模式的用例
# runnr：执行的报告
# run：执行



import unittest
from  my_work.common import contants
from my_work.reports import HTMLTestRunnerNew

discover=unittest.defaultTestLoader.discover(contants.case_dir,pattern='test_*.py',top_level_dir=None)
with open(contants.report_dir,'wb+')as file:
    runner=HTMLTestRunnerNew.HTMLTestRunner(stream=file,title='报告',description='登录接口测试报告结果',tester='penny')

    runner.run(discover)