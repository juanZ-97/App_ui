import pytest
from utils import shell

if __name__ == '__main__':
    # pytest.main(['-v', '--maxfail=30', './tests/test_case/test02_play_entry.yml', '--alluredir', 'report/test'])
    # pytest.main(['-v', '--maxfail=30', './tests/test_case/test09_listen_collect.yml', '--alluredir', 'report/test'])
    # pytest.main(['-v', '--maxfail=30', './tests/test_case/test10_listen_buy&history.yml', '--alluredir', 'report/test'])
    # pytest.main(['-v', '--maxfail=30', './tests/test_case/test11_listen_other.yml', '--alluredir', 'report/test'])
    # pytest.main(['-v', '--maxfail=30', './tests/test_case/test17_home_sound_lover.yml', '--alluredir', 'report/test'])
    # pytest.main(['-v', '--maxfail=30', './tests/test_case/test21_enter_live.yml', '--alluredir', 'report/test'])
    # pytest.main(['-v', '--maxfail=30', './tests/test_case/test22_live_basic_01.yml', '--alluredir', 'report/test'])
    pytest.main(['-v', '--maxfail=30', './tests/test_case', '--alluredir', 'report/test'])
    # pytest.main(['-v', '--maxfail=30', './tests/test.yml', '--alluredir', 'report/test'] )
    # 调试时暂时注释掉以下两行
    # shell.Shell.invoke('allure generate report/test --clean')
    # shell.Shell.invoke('allure open allure-report')

