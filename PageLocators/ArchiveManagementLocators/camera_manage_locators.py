from selenium.webdriver.common.by import By


class CameraManageLocators:
    # 展开所属配电房
    room = (By.XPATH, "//label[text()='所属配电房：']/following-sibling::div/div//b")
    room_choice = (By.XPATH, "//*[@id='select2-drop']/ul//li/div[contains(text(),'replace')]")
    # 展开所属NVR
    open_NVR = (By.XPATH, "//label[text()='所属NVR：']/following-sibling::div/div//b")
    NVR_choice = (By.XPATH, "//*[@id='select2-drop']/ul//li/div[contains(text(),'replace')]")
    # 摄像头名称
    camera_name = (By.XPATH, ".//*[@id='name']")
    # 通道号
    channel_number = (By.XPATH, "//*[@id='channelNo']")
    # 是否云台控制
    whether_control = (By.XPATH, '//span[text()="replace"]/..')
    # 保存并返回按钮
    submit_and_return = (By.XPATH, '//*[@id="btnSubmit" and @value="保存并返回"]')
    # 保存并新增按钮
    submit_and_add = (By.XPATH, './/*[@id="btnSubmit" and @value="保存并新增"]')


    input_locator = (By.XPATH, "//*[@id='select2-drop']/div/input")

