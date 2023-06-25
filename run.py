import pytest
from utils import shell

if __name__ == '__main__':
    # pytest.main(['-v', '--maxfail=30', './tests/test_case/test06_play_media_controls.yml', '--alluredir', 'report/test'])
    pytest.main(['-v', '--maxfail=30', './tests/test_case', '--alluredir', 'report/test'])
    # pytest.main(['-v', '--maxfail=30', './tests/test.yml', '--alluredir', 'report/test'])
    # 调试时暂时注释掉以下两行
    # shell.Shell.invoke('allure generate report/test --clean')
    # shell.Shell.invoke('allure open allure-report')

