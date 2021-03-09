from Common.basepage import BasePage
from PageObjects.home_page import HomePage
from PageLocators.SystemManageLocators.user_manage_locators import UserManageLocators as loc
from PageLocators.home_page_locators import HomePageLocator as loc_home


class UserManagePage(BasePage):

    # 编辑用户
    def edit_user(self, name, user_name, password, confirm_password, email, phone, role, manage_room, remark, mode, manage_room_old):
        if name:
            # 输入姓名
            if mode == '修改':
                self.clear_input(loc.name)
            self.input_text(loc.name, name)
        if user_name:
            # 输入登录名
            if mode == '修改':
                self.clear_input(loc.user_name)
            self.input_text(loc.user_name, user_name)
        if password:
            # 输入密码
            if mode == '修改':
                self.clear_input(loc.password)
            self.input_text(loc.password, password)
        if confirm_password:
            # 输入确认密码
            if mode == '修改':
                self.clear_input(loc.confirm_password)
            self.input_text(loc.confirm_password, confirm_password)
        if email:
            # 输入邮箱，可为空
            if mode == '修改':
                self.clear_input(loc.email)
            self.input_text(loc.email, email)
        if phone:
            # 输入手机号
            if mode == '修改':
                self.clear_input(loc.phone)
            self.input_text(loc.phone, phone)
        if mode == '新增':
            if role:
                # 选择用户角色+
                if role != "系统管理员":
                    role_replace = str(loc.role).replace('replace', role)
                    self.click_element(loc.role_manage)
                    self.click_element(eval(role_replace))
            if manage_room:
                # 选择管辖配电房
                manage_room_list = str(manage_room).split('|')  # 传入多个配电房时，使用|符号将其切片，得到一个列表
                for i in manage_room_list:
                    manage_room_replace = str(loc.manage_room).replace('replace', i)  # 将replace替换为传入的配电房名称
                    self.click_element(eval(manage_room_replace))
        if mode == '修改':
            if role:
                # 选择用户角色
                role_replace = str(loc.role).replace('replace', role)
                self.click_element(eval(role_replace))
            if manage_room:
                # 取消之前已勾选的配电房
                manage_room_old_list = str(manage_room_old).split('|')  # 传入多个配电房时，使用|符号将其切片，得到一个列表
                for i in manage_room_old_list:
                    manage_room_replace = str(loc.manage_room).replace('replace', i)  # 将replace替换为传入的配电房名称
                    self.click_element(eval(manage_room_replace))
                # 选择管辖配电房
                manage_room_list = str(manage_room).split('|')  # 传入多个配电房时，使用|符号将其切片，得到一个列表
                for i in manage_room_list:
                    manage_room_replace = str(loc.manage_room).replace('replace', i)  # 将replace替换为传入的配电房名称
                    self.click_element(eval(manage_room_replace))
        if remark:
            # 输入备注信息
            if mode == '修改':
                self.clear_input(loc.remark)
            self.input_text(loc.remark, remark)
        # 点击保存按钮
        HomePage(self.driver).click_submit_button()

    # 新增用户
    def add_user(self, name=None, user_name=None, password=None, confirm_password=None, email=None,
                 phone=None, role=None, manage_room=None, remark=None):
        # 进入用户管理界面
        HomePage(self.driver).enter_user_manage()
        # 点击新增按钮
        HomePage(self.driver).click_add_button()
        # 在用户编辑界面进行输入
        self.edit_user(name, user_name, password, confirm_password, email, phone, role, manage_room, remark, mode='新增', manage_room_old=None)

    # 修改用户
    def modify_user(self, user_name_location, name=None, user_name=None, password=None, confirm_password=None, email=None, phone=None,
                    role=None, manage_room=None, remark=None, manage_room_old=None):
        # 进入用户管理界面
        HomePage(self.driver).enter_user_manage()
        modify_button_replace = str(loc.modify_button).replace('replace', user_name_location)
        # 当前页面是否存在目标元素，不存在则点击下一页按钮，在其他的页面继续查找
        HomePage(self.driver).whether_need_click_next_page_button(eval(modify_button_replace))
        # 点击修改按钮
        self.click_element(eval(modify_button_replace))
        # 在用户编辑界面进行输入
        self.edit_user(name, user_name, password, confirm_password, email, phone, role, manage_room, remark, mode='修改', manage_room_old=manage_room_old)

    # 删除用户
    def delete_user(self, user_name_location):
        # 进入用户管理界面
        HomePage(self.driver).enter_user_manage()
        delete_button_replace = str(loc.delete_button).replace('replace', user_name_location)
        # 当前页面是否存在目标元素，不存在则点击下一页按钮，在其他的页面继续查找
        HomePage(self.driver).whether_need_click_next_page_button(eval(delete_button_replace))
        # 点击删除按钮
        self.click_element(eval(delete_button_replace))
        # 切换到默认iframe
        self.back_to_default_content()
        time.sleep(0.5)
        # 在弹出的提示框中点击确定按钮
        self.click_element(loc_home.confirm_button)


if __name__ == '__main__':
    from selenium import webdriver
    from PageObjects.login_page import LoginPage
    from PageLocators.login_page_locators import LoginPageLocator as loc_1
    from Common import dir_config
    from Common.do_excel import DoExcel
    import time

    driver = webdriver.Chrome()
    driver.get('http://172.17.46.198:9080/IDRMS')
    LoginPage(driver).input_text(loc_1.username_ele, "idrmstest")
    LoginPage(driver).input_text(loc_1.password_ele, "fu123456")
    time.sleep(10)
    LoginPage(driver).click_element(loc_1.click_button)
    test_datas = DoExcel('user').get_data(dir_config.archives_data_excel_path)[0]
    UserManagePage(driver).add_user(test_datas['name'], test_datas['user_name'], test_datas['password'], test_datas['confirm_password'], test_datas['email'],
                                    test_datas['phone'], test_datas['role'], test_datas['manage_room'], test_datas['remark'])