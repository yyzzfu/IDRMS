from Common.basepage import BasePage
from PageObjects.home_page import HomePage
from PageLocators.ArchiveManagementLocators.alarm_set_locators import AlarmSetLocators as loc
from PageLocators.home_page_locators import HomePageLocator as loc_home


class AlarmSetPage(BasePage):

    # 编辑智能网关告警
    def edit_alarm_set(
            self, room, monitoring, node_position, cabinet_or_transformer, alarm_type, alarm_data, value_feedback_point, upper_limit, remark, mode):
        if room:
            room_choice_replace = str(loc.room_choice).replace('replace', room)
            # 展开所属配电房下拉框
            self.click_element(loc.room)
            # 选择配电房
            self.click_element(eval(room_choice_replace))
        if monitoring:
            monitoring_equipment_choice_replace = str(loc.monitoring_equipment_choice).replace('replace', monitoring)
            # 展开所属一体机下拉框
            self.click_element(loc.monitoring_equipment)
            # 选择一体机
            self.click_element(eval(monitoring_equipment_choice_replace))
        # 在“节点位置”中点击环境/开关柜/变压器
        if node_position:
            node_position_replace = str(loc.node_position).replace('replace', node_position)
            self.click_element(eval(node_position_replace))
        # 展开所属位置，同一个下拉框，选择开关柜或变压器时，各自的定位元素不一样
        # 所以这里需进行判断，不同的节点位置，展开所属位置下拉框，需点击的元素也不一样
        # 在所属位置中选择开关柜/变压器
        if cabinet_or_transformer:
            if node_position == '开关柜':
                self.click_element(loc.position_belong_cabinet)  # 展开所属位置下拉框
            elif node_position == '变压器':
                self.click_element(loc.position_belong_transformer)  # 展开所属位置下拉框
            # 从DataPointManageLocators类中获取到cabinet_or_transformer_choice的定位元素，将其中的replace替换为函数传入的cabinet_or_transformer值
            cabinet_or_transformer_choice_replace = str(loc.cabinet_or_transformer_choice).replace('replace', cabinet_or_transformer)
            self.click_element(eval(cabinet_or_transformer_choice_replace))
        # 选择告警类型
        if alarm_type:
            alarm_type_replace = str(loc.alarm_type).replace('replace', alarm_type)
            self.click_element(eval(alarm_type_replace))
        if alarm_type == '烟感' or alarm_type == '水浸':
            if alarm_data:
                # 展开告警测量点
                self.click_element(loc.open_alarm_data_select)
                # 选择告警测量点
                self.input_text(loc.alarm_input, alarm_data)
                self.enter_button(loc.alarm_input)
        else:
            if alarm_data:
                # alarm_data_choice_replace = str(loc.alarm_data).replace('replace', alarm_data)
                # 展开告警测量点
                self.click_element(loc.open_alarm_data_select)
                # 选择告警测量点
                # self.click_element(eval(alarm_data_choice_replace))
                self.input_text(loc.alarm_input, alarm_data)
                self.enter_button(loc.alarm_input)
            if value_feedback_point:
                # value_feedback_point_replace = str(loc.value_feedback_point).replace('replace', value_feedback_point)
                # 展开值反馈测量点下拉框
                self.click_element(loc.open_value_feedback_point_select)
                # 选择值反馈测量点
                # self.click_element(eval(value_feedback_point_replace))
                self.input_text(loc.alarm_input, value_feedback_point)
                self.enter_button(loc.alarm_input)
            # 输入上限阀值，可为空
            if upper_limit:
                if mode == '修改':
                    self.clear_input(loc.upper_limit)
                self.input_text(loc.upper_limit, upper_limit)
        if remark:
            if mode == '修改':
                self.clear_input(loc.remark)
            # 输入备注
            self.input_text(loc.remark, remark)
        # 点击保存并返回按钮
        self.click_element(loc.submit_and_return)

    # 新增智能网关告警设置
    def add_alarm_set(self, room=None, monitoring=None, node_position=None, cabinet_or_transformer=None, alarm_type=None, alarm_data=None,
                      value_feedback_point=None, upper_limit=None, remark=None, mode=None):
        # 进入控制节点管理界面
        HomePage(self.driver).enter_alarm_set()
        # 点击新增按钮
        HomePage(self.driver).click_add_button()
        # 在控制节点编辑界面进行输入
        self.edit_alarm_set(room, monitoring, node_position, cabinet_or_transformer, alarm_type, alarm_data, value_feedback_point, upper_limit, remark, mode=None)

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
    driver.get('http://172.17.46.200:8080/IDRMS')
    LoginPage(driver).input_text(loc_1.username_ele, "admin")
    LoginPage(driver).input_text(loc_1.password_ele, "e2020jl")
    time.sleep(10)
    LoginPage(driver).click_element(loc_1.click_button)
    # datas = DoExcel('data_point').get_data(dir_config.archives_data_excel_path)[0]
    AlarmSetPage(driver).add_alarm_set(room="精伦电气配电房1", monitoring="一体机", node_position="环境", alarm_type="环境温度",
                                       alarm_data="测试1告警", value_feedback_point="测试1")
    # AlarmSetPage(driver).add_alarm_set(room="精伦电气配电房1", monitoring="一体机", node_position="环境", alarm_type="烟感",
    #     #                                    alarm_data="烟感测试")