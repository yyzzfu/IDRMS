import pytest
from selenium import webdriver
from TestDatas import common_datas as CD
from PageObjects.login_page import LoginPage
from PageLocators.login_page_locators import LoginPageLocator as loc1
import time
from Common.do_mysql import DoMysql


driver = None


@pytest.fixture(scope='session')   # 所有的.py文件只运行一次
def enter_the_homepage():
    global driver    # 声明全局变量
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(CD.web_login_url)
    # 需手动输入验证码
    LoginPage(driver).input_text(loc1.username_ele, 'admin')
    LoginPage(driver).input_text(loc1.password_ele, 'e2020jl')
    while True:
        time.sleep(10)
        if LoginPage(driver).get_title() == '智能配电房监测系统登录':
            LoginPage(driver).click_element(loc1.click_button)
        if LoginPage(driver).get_title() == '智能配电房监测系统':
            break
        else:
            LoginPage(driver).clear_input(loc1.code_ele)
    # 不需手动输入验证码
    # login_sucess.login_sucess(driver)
    yield driver
    driver.quit()


@pytest.fixture()   # 每个测试用例都执行一次
def refresh():  # 用例执行前刷新页面
    global driver   # 全局变量
    LoginPage(driver).refresh_page()


@pytest.fixture(scope='class')
def delete_table_sys_user():
    # sql = 'DELETE FROM sys_user WHERE login_name <> "{}" and login_name <> "{}" and login_name <> "{}"'.format('thinkgem', 'idrmstest', 'idrmstest1')
    sql = 'DELETE FROM sys_user WHERE login_name <> "{}"'.format('thinkgem')
    DoMysql().delete_datas_from_table_with_sql(sql)


@pytest.fixture(scope='class')
def delete_table_ar_distribution_room():
    DoMysql().delete_all_datas_from_table('ar_distribution_room')


@pytest.fixture(scope='class')
def delete_table_ar_transformer():
    DoMysql().delete_all_datas_from_table('ar_transformer')


@pytest.fixture(scope='class')
def delete_table_ar_switch_cabinet():
    DoMysql().delete_all_datas_from_table('ar_switch_cabinet')


@pytest.fixture(scope='class')
def delete_table_ar_monitor_equipment():
    DoMysql().delete_all_datas_from_table('ar_monitor_equipment')


@pytest.fixture(scope='class')
def delete_table_ar_data_point():
    DoMysql().delete_all_datas_from_table('ar_data_point')


@pytest.fixture(scope='class')
def delete_table_sys_area():
    DoMysql().delete_all_datas_from_table('sys_area')


@pytest.fixture(scope='class')
def delete_table_ar_control_point():
    DoMysql().delete_all_datas_from_table('ar_control_point')


