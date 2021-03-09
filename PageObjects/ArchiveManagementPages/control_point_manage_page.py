from Common.basepage import BasePage
from PageObjects.home_page import HomePage
from PageLocators.ArchiveManagementLocators.control_point_manage_locators import ControlPointManageLocators as loc
from PageLocators.home_page_locators import HomePageLocator as loc_home


class ControlPointManagePage(BasePage):

    # 编辑控制节点
    def edit_control_point(
            self, room, monitoring, data_type, status_feedback_point, control_point_name, channel_number, whether_control, remark, mode):
        if room:
            room_choice_replace = str(loc.room_choice).replace('replace', room)
            # 展开所属配电房下拉框
            self.click_element(loc.room_select)
            # 选择配电房
            self.click_element(eval(room_choice_replace))
        if monitoring:
            monitoring_equipment_choice_replace = str(loc.monitoring_equipment_choice).replace('replace', monitoring)
            # 展开所属一体机下拉框
            self.click_element(loc.monitoring_equipment_select)
            # 选择一体机
            self.click_element(eval(monitoring_equipment_choice_replace))
        if data_type:
            data_type_choice_replace = str(loc.data_type_choice).replace('replace', data_type)
            # 选择数据分类
            self.click_element(eval(data_type_choice_replace))
        if status_feedback_point:
            status_feedback_point_choice_replace = str(loc.status_feedback_point_choice).replace('replace', status_feedback_point)
            # 展开状态反馈节点
            self.click_element(loc.status_feedback_point_select)
            # 选择状态反馈节点
            self.click_element(eval(status_feedback_point_choice_replace))
        if control_point_name:
            # if mode == '修改':
            self.clear_input(loc.control_point_name)
            # 输入控制节点名称
            self.input_text(loc.control_point_name, control_point_name)
        if channel_number:
            if mode == '修改':
                self.clear_input(loc.channel_number)
            # 输入通道号
            self.input_text(loc.channel_number, channel_number)
        if whether_control:
            # 是否可远程控制中，点击是或否
            whether_control_replace = str(loc.whether_control).replace('replace', whether_control)
            self.click_element(eval(whether_control_replace))
        if remark:
            if mode == '修改':
                self.clear_input(loc.channel_number)
            # 输入备注
            self.input_text(loc.remark, remark)
        # 点击保存并返回按钮
        self.click_element(loc.submit_and_return)

    # 新增控制节点
    def add_control_point(self, room=None, monitoring=None, data_type=None, status_feedback_point=None, control_point_name=None,
                          channel_number=None, whether_control=None, remark=None):
        # 进入控制节点管理界面
        HomePage(self.driver).enter_control_point_manage()
        # 点击新增按钮
        HomePage(self.driver).click_add_button()
        # 在控制节点编辑界面进行输入
        self.edit_control_point(room, monitoring, data_type, status_feedback_point,
                                control_point_name, channel_number, whether_control, remark, mode=None)

    # 修改控制节点
    def modify_control_point(self, room_location, monitoring_location, modify_control_point, room=None, monitoring=None, data_type=None,
                             status_feedback_point=None, control_point_name=None, channel_number=None, whether_control=None, remark=None):
        # 进入控制节点管理界面
        HomePage(self.driver).enter_control_point_manage()
        modify_button_replace = str(loc.modify_button).replace('pdf_replace', room_location).replace(
            'ytj_replace', monitoring_location).replace('jdmc_replace', modify_control_point)
        # 当前页面是否能找到元素，如果存在多页，则去其他页面查找元素是否存在
        HomePage(self.driver).whether_need_click_next_page_button(eval(modify_button_replace))
        # 点击修改按钮
        self.click_element(eval(modify_button_replace))
        # 在控制节点编辑界面进行输入
        self.edit_control_point(room, monitoring, data_type, status_feedback_point,
                                control_point_name, channel_number, whether_control, remark, mode='修改')

    # 删除控制节点
    def delete_control_point(self, room_location, monitoring_location, delete_control_point):
        # 进入控制节点管理界面
        HomePage(self.driver).enter_control_point_manage()
        delete_button_replace = str(loc.delete_button).replace('pdf_replace', room_location).replace(
            'ytj_replace', monitoring_location).replace('jdmc_replace', delete_control_point)
        # 当前页面是否能找到元素，如果存在多页，则去其他页面查找元素是否存在
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
    driver.get('http://172.17.46.196:8080/IDRMS')
    LoginPage(driver).input_text(loc_1.username_ele, "admin")
    LoginPage(driver).input_text(loc_1.password_ele, "e2020jl")
    time.sleep(10)
    LoginPage(driver).click_element(loc_1.click_button)
    # datas = DoExcel('data_point').get_data(dir_config.archives_data_excel_path)[0]
    ControlPointManagePage(driver).add_control_point("精伦电气配电房1", "一体机1", "水泵", "水泵1", "水泵控制", 1)