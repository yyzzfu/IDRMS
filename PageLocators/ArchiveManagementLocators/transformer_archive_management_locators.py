from selenium.webdriver.common.by import By


class TransformerArchiveManageLocators:

    # 展开所属配电房
    room_select = (By.XPATH, "//label[text()='所属配电房：']/following-sibling::div/div//b")
    # 根据配电房名称来定位需要选择的配电房-----后续优化，将配电房名称参数化
    # room_choice = (By.XPATH, "//*[@id='select2-drop']/ul//li/div[contains(text(),'配电房')]")
    room_choice = (By.XPATH, "//*[@id='select2-drop']/ul//li/div[contains(text(),'replace')]")
    # 变压器名称
    transformer_name = (By.XPATH, "//*[@id='name']")
    # 额定电压高压侧
    voltage_level_high = (By.XPATH, "//*[@id='voltageLevelHigh']")
    # 额定电压低压侧
    voltage_level_low = (By.XPATH, "//*[@id='voltageLevelLow']")
    # 装机容量
    capacity = (By.XPATH, "//*[@id='installCapacity']")
    # 备注
    remark = (By.XPATH, "//*[@id='remarks']")

    # 列表中修改按钮，将pdf_replace替换为对应的配电房名称名称，byq_replace替换为对应的变压器名称
    modify_button = (By.XPATH, "//table[@id='dataGrid']//td[@title='pdf_replace']/..//td[@title='byq_replace']/..//div[@title='修改']")
    # 列表中删除按钮，将pdf_replace替换为对应的配电房名称名称，byq_replace替换为对应的变压器名称
    delete_button = (By.XPATH, "//table[@id='dataGrid']//td[@title='pdf_replace']/..//td[@title='kgg_replace']/..//div[@title='删除']")
