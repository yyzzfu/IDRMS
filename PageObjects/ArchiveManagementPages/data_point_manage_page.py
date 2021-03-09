from Common.basepage import BasePage
from PageObjects.home_page import HomePage
from PageLocators.ArchiveManagementLocators.data_point_manage_locators import DataPointManageLocators as loc
from PageLocators.home_page_locators import HomePageLocator as loc_home


class DataPointManagePage(BasePage):

    # 数据节点编辑
    def edit_data_point(self, room, monitoring, node_position, cabinet_or_transformer, data_type, signal_type, whether_alarm,
                        data_point_name, channel_number, data_unit, decimal_point_number, upper_limit, remark, mode):
        """
        :param room: 所属配电房中需要勾选的配电房名称
        :param monitoring: 所属监控设备中需要勾选的监控设备名称
        :param node_position: 节点位置：环境、开关柜、变压器
        :param cabinet_or_transformer: 所属位置中需要勾选的开关柜名称或变压器名称
        :param data_type: 数据分类：line_voltage线电压，phase_voltage相电压，electricity电流，cable_temperature线缆温度
                                    cabinet_temperature柜体温度，partial_discharge局放等等
        :param signal_type: 型号类型：遥测/遥信
        :param whether_alarm: 是否告警：是/否
        :param data_point_name: 数据节点名称
        :param channel_number: 通道号
        :param data_unit: 数据单位，可为空
        :param decimal_point_number: 小数位数，可为空
        :param upper_limit: 上限阀值，可为空
        :param remark: 备注信息，可为空
        :param mode: 编辑模式，新增或修改
        :return:
        """
        # 选择所属配电房
        if room:
            # 从DataPointManageLocators类中获取到的room_choice的定位元素，将其中的replace替换为函数传入的room值
            room_choice_replace = str(loc.room_choice).replace('replace', room)
            # 展开所属配电房
            self.click_element(loc.room)
            # 选择配电房
            self.click_element(eval(room_choice_replace))
        # 选择所属监控设备
        if monitoring:
            # 从DataPointManageLocators类中获取到的monitoring_equipment_choice的定位元素，将其中的replace替换为函数传入的monitoring值
            monitoring_equipment_choice_replace = str(loc.monitoring_equipment_choice).replace('replace', monitoring)
            # 展开所属监控设备
            self.click_element(loc.monitoring_equipment)
            # 选择监控设备
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
        # 选择数据分类
        if data_type:
            data_type_replace = str(loc.data_type).replace('replace', data_type)
            self.click_element(eval(data_type_replace))
        # 点击信号类型，遥信或遥测
        if signal_type:
            signal_type_replace = str(loc.signal_type).replace('replace', signal_type)
            self.click_element(eval(signal_type_replace))
        # 在“是否告警”中点击是或否
        if whether_alarm:
            whether_alarm_replace = str(loc.whether_alarm).replace('replace', whether_alarm)
            self.click_element(eval(whether_alarm_replace))
        # 输入数据节点名称
        if data_point_name:
            if mode == '修改':
                self.clear_input(loc.data_point_name)
            self.input_text(loc.data_point_name, data_point_name)
        # 输入通道号
        if channel_number:
            if mode == '修改':
                self.clear_input(loc.channel_number)
            self.input_text(loc.channel_number, channel_number)
        # 输入数据单位，可为空
        if data_unit:
            if mode == '修改':
                self.clear_input(loc.data_unit)
            self.input_text(loc.data_unit, data_unit)
        # 输入小数位数，可为空
        if decimal_point_number:
            if mode == '修改':
                self.clear_input(loc.decimal_point_number)
            self.input_text(loc.decimal_point_number, decimal_point_number)
        # 输入上限阀值，可为空
        if upper_limit:
            if mode == '修改':
                self.clear_input(loc.upper_limit)
            self.input_text(loc.upper_limit, upper_limit)
        # 输入备注信息，可为空
        if remark:
            if mode == '修改':
                self.clear_input(loc.remark)
            self.input_text(loc.remark, remark)
        # 点击保存并返回按钮
        self.click_element(loc.submit_and_return)

    # 新增数据节点
    def add_data_point(self, room=None, monitoring=None, node_position=None, cabinet_or_transformer=None, data_type=None, signal_type=None, whether_alarm=None,
                       data_point_name=None, channel_number=None, data_unit=None, decimal_point_number=None, upper_limit=None, remark=None):
        # 进入数据节点管理界面
        HomePage(self.driver).enter_data_point_manage()
        # 点击新增按钮
        HomePage(self.driver).click_add_button()
        # 在数据节点编辑界面进行输入
        self.edit_data_point(room, monitoring, node_position, cabinet_or_transformer, data_type, signal_type, whether_alarm, data_point_name,
                             channel_number, data_unit, decimal_point_number, upper_limit, remark, mode=None)

    # 修改数据节点
    def modify_data_point(self, monitoring_location, node_position_location, modify_data_point_location, room=None, monitoring=None, node_position=None,
                          cabinet_or_transformer=None, data_type=None, signal_type=None, whether_alarm=None, data_point_name=None, channel_number=None,
                          data_unit=None, decimal_point_number=None, upper_limit=None, remark=None):
        """
        :param monitoring_location: 需要修改的数据节点---对应的一体机
        :param node_position_location: 需要修改的数据节点---对应的所属位置，环境对应的是--配电房，开关柜/变压器对应的是--具体的某一个开关柜/变压器
        :param modify_data_point_location: 需要修改的数据节点---对应的数据节点名称
        :param room:
        :param monitoring:
        :param node_position:
        :param cabinet_or_transformer:
        :param data_type:
        :param signal_type:
        :param whether_alarm:
        :param data_point_name:
        :param channel_number:
        :param data_unit:
        :param decimal_point_number:
        :param upper_limit:
        :param remark:
        :return:
        """
        # 进入数据节点管理界面
        HomePage(self.driver).enter_data_point_manage()
        # 从数据节点列表中--需要修改的数据节点--对应的操作栏中，点击修改按钮
        # 如果数据节点信息比较多，有多页--而需要修改的数据节点不在当前页面，则需要翻页，在其他页面继续查找
        modify_button_replace = str(loc.modify_button).replace('monitoring', monitoring_location).replace(
            'node_position', node_position_location).replace('modify_data_point', modify_data_point_location)
        HomePage(self.driver).whether_need_click_next_page_button(eval(modify_button_replace))
        # 点击数据节点操作栏中的修改按钮
        self.click_element(eval(modify_button_replace))
        # 在数据节点编辑界面进行输入
        self.edit_data_point(room, monitoring, node_position, cabinet_or_transformer, data_type, signal_type, whether_alarm, data_point_name,
                             channel_number, data_unit, decimal_point_number, upper_limit, remark, mode='修改')

    # 删除数据节点
    def delete_data_point(self, monitoring_location, node_position_location, delete_data_point_location):
        """
        :param monitoring_location: 需要删除的数据节点---对应的一体机
        :param node_position_location: 需要删除的数据节点---对应的所属位置，环境对应的是--配电房，开关柜/变压器对应的是--具体的某一个开关柜/变压器
        :param delete_data_point_location: 需要删除的数据节点---对应的数据节点名称
        :return:
        """
        # 进入数据节点管理界面
        HomePage(self.driver).enter_data_point_manage()
        # 从数据节点列表中--需要修改的数据节点--对应的操作栏中，点击删除按钮
        # 如果数据节点信息比较多，有多页--而需要删除的数据节点不在当前页面，则需要翻页
        delete_button_replace = str(loc.delete_button).replace('monitoring', monitoring_location).replace(
            'node_position', node_position_location).replace('delete_data_point', delete_data_point_location)
        HomePage(self.driver).whether_need_click_next_page_button(eval(delete_button_replace))  # 当前页面找到了元素，则继续下一步操作，否则点击“下一页”按钮，在其他页面继续寻找
        # 点击数据节点操作栏中的删除按钮
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
    driver.get('http://172.17.46.231:8080/IDRMS')
    LoginPage(driver).input_text(loc_1.username_ele, "admin")
    LoginPage(driver).input_text(loc_1.password_ele, "e2020jl")
    time.sleep(10)
    LoginPage(driver).click_element(loc_1.click_button)
    # datas = DoExcel('data_point').get_data(dir_config.archives_data_excel_path)[0]
    # DataPointManagePage(driver).add_data_point(datas['room_name'], datas['monitoring_name'], datas['node_position'], datas['cabinet_or_transformer'], datas['data_type']
    #                                            , datas['signal_type'], datas['data_point_name'], datas['channel_number'], datas['data_unit'],
    #                                            datas['decimal_point_number'], datas['upper_limit'], datas['remark'])
    # DataPointManagePage(driver).add_data_point(room='精伦电气配电房1', monitoring='高压室一体机',
    #                                               node_position='开关柜', cabinet_or_transformer='高压室隔离柜6', data_type='电流', signal_type='遥测', data_point_name='新增测试001',
    #                                               channel_number='666', data_unit='MM', decimal_point_number='2', upper_limit='20', remark='新增测试001')
    # DataPointManagePage(driver).modify_data_point('高压室一体机', '高压室隔离柜6', '修改测试001', room='精伦电气配电房5', monitoring='配电房5一体机',
    #                       node_position='开关柜', cabinet_or_transformer='进线柜7', data_type='线缆温度', signal_type='遥测', data_point_name='修改测试002',
    #                       channel_number='999', data_unit='UUU', decimal_point_number='2', upper_limit='22', remark='再次是否成功')

    DataPointManagePage(driver).delete_data_point('配电房5一体机', '进线柜7', '修改测试002')
