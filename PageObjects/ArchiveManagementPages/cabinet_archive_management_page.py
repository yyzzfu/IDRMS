from Common.basepage import BasePage
from PageObjects.home_page import HomePage
from PageLocators.ArchiveManagementLocators.cabinet_archive_management_locators import CabinetArchiveMmanagementLocators as loc
from PageLocators.home_page_locators import HomePageLocator as loc_home


class CabinetArchiveMmanagementPage(BasePage):

    # 编辑开关柜信息
    def edit_cabinet(self, room, cabinet_name, cabinet_type, remark, mode):
        if room:
            room_choice_replace = str(loc.room_choice).replace('replace', room)
            # 点击所属配电房输入框，展开所属配电房下拉框
            self.click_element(loc.room_select)
            # 选择配电房
            self.click_element(eval(room_choice_replace))
        if cabinet_name:
            if mode == "修改":
                self.clear_input(loc.cabinet_name)
            # 输入开关柜名称
            self.clear_input(loc.cabinet_name)
            self.input_text(loc.cabinet_name, cabinet_name)
        # 选择开关类型,cabinet_type为进线柜时，便点击进线柜。cabinet_type为计量柜时，便点击计量柜。
        if cabinet_type:
            cabinet_type_replace = str(loc.cabinet_type).replace('replace', cabinet_type)
            self.click_element(eval(cabinet_type_replace))
        # 输入备注信息,可为空
        if remark:
            if mode == "修改":
                self.clear_input(loc.remark)
            self.input_text(loc.remark, remark)
        # 点击保存按钮
        HomePage(self.driver).click_submit_button()

    # 新建开关柜
    def add_cabinet(self, room=None, cabinet_name=None, cabinet_type=None, remark=None):
        # 进入开关柜档案管理界面
        HomePage(self.driver).enter_cabinet_archive_management()
        # 点击新增按钮
        HomePage(self.driver).click_add_button()
        self.edit_cabinet(room, cabinet_name, cabinet_type, remark, mode=None)

    # 修改开关柜
    def modify_cabinet(self, room_location, cabinet_location, room=None, cabinet_name=None, cabinet_type=None, remark=None):
        """
        :param room_location: 需要修改的开关柜--对应的配电房名称
        :param cabinet_location: 需要修改的开关柜--对应的开关柜名称
        :param room: 输入修改内容
        :param cabinet_name: 输入修改内容
        :param cabinet_type: 输入修改内容
        :param remark: 输入修改内容
        :return:
        """
        # 进入开关柜档案管理界面
        HomePage(self.driver).enter_cabinet_archive_management()
        modify_button_replace = str(loc.modify_button).replace('pdf_replace', room_location).replace('kgg_replace', cabinet_location)
        # 开关柜列表中--需要修改的开关柜--操作栏中，点击修改按钮
        # 如果当前页面中，没找到目标开关柜，而“下一页”按钮可点击，则点击下一页按钮，在其他的页面继续寻找
        HomePage(self.driver).whether_need_click_next_page_button(eval(modify_button_replace))
        # 点击修改按钮
        self.click_element(eval(modify_button_replace))
        # 在开关柜编辑界面，进行修改
        self.edit_cabinet(room, cabinet_name, cabinet_type, remark, mode='修改')

    # 删除开关柜
    def delete_cabinet(self, room_location, cabinet_location):
        """
        :param room_location: 需要删除的开关柜--对应的配电房名称
        :param cabinet_location: 需要删除的开关柜--对应的开关柜名称
        :return:
        """
        # 进入开关柜档案管理界面
        HomePage(self.driver).enter_cabinet_archive_management()
        delete_button_replace = str(loc.delete_button).replace('pdf_replace', room_location).replace('kgg_replace', cabinet_location)
        # 开关柜列表中--需要修改的开关柜--操作栏中，点击删除按钮
        # 如果当前页面中，没找到目标开关柜，而“下一页”按钮可点击，则点击下一页按钮，在其他的页面继续寻找
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
    driver.get('http://172.17.46.231:8080/IDRMS')
    LoginPage(driver).input_text(loc_1.username_ele, "admin")
    LoginPage(driver).input_text(loc_1.password_ele, "e2020jl")
    time.sleep(10)
    LoginPage(driver).click_element(loc_1.click_button)
    # test_datas = DoExcel('archives').get_data(dir_config.archives_data_excel_path)[0]
    # CabinetArchiveMmanagementPage(driver).add_cabinet(test_datas['room_name'],
    #                                                   test_datas['cabinet_name'],
    #                                                   test_datas['cabinet_type'],
    #                                                   test_datas['remark'])
    # CabinetArchiveMmanagementPage(driver).add_cabinet('精伦电气配电房6', '新增测试001', '出线柜', '备注001')
    CabinetArchiveMmanagementPage(driver).add_cabinet('', '123', '', '')
    # CabinetArchiveMmanagementPage(driver).modify_cabinet('精伦电气配电房6', '新增测试001', '精伦电气配电房5', '修改测试001', '计量柜', '修改备注001')
    # CabinetArchiveMmanagementPage(driver).delete_cabinet('精伦电气配电房5', '修改测试001')
