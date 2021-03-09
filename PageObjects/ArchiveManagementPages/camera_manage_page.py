from Common.basepage import BasePage
from PageObjects.home_page import HomePage
from PageLocators.ArchiveManagementLocators.camera_manage_locators import CameraManageLocators as loc
from PageLocators.home_page_locators import HomePageLocator as loc_home


class CameraManage(BasePage):

    def edit_camera(self, room, NVR, camera_name, channel_number, whether_control, mode):
        if room:
            # room_choice_replace = str(loc.room_choice).replace(room, 'replace')
            self.click_element(loc.room)
            # self.click_element(eval(room_choice_replace))
            self.input_text(loc.input_locator, room)
            self.enter_button(loc.input_locator)
        if NVR:
            # NVR_choice_replace = str(loc.NVR_choice).replace(NVR, 'replace')
            self.click_element(loc.open_NVR)
            # self.click_element(NVR_choice_replace)
            self.input_text(loc.input_locator, NVR)
            self.enter_button(loc.input_locator)
        if camera_name:
            if mode=='修改':
                self.clear_input(loc.camera_name)
            self.input_text(loc.camera_name, camera_name)
        if channel_number:
            if mode=='修改':
                self.clear_input(loc.channel_number)
            self.input_text(loc.channel_number, channel_number)
        if whether_control:
            whether_control_replace = str(loc.whether_control).replace('replace', whether_control)
            self.click_element(eval(whether_control_replace))
        # 点击保存并返回按钮
        self.click_element(loc.submit_and_return)

    def add_camera(self, room=None, NVR=None, camera_name=None, channel_number=None, whether_control=None):
        HomePage(self.driver).enter_camera_manage()
        HomePage(self.driver).click_add_button()
        self.edit_camera(room=room, NVR=NVR, camera_name=camera_name, channel_number=channel_number, whether_control=whether_control, mode='新增')


if __name__ == '__main__':
    from selenium import webdriver
    from PageObjects.login_page import LoginPage
    from PageLocators.login_page_locators import LoginPageLocator as loc_1
    from Common import dir_config
    from Common.do_excel import DoExcel
    import time

    driver = webdriver.Chrome()
    driver.get('http://172.17.46.200:8080/IDRMS')
    driver.maximize_window()
    LoginPage(driver).input_text(loc_1.username_ele, "admin")
    LoginPage(driver).input_text(loc_1.password_ele, "e2020jl")
    time.sleep(10)
    LoginPage(driver).click_element(loc_1.click_button)


    CameraManage(driver).add_camera('样机配电房', 'NVR', '摄像头test', '32', whether_control='是')