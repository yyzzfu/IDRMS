from selenium.webdriver.common.by import By


class DataPointManageLocators:

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
    position_belong_transformer = (By.XPATH, "//label[text()='测量点所属：']/following-sibling::div/div[1]/a//b")
    position_belong_cabinet = (By.XPATH, "//label[text()='测量点所属：']/following-sibling::div/div[2]/a//b")
    # 使用反射，将replace替换为需要勾选的开关柜或变压器的名称
    cabinet_or_transformer_choice = (By.XPATH, "//*[@id='select2-drop']/ul//li/div[contains(text(),'replace')]")

    # 数据分类
    data_type = (By.XPATH, '//label[text()="数据类型："]/following-sibling::div//span[text()="replace"]/..')
    # 信号类型
    signal_type = (By.XPATH, '//label[text()="信号类型："]/following-sibling::div//span[text()="replace"]/..')
    # 是否告警
    whether_alarm = (By.XPATH, '//span[text()="replace"]/..')
    # 数据节点名称
    data_point_name = (By.XPATH, "//*[@id='name']")
    # 通道号
    channel_number = (By.XPATH, "//*[@id='channelNo']")
    # 数据单位
    data_unit = (By.XPATH, "//*[@id='dataUnit']")
    # 小数位数
    decimal_point_number = (By.XPATH, "//*[@id='decimalPointNum']")
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



if __name__ == '__main__':
    a = DataPointManageLocators().room_choice
    print(a)
    print(type(a))
    b = str(a)
    c = b.replace('replace', '配电房A')
    print(type(b))
    print(c)
    print(type(c))
    print(eval(c))
    print(type(eval(c)))