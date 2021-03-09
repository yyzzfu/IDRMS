from Common.basepage import BasePage
from PageObjects.home_page import HomePage
import time
from PageLocators.ArchiveManagementLocators.monitoring_equipment_manage_locators import MonitoringEquipmentManageLocators as loc
from PageLocators.home_page_locators import HomePageLocator as loc_home


class MonitoringEquipmentManagePage(BasePage):

    # 编辑监控设备
    def edit_monitoring(self, room, monitoring_name, monitoring_type, mailing_address, network_connection_mode,
                        network_ip, network_port, domain_name, login_username, login_password, remark, mode):
        if room:
            room_choice_replace = str(loc.room_choice).replace('replace', room)
            # 展开所属配电房下拉框
            self.click_element(loc.room_select)
            # 选择配电房
            self.click_element(eval(room_choice_replace))
        if monitoring_name:
            # 输入监控设备名称
            if mode == '修改':
                self.clear_input(loc.monitoring_name)
            self.input_text(loc.monitoring_name, monitoring_name)
        if monitoring_type:
            # 选择监控设备类型
            monitoring_type_replace = str(loc.monitoring_type).replace('replace', monitoring_type)
            self.click_element(eval(monitoring_type_replace))
        if mailing_address:
            # 输入设备通信地址
            if mode == '修改':
                self.clear_input(loc.mailing_address)
            self.input_text(loc.mailing_address, mailing_address)
        if network_connection_mode:
            # 在网络连接方式中，点击IP/域名
            network_connection_mode_replace = str(loc.network_connection_mode).replace('replace', network_connection_mode)
            self.click_element(eval(network_connection_mode_replace))
        if network_ip:
            # 输入网络IP
            if mode == '修改':
                self.clear_input(loc.network_ip)
            self.input_text(loc.network_ip, network_ip)
        if network_port:
            # 输入网络端口
            if mode == '修改':
                self.clear_input(loc.network_port)
            self.input_text(loc.network_port, network_port)
        if domain_name:
            # 输入域名访问路径
            if mode == '修改':
                self.clear_input(loc.domainName)
            self.input_text(loc.domainName, domain_name)
        if login_username:
            # 输入登录用户名
            if mode == '修改':
                self.clear_input(loc.login_username)
            self.input_text(loc.login_username, login_username)
        if login_password:
            # 输入登录密码
            if mode == '修改':
                self.clear_input(loc.login_password)
            self.input_text(loc.login_password, login_password)
        if remark:
            # 输入备注信息，可为空
            if mode == '修改':
                self.clear_input(loc.remark)
            self.input_text(loc.remark, remark)
        HomePage(self.driver).click_submit_button()
        # 切换到默认iframe
        self.back_to_default_content()
        time.sleep(0.5)
        # 在提示框中点击确定按钮
        self.click_element(loc.confirm_button)

    # 新增监控设备
    def add_monitoring(self, room=None, monitoring_name=None, monitoring_type=None, mailing_address=None, network_connection_mode=None,
                       network_ip=None, network_port=None, domain_name=None, login_username=None, login_password=None, remark=None):
        # 进入监控设备管理界面
        HomePage(self.driver).enter_monitoring_equipment_manage()
        # 点击新增按钮
        HomePage(self.driver).click_add_button()
        # 在监控设备编辑界面进行输入
        self.edit_monitoring(room, monitoring_name, monitoring_type, mailing_address, network_connection_mode, network_ip, network_port,
                             domain_name, login_username, login_password, remark, mode=None)

    # 修改监控设备
    def modify_monitoring(self, room_location, modify_monitoring, room=None, monitoring_name=None, monitoring_type=None, mailing_address=None,
                          network_connection_mode=None, network_ip=None, network_port=None, domain_name=None, login_username=None,
                          login_password=None, remark=None):
        # 进入监控设备管理界面
        HomePage(self.driver).enter_monitoring_equipment_manage()
        # 当前页面是否存在目标元素，如果下一页按钮可点击，则点击下一页按钮，在其他页面进行查找
        modify_button_replace = str(loc.modify_button).replace('pdf_replace', room_location).replace('jksb_replace', modify_monitoring)
        HomePage(self.driver).whether_need_click_next_page_button(eval(modify_button_replace))
        # 点击修改按钮
        self.click_element(eval(modify_button_replace))
        # 在监控设备编辑界面进行输入
        self.edit_monitoring(room, monitoring_name, monitoring_type, mailing_address, network_connection_mode,
                             network_ip, network_port, domain_name, login_username, login_password, remark, mode='修改')

    # 删除监控设备
    def delete_monitoring(self, room_location, delete_monitoring):
        # 进入监控设备管理界面
        HomePage(self.driver).enter_monitoring_equipment_manage()
        # 当前页面是否存在目标元素，如果下一页按钮可点击，则点击下一页按钮，在其他页面进行查找
        delete_button_replace = str(loc.delete_button).replace('pdf_replace', room_location).replace('jksb_replace', delete_monitoring)
        HomePage(self.driver).whether_need_click_next_page_button(eval(delete_button_replace))
        # 点击删除按钮
        self.click_element(eval(delete_button_replace))
        # 切换到默认iframe
        self.back_to_default_content()
        time.sleep(0.5)
        # 在弹出的提示框中点击确定按钮
        self.click_element(loc_home.confirm_button)


if __name__ == '__main__':
    from selenium import webdriver
    from PageObjects.login_page import LoginPage
    from PageLocators.login_page_locators import LoginPageLocator as loc_1
    from Common import dir_config
    from Common.do_excel import DoExcel

    driver = webdriver.Chrome()
    driver.get('http://172.17.46.196:8080/IDRMS')
    LoginPage(driver).input_text(loc_1.username_ele, "admin")
    LoginPage(driver).input_text(loc_1.password_ele, "e2020jl")
    time.sleep(10)
    LoginPage(driver).click_element(loc_1.click_button)
    # test_datas = DoExcel('archives').get_data(dir_config.archives_data_excel_path)[0]
    # MonitoringEquipmentManagePage(driver).add_monitoring(test_datas['room_name'], test_datas['monitoring_name'], test_datas['monitoring_type'],
    #                                                      test_datas['mailing_address'], test_datas['network_connection_mode'],
    #                                                      test_datas['network_ip'], test_datas['network_port'], test_datas['domainName'],
    #                                                      test_datas['login_username'], test_datas['login_password'], test_datas['remark'])
    # MonitoringEquipmentManagePage(driver).add_monitoring(room='精伦电气配电房1', monitoring_name='新增监控设备001', mailing_address='888', remark='新增测试001')
    # MonitoringEquipmentManagePage(driver).modify_monitoring(room_location='精伦电气配电房1', modify_monitoring='新增监控设备001',
    #                                                         room='精伦电气配电房2', monitoring_name='修改监控设备001', mailing_address='999', remark='修改测试001')

    MonitoringEquipmentManagePage(driver).delete_monitoring(room_location='精伦电气配电房2', delete_monitoring='修改监控设备001')