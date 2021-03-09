from selenium.webdriver.common.by import By


class LoginPageLocator:

    username_ele = (By.ID, 'username')
    password_ele = (By.ID, 'password')
    code_ele = (By.XPATH, "//input[@id='validateCode']")
    click_button = (By.ID, 'loginBtn')
    code_img = (By.XPATH, "//*[@id='loginForm']/div[1]/img")
    chang_code_img = (By.XPATH, '//*[@id="loginForm"]/div[1]//a[text()="看不清"]')