from selenium.webdriver.common.by import By


class AlarmSetLocators:

    # 展开所属配电房
    room = (By.XPATH, "//label[text()='所属配电房：']/following-sibling::div/div//b")
    # 使用反射，将replace替换为需要勾选的配电房名称
    room_choice = (By.XPATH, "//*[@id='select2-drop']/ul//li/div[contains(text(),'replace')]")

    # 展开所属监控设备
    monitoring_equipment = (By.XPATH, "//label[text()='所属智能网关：']/following-sibling::div/div//b")
    # 使用反射，将replace替换为需要勾选的监控设备名称
    monitoring_equipment_choice = (By.XPATH, "//*[@id='select2-drop']/ul//li/div[contains(text(),'replace')]")

    # 节点位置
    node_position = (By.XPATH, '//label[text()="测量点位置："]/following-sibling::div//span[text()="replace"]/..')

    # 展开所属位置
    # position_belong = (By.XPATH, "//label[text()='所属位置：']/following-sibling::div/div//b")
    position_belong_transformer = (By.XPATH, "//label[text()='所属位置：']/following-sibling::div/div[1]/a//b")
    position_belong_cabinet = (By.XPATH, "//label[text()='所属位置：']/following-sibling::div/div[2]/a//b")
    # 使用反射，将replace替换为需要勾选的开关柜或变压器的名称
    cabinet_or_transformer_choice = (By.XPATH, "//*[@id='select2-drop']/ul//li/div[contains(text(),'replace')]")

    # 告警类型
    alarm_type = (By.XPATH, '//label[text()="告警类型："]/following-sibling::div//span[text()="replace"]/..')

    # 展开告警测量点下拉框
    open_alarm_data_select = (By.XPATH, "//label[text()='告警测量点：']/following-sibling::div/div//b")
    # 告警测量点输入框
    # alarm_data_input = (By.XPATH, '//label[text()="告警测量点："]/following-sibling::div//input')
    # alarm_data_input = (By.XPATH, '//label[text()="告警测量点："]/../div//input')
    alarm_input = (By.XPATH, "//*[@id='select2-drop']/div/input")
    # # 下拉框
    # select_locator = (By.XPATH, "//label[text()='告警测量点：']/following-sibling::div/select")
    # 告警测量点
    alarm_data = (By.XPATH, '//label[text()="告警测量点："]/following-sibling::div//span[text()="replace"]/..')
    # 展开值反馈测量点下拉框
    open_value_feedback_point_select = (By.XPATH, "//label[text()='值反馈测量点：']/following-sibling::div/div//b")
    # 值反馈测量点输入框
    value_feedback_point_input = (By.XPATH, '//label[text()="值反馈测量点："]/following-sibling::div//input')
    # 值反馈测量点
    value_feedback_point = (By.XPATH, '//label[text()="值反馈测量点："]/following-sibling::div//span[text()="replace"]/..')

    # 上限阀值
    upper_limit = (By.XPATH,"//*[@id='alarm.ycAlarm.upperLimit']")
    # 备注信息
    remark = (By.XPATH, "//*[@id='remarks']")

    # 保存并返回按钮
    submit_and_return = (By.XPATH, '//*[@id="btnSubmit" and @value="保存并返回"]')
    # 保存并新增按钮
    submit_and_add = (By.XPATH, './/*[@id="btnSubmit" and @value="保存并新增"]')

    # 列表中修改按钮，将monitoring替换为对应的一体机名称，node_position替换为所属位置，modify_data_point替换为数据节点名称
    modify_button = (By.XPATH, "//table[@id='dataGrid']//td[@title='monitoring']/..//td[@title='node_position']/..//td[@title='modify_data_point']/..//div[@title='修改']")
    # 列表中修改按钮，将monitoring替换为对应的一体机名称，node_position替换为所属位置，modify_data_point替换为数据节点名称
    delete_button = (By.XPATH, "//table[@id='dataGrid']//td[@title='monitoring']/..//td[@title='node_position']/..//td[@title='delete_data_point']/..//div[@title='删除']")
