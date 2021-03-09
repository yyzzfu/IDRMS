from selenium.webdriver.common.by import By


class MonitoringEquipmentManageLocators:

    # 展开所属配电房
    room_select = (By.XPATH, "//label[text()='所属配电房：']/following-sibling::div/div//b")
    # 根据配电房名称来定位需要选择的配电房-----后续优化，将配电房名称参数化
    room_choice = (By.XPATH, "//*[@id='select2-drop']/ul//li/div[contains(text(),'replace')]")
    # 监控设备名称
    monitoring_name = (By.XPATH, "//*[@id='name']")
    # 监控设备类型
    monitoring_type = (By.XPATH, '//label[text()="监控设备类型："]/following-sibling::div//span[text()="replace"]/..')
    # -----------------------------------NVR-IP-----------------------------------------------------------------
    # 网络连接方式
    network_connection_mode = (By.XPATH, '//label[text()="网络连接方式："]/following-sibling::div//span[text()="replace"]/..')
    # 网络ip
    network_ip = (By.XPATH, "//*[@id='ip']")
    # 网络端口
    network_port = (By.XPATH, "//*[@id='port']")
    # 登录用户名
    login_username = (By.XPATH, "//*[@id='loginUsername']")
    # 登录密码
    login_password = (By.XPATH, "//*[@id='loginPassword']")

    # -----------------------------------NVR-域名-----------------------------------------------------------------
    # 域名访问路径
    domainName = (By.XPATH, "//*[@id='domainName']")

    # 通信地址
    mailing_address = (By.XPATH, "//*[@id='deviceAddress']")
    # 备注信息
    remark = (By.XPATH, "//*[@id='remarks']")
    # 确定提示框中的确定按钮
    confirm_button = (By.XPATH, '//*[@id="jbox-states"]/descendant::div//button [text()="确定"]')
    # 确定提示框中的取消按钮
    cancel_button = (By.XPATH, '//*[@id="jbox-states"]/descendant::div//button [text()="取消"]')

    # 列表中修改按钮，将pdf_replace替换为对应的配电房名称，jksb_replace替换为监控设备名称
    modify_button = (By.XPATH, "//table[@id='dataGrid']//td[@title='pdf_replace']/..//td[@title='jksb_replace']/..//div[@title='修改']")
    # 列表中删除按钮，将pdf_replace替换为对应的配电房名称，kgg_replace替换为监控设备名称
    delete_button = (By.XPATH, "//table[@id='dataGrid']//td[@title='pdf_replace']/..//td[@title='jksb_replace']/..//div[@title='删除']")
