from selenium.webdriver.common.by import By


class CabinetArchiveMmanagementLocators:

    # 展开所属配电房
    room_select = (By.XPATH, "//label[text()='所属配电房：']/following-sibling::div/div//b")
    # 根据配电房名称来定位需要选择的配电房-----后续优化，将配电房名称参数化
    room_choice = (By.XPATH, "//*[@id='select2-drop']/ul//li/div[contains(text(),'replace')]")
    # 开关柜名称
    cabinet_name = (By.XPATH, "//*[@id='name']")
    # 开关柜类型，将replace替换为需要点击的开关柜类型名称
    cabinet_type = (By.XPATH, '//label[text()="开关柜类型："]/following-sibling::div//span[contains(text(),"replace") ]/..')
    # 备注信息
    remark = (By.XPATH, "//*[@id='remarks']")

    # 列表中修改按钮，将pdf_replace替换为对应的配电房名称，kgg_replace替换为开关柜名称
    modify_button = (By.XPATH, "//table[@id='dataGrid']//td[@title='pdf_replace']/..//td[@title='kgg_replace']/..//div[@title='修改']")
    # 列表中删除按钮，将pdf_replace替换为对应的配电房名称，kgg_replace替换为开关柜名称
    delete_button = (By.XPATH, "//table[@id='dataGrid']//td[@title='pdf_replace']/..//td[@title='kgg_replace']/..//div[@title='删除']")

