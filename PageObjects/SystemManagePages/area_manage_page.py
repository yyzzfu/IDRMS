from Common.basepage import BasePage
from PageObjects.home_page import HomePage
from PageLocators.SystemManageLocators.area_manage_locators import AreaManageLocators as loc
from PageLocators.home_page_locators import HomePageLocator as loc_home


class AreaManagePage(BasePage):

    # 编辑区域
    def edit_area(self, area_name, area_code, remark, mode):
        if area_name:
            # 输入区域名称
            if mode == '修改':
                self.clear_input(loc.area_name)
            self.input_text(loc.area_name, area_name)
        if area_code:
            # 输入区域编码
            if mode == '修改':
                self.clear_input(loc.area_code)
            self.input_text(loc.area_code, area_code)
        if remark:
            # 输入备注信息
            if mode == '修改':
                self.clear_input(loc.remark)
            self.input_text(loc.remark, remark)
        # 点击保存
        HomePage(self.driver).click_submit_button()

    # 新增区域
    def add_area(self, area_name=None, area_code=None, remark=None):
        # 进入区域管理节点
        HomePage(self.driver).enter_area_manage()
        # 点击新增按钮
        self.click_element(loc.add_button)
        # 在区域编辑界面进行输入
        self.edit_area(area_name, area_code, remark, mode=None)

    # 修改区域
    def modify_area(self, area_code_location, area_name=None, area_code=None, remark=None):
        # 进入区域管理节点
        HomePage(self.driver).enter_area_manage()
        modify_button_replace = str(loc.modify_button).replace('replace', area_code_location)
        HomePage(self.driver).whether_need_click_next_page_button(eval(modify_button_replace))
        # 点击修改按钮
        self.click_element(eval(modify_button_replace))
        # 在区域编辑界面进行输入
        self.edit_area(area_name, area_code, remark, mode='修改')

    # 删除区域
    def delete_area(self, area_code_location):
        # 进入区域管理节点
        HomePage(self.driver).enter_area_manage()
        delete_button_replace = str(loc.delete_button).replace('replace', area_code_location)
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
    import time

    driver = webdriver.Chrome()
    driver.get('http://172.17.46.198:9080/IDRMS')
    LoginPage(driver).input_text(loc_1.username_ele, "idrmstest")
    LoginPage(driver).input_text(loc_1.password_ele, "fu123456")
    time.sleep(10)
    LoginPage(driver).click_element(loc_1.click_button)
    test_datas = DoExcel('area').get_data(dir_config.archives_data_excel_path)[0]
    AreaManagePage(driver).add_area(test_datas['area_name'], test_datas['area_code'], test_datas['remark'])
