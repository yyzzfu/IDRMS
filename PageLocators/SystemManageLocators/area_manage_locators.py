from selenium.webdriver.common.by import By


class AreaManageLocators:

    # 新增按钮
    add_button = (By.XPATH, "//html//a[text()='新增']")
    # 区域名称
    area_name = (By.XPATH, "//*[@id='name']")
    # 区域编码
    area_code = (By.XPATH, "//*[@id='code']")
    # 备注信息
    remark = (By.XPATH, "//*[@id='remarks']")

    # 列表中修改按钮，将replace替换为对应的区域编码即可
    modify_button = (By.XPATH, "//table[@id='dataGrid']//td[@title='replace']/..//div[@title='修改']")
    # 列表中删除按钮，将replace替换为对应的区域编码即可
    delete_button = (By.XPATH, "//table[@id='dataGrid']//td[@title='replace']/..//div[@title='删除']")
