from Common.basepage import BasePage
from PageObjects.home_page import HomePage
from PageLocators.ArchiveManagementLocators.transformer_archive_management_locators import TransformerArchiveManageLocators as loc
from PageLocators.home_page_locators import HomePageLocator as loc_home


class TransformerArchiveManagePage(BasePage):

    # 编辑变压器
    def edit_transformer(self, room, transformer_name, voltage_level_high, voltage_level_low, capacity, remark, mode):
        if room:
            # 展开所属配电房下拉框
            self.click_element(loc.room_select)
            room_choice_replace = str(loc.room_choice).replace('replace', room)
            self.click_element(eval(room_choice_replace))
        if transformer_name:
            # 输入变压器名称
            self.clear_input(loc.transformer_name)
            self.input_text(loc.transformer_name, transformer_name)
        if voltage_level_high:
            # 输入额定电压高压侧
            self.clear_input(loc.voltage_level_high)
            self.input_text(loc.voltage_level_high, voltage_level_high)
        if voltage_level_low:
            # 输入额定电压低压侧
            self.clear_input(loc.voltage_level_low)
            self.input_text(loc.voltage_level_low, voltage_level_low)
        if capacity:
            # 输入装机容量
            self.clear_input(loc.capacity)
            self.input_text(loc.capacity, capacity)
        if remark:
            # 输入备注信息,可为空
            if mode == '修改':
                self.clear_input(loc.remark)
            self.input_text(loc.remark, remark)
        # 点击保存按钮
        HomePage(self.driver).click_submit_button()

    # 新增变压器
    def add_transformer(self, room=None, transformer_name=None, voltage_level_high=None, voltage_level_low=None, capacity=None, remark=None):
        # 进入变压器档案管理界面
        HomePage(self.driver).enter_transformer_archive_management()
        # 点击新增按钮
        HomePage(self.driver).click_add_button()
        # 在变压器编辑界面进行输入
        self.edit_transformer(room, transformer_name, voltage_level_high, voltage_level_low, capacity, remark, mode=None)

    # 修改变压器
    def modify_transformer(self, room_location, transformer_location, room=None, transformer_name=None, voltage_level_high=None,
                           voltage_level_low=None, capacity=None, remark=None):
        # 进入变压器档案管理界面
        HomePage(self.driver).enter_transformer_archive_management()
        modify_button_replace = str(loc.modify_button).replace('pdf_replace', room_location).replace('byq_replace', transformer_location)
        HomePage(self.driver).whether_need_click_next_page_button(eval(modify_button_replace))
        # 点击修改按钮
        self.click_element(eval(modify_button_replace))
        self.edit_transformer(room, transformer_name, voltage_level_high, voltage_level_low, capacity, remark, mode='修改')

    # 删除变压器
    def delete_transformer(self, room_location, transformer_location):
        # 进入变压器档案管理界面
        HomePage(self.driver).enter_transformer_archive_management()
        delete_button_replace = str(loc.delete_button).replace('pdf_replace', room_location).replace('byq_replace', transformer_location)
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
    import time
    from PageLocators.login_page_locators import LoginPageLocator as loc_1
    from Common import dir_config
    from Common.do_excel import DoExcel

    driver = webdriver.Chrome()
    driver.get('http://172.17.46.198:9080/IDRMS')
    LoginPage(driver).input_text(loc_1.username_ele, "idrmstest")
    LoginPage(driver).input_text(loc_1.password_ele, "fu123456")
    time.sleep(10)
    LoginPage(driver).click_element(loc_1.click_button)
    test_datas = DoExcel('archives').get_data(dir_config.archives_data_excel_path)
    TransformerArchiveManagePage(driver).add_transformer(test_datas[0]['room_name'],
                                                         test_datas[0]['transformer_name'],
                                                         test_datas[0]['voltage_level'],
                                                         test_datas[0]['capacity'],
                                                         test_datas[0]['transformer_type'],
                                                         test_datas[0]['remark'])
