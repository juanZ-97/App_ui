
"""
@ Author：YueC
@ Description：
"""
import pytest
from utils import shell

if __name__ == '__main__':
    pytest.main(['-v', '--maxfail=30', './tests/test_case/test01_login.yml', '--alluredir', 'report/test'])
    shell.Shell.invoke('allure generate report/test --clean')
    shell.Shell.invoke('allure open allure-report')

