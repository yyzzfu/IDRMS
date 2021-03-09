from selenium import webdriver
import re
from PageLocators.login_page_locators import LoginPageLocator as loc
from Common.basepage import BasePage
from aip import AipOcr
from PIL import Image
from Common import dir_config
import time
from TestDatas import login_datas as LD


""" 你的 APPID AK SK """
config = {
    "appId": '20367335',
    "apiKey": 'wfXUvEBDyQT87der31X0i6L6',
    "secretKey": 'WeCD7QoGG4oIRrZrWFAv1Gaig05KqbM4'
}

client = AipOcr(**config)


class LoginPage(BasePage):

    def login(self, username, password, code):
        doc = '登录页面_登录操作'
        if username:
            self.input_text(loc.username_ele, username, doc=doc)
        if password:
            self.input_text(loc.password_ele, password, doc=doc)
        if code:
            self.input_text(loc.code_ele, code, doc=doc)
        # time.sleep(10)
        self.click_element(loc.click_button, doc=doc)

    def clear_username_input(self):
        doc = '登录页面'
        self.clear_input(loc.username_ele, doc=doc)

    def clear_password_input(self):
        doc = '登录页面'
        self.clear_input(loc.password_ele, doc=doc)

    def clear_code_input(self):
        doc = '登录页面'
        self.clear_input(loc.code_ele, doc=doc)

    def chang_code_img(self):
        doc = '登录页面'
        self.click_element(loc.chang_code_img, doc=doc)

    def code_image_to_text(self, file_name=None):
        if not file_name:
            file_name = dir_config.code_picture_dir + "/code.png"
        self.driver.save_screenshot(file_name)
        code_element = self.get_element(loc.code_img)
        left = code_element.location['x']
        top = code_element.location['y']
        right = code_element.size['width'] + left
        height = code_element.size['height'] + top
        im = Image.open(file_name)
        img = im.crop((left, top, right, height))
        img.save(file_name)
        img = Image.open(file_name)
        # 模式"L"为灰色图像
        img = img.convert('L')
        img.save(file_name)
        text = self.get_image_str(file_name)
        code_text = (re.findall(r'[a-zA-Z0-9]', text))
        if not code_text:
            text = ''.join(code_text)
            if len(text) == 4:
                return text
            else:
                self.chang_code_img()
                time.sleep(1)
                return self.code_image_to_text(file_name)
        else:
            self.chang_code_img()
            time.sleep(1)
            return self.code_image_to_text(file_name)

    # 读取图片
    def get_file_content(self, file_name):
        with open(file_name, 'rb') as fp:
            return fp.read()

    def get_image_str(self, file_name):
        image = self.get_file_content(file_name)
        # 调用通用文字识别, 图片参数为本地图片
        result = client.basicGeneral(image)
    # 结果拼接返回输出
        if 'words_result' in result:
            return ''.join([w['words'] for w in result['words_result']])

    # 刷新页面
    def refresh_page(self):
        self.driver.refresh()
        self.log.info("已刷新页面")

    def login_sucess(self):
        self.log.info('开始获取验证码！！！')
        code = self.code_image_to_text()
        self.log.info("验证码获取完成，获取到的验证码为：{}".format(code))
        self.login(LD.sucess_data['username'], LD.sucess_data['password'], code)
        if self.get_title() != '智能配电房监测系统':
            self.log.info('登录失败！！！')
            self.refresh_page()
            self.clear_username_input()
            time.sleep(0.5)
            return self.login_sucess()
        else:
            self.log.info('登录成功！！！')


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('http://172.17.46.198:9080/IDRMS')
    a = LoginPage(driver)
    a.login_sucess()
