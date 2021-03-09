from selenium.webdriver.common.by import By


class ControlPointManageLocators:

    # 展开所属配电房
    room_select = (By.XPATH, "//label[text()='所属配电房：']/following-sibling::div/div//b")
    # 使用反射，将replace替换为需要勾选的配电房名称
    room_choice = (By.XPATH, "//*[@id='select2-drop']/ul//li/div[contains(text(),'replace')]")
    # 展开所属监控设备
    monitoring_equipment_select = (By.XPATH, "//label[text()='所属智能网关：']/following-sibling::div/div//b")
    # 使用反射，将replace替换为需要勾选的监控设备名称
    monitoring_equipment_choice = (By.XPATH, "//*[@id='select2-drop']/ul//li/div[contains(text(),'replace')]")
    # 数据分类
    data_type_choice = (By.XPATH, '//label[text()="数据类型："]/following-sibling::div//span[text()="replace"]/..')
    # 展开状态反馈节点
    status_feedback_point_select = (By.XPATH, "//label[text()='状态反馈测量点：']/following-sibling::div/div//b")
    status_feedback_point_choice = (By.XPATH, "//*[@id='select2-drop']/ul//li/div[contains(text(),'replace')]")
    # 控制节点名称
    control_point_name = (By.XPATH, "//*[@id='name']")
    # 通道号
    channel_number = (By.XPATH, "//*[@id='channelNo']")
    # 是否远程控制
    whether_control = (By.XPATH, '//label[text()="是否可远程控制："]/following-sibling::div//span[text()="replace"]/..')
    # 备注
    remark = (By.XPATH, "//*[@id='remarks']")
    # 保存并返回按钮
    submit_and_return = (By.XPATH, '//*[@id="btnSubmit" and @value="保存并返回"]')

    # 列表中修改按钮，将pdf_replace替换为对应的配电房名称，ytj_replace替换为一体机名称，jdmc_replace替换为数据节点名称
    modify_button = (By.XPATH, "//table[@id='dataGrid']//td[@title='pdf_replace']/..//td[@title='ytj_replace']/..//td[@title='jdmc_replace']/..//div[@title='修改']")
    # 列表中修改按钮，将pdf_replace替换为对应的配电房名称，ytj_replace替换为一体机名称，jdmc_replace替换为数据节点名称
    delete_button = (By.XPATH, "//table[@id='dataGrid']//td[@title='pdf_replace']/..//td[@title='ytj_replace']/..//td[@title='jdmc_replace']/..//div[@title='删除']")
