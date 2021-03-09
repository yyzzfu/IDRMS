from selenium.webdriver.common.by import By


class UserManageLocators:

    # 姓名
    name = (By.XPATH, ".//*[@id='name']")
    # 登录名
    user_name = (By.XPATH, ".//*[@id='user_name']")
    # 密码
    password = (By.XPATH, ".//*[@id='newPassword']")
    # 确认密码
    confirm_password = (By.XPATH, ".//*[@id='confirmNewPassword']")
    # 邮箱
    email = (By.XPATH, ".//*[@id='email']")
    # 手机
    phone = (By.XPATH, ".//*[@id='phone']")
    # 用户角色
    role = (By.XPATH, "//span[text()='replace']/..")
    # 系统管理员
    role_manage = (By.XPATH, "//span[text()='系统管理员']/..")
    # 管辖配电房
    manage_room = (By.XPATH, "//*[@id='areaTree']//span[text()='replace']")
    # 备注信息
    remark = (By.XPATH, "//*[@id='remarks']")

    # 列表中修改按钮，将replace替换为对应的登录名即可
    modify_button = (By.XPATH, "//table[@id='dataGrid']//td[@title='replace']/..//div[@title='修改']")
    # 列表中删除按钮，将replace替换为对应的登录名即可
    delete_button = (By.XPATH, "//table[@id='dataGrid']//td[@title='replace']/..//div[@title='删除']")
