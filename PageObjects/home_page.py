from Common.basepage import BasePage
from PageLocators.home_page_locators import HomePageLocator as loc
from PageObjects.login_page import LoginPage
import time
from Common import rename_filename_and_get_filepath_locator


class HomePage(BasePage):

    # 关闭“主页”标签---------------------------
    def close_home_tag(self):
        doc = '主页tab标签'
        self.click_element(loc.home_tag_close, doc)

# ---------------------------------------------------档案管理----------------------------------------------------
    # 展开档案管理---------------------------------
    def open_archive_management(self):
        doc = '主页'
        self.click_element(loc.open_archive_management, doc)

    # 进入配电房档案管理-----------------------------
    def enter_room_archive_management(self):
        try:
            # 关闭“主页”标签
            self.close_home_tag()
            # 展开档案管理一级菜单
            self.open_archive_management()
            # 点击配电房档案管理
            self.click_element(loc.room_archive_management)
            # 切换iframe到新打开的tab里面
            self.switch_iframe_to_new_tab()
            self.log.info('已进入配电房档案管理界面！！！')
        except:
            self.log.error('进入配电房档案管理界面失败！！！')

    # 进入变压器档案管理------------------------------------
    def enter_transformer_archive_management(self):
        try:
            # 关闭“主页”标签
            self.close_home_tag()
            # 展开档案管理一级菜单
            self.open_archive_management()
            # 点击变压器档案管理
            self.click_element(loc.transformer_archive_management)
            # 切换iframe到新打开的tab里面
            self.switch_iframe_to_new_tab()
            self.log.info('已进入变压器档案管理界面！！！')
        except:
            self.log.error('进入变压器档案管理界面失败！！！')

    # 进入开关柜档案管理-----------------------------------
    def enter_cabinet_archive_management(self):
        try:
            # 关闭“主页”标签
            self.close_home_tag()
            # 展开档案管理一级菜单
            self.open_archive_management()
            # 点击开关柜档案管理
            self.click_element(loc.cabinet_archive_management)
            # 切换iframe到新打开的tab里面
            self.switch_iframe_to_new_tab()
            self.log.info('已进入开关柜档案管理界面！！！')
        except:
            self.log.error('进入开关柜档案管理界面失败！！！')

    # 进入监控设备管理---------------------------------
    def enter_monitoring_equipment_manage(self):
        try:
            # 关闭“主页”标签
            self.close_home_tag()
            # 展开档案管理一级菜单
            self.open_archive_management()
            # 点击监控设备管理
            self.click_element(loc.monitoring_equipment_manage)
            # 切换iframe到新打开的tab里面
            self.switch_iframe_to_new_tab()
            self.log.info('已进入监控设备管理界面！！！')
        except:
            self.log.error('进入监控设备管理界面失败！！！')

    # 进入数据节点管理-----------------------------------
    def enter_data_point_manage(self):
        try:
            # 关闭“主页”标签
            self.close_home_tag()
            # 展开档案管理一级菜单
            self.click_element(loc.open_data_point_manage)
            # 点击数据节点管理
            self.click_element(loc.data_point_manage)
            # 切换iframe到新打开的tab里面
            self.switch_iframe_to_new_tab()
            self.log.info('已进入数据节点管理界面！！！')
        except:
            self.log.error('进入数据节点管理界面失败！！！')

    # 进入控制节点管理-----------------------------------
    def enter_control_point_manage(self):
        try:
            # 关闭“主页”标签
            self.close_home_tag()
            # 展开档案管理一级菜单
            # self.open_archive_management()
            self.click_element(loc.open_data_point_manage)
            # 点击数据节点管理
            self.click_element(loc.control_point_manage)
            # 切换iframe到新打开的tab里面
            self.switch_iframe_to_new_tab()
            self.log.info('已进入控制节点管理界面！！！')
        except:
            self.log.error('进入控制节点管理界面失败！！！')

        # 进入智能网关告警设置 -----------------------------------
    def enter_alarm_set(self):
        try:
            # 关闭“主页”标签
            self.close_home_tag()
            # 展开档案管理一级菜单
            self.click_element(loc.open_data_point_manage)
            # 点击数据节点管理
            self.click_element(loc.alarm_set)
            # 切换iframe到新打开的tab里面
            self.switch_iframe_to_new_tab()
            self.log.info('已进入智能网关告警设置界面！！！')
        except:
            self.log.error('进入智能网关告警设置失败！！！')

    # 进入摄像头节点设置 -----------------------------------
    def enter_camera_manage(self):
        try:
            # 关闭“主页”标签
            self.close_home_tag()
            # 展开档案管理一级菜单
            self.click_element(loc.open_data_point_manage)
            # 点击数据节点管理
            self.click_element(loc.camera_manage)
            # 切换iframe到新打开的tab里面
            self.switch_iframe_to_new_tab()
            self.log.info('已进入摄像头节点界面！！！')
        except:
            self.log.error('进入摄像头节点界面失败！！！')
# ---------------------------------------------------系统管理----------------------------------------------------

    # 展开系统管理------------------------------
    def open_system_manage(self):
        doc = '主页'
        self.click_element(loc.open_system_manage, doc=doc)

    # 进入用户管理------------------------------
    def enter_user_manage(self):
        try:
            # 关闭“主页”标签
            self.close_home_tag()
            # 展开系统管理一级菜单
            self.open_system_manage()
            # 点击用户管理
            self.click_element(loc.user_manage)
            # 切换iframe到新打开的tab里面
            self.switch_iframe_to_new_tab()  # 第一次切换iframe
            # 再切换一次, 这个页面比较特殊，需要切换两次iframe
            self.switch_iframe(loc.user_manage_iframe)  # 第二次切换iframe
            self.log.info('已进入用户管理界面！！！')
        except:
            self.log.error('进入用户管理界面失败！！！')

    # 进入区域管理------------------------------
    def enter_area_manage(self):
        try:
            # 关闭“主页”标签
            self.close_home_tag()
            # 展开系统管理一级菜单
            self.open_system_manage()
            # 点击区域管理
            self.click_element(loc.area_manage)
            # 切换iframe到新打开的tab里面
            self.switch_iframe_to_new_tab()
            self.log.info('已进入区域管理界面！！！')
        except:
            self.log.error('进入区域管理界面失败！！！')

    # 点击新增按钮
    def click_add_button(self):
        self.click_element(loc.add_button)

    # 点击保存按钮
    def click_submit_button(self):
        self.click_element(loc.submit)

    # 进入新的iframe
    def switch_iframe_to_new_tab(self):
        self.switch_iframe(self.get_element(loc.iframe))

    def get_success_save_tip(self):
        try:
            tip = self.get_text(loc.success_save_tip)
            self.log.info('获取提示信息成功！！！获取到的文本信息为{}'.format(tip))
            return tip
        except:
            self.log.info('获取提示信息失败！！！')

    def get_success_delete_tip(self):
        time.sleep(0.5)                   # 睡眠0.5秒，待删除成功后，再进行获取提示信息操作
        self.switch_iframe_to_new_tab()   # iframe切换，不然删除成功后，不能获取到删除成功提示信息
        try:
            tip = self.get_text(loc.success_save_tip)
            self.log.info('获取提示信息成功！！！获取到的文本信息为{}'.format(tip))
            return tip
        except:
            self.log.info('获取提示信息失败！！！')

    def get_hall_area_bg_success_save_tip(self):
        try:
            tip = self.get_text(loc.hall_area_bg_success_save_tip)
            self.log.info('获取区域分布图保存成功提示信息成功！！！获取到的文本信息为{}'.format(tip))
            return tip
        except:
            self.log.info('获取区域分布图保存成功提示信息失败！！！')

    def get_list_first_name_text(self):
        try:
            text = self.get_text(loc.list_first_name_text)
            self.log.info('获取列表第一行中的名称成功！！！')
            return text
        except:
            self.log.error('获取列表第一行中的名称失败！！！')

        # 获取列表中最后一个区域名称
    def get_list_last_name_text(self):
        try:
            text = self.get_text(loc.list_last_name_text)
            self.log.info('获取列表最后一行中的名称成功！！！')
            return text
        except:
            self.log.error('获取列表最后一行中的名称失败！！！')

    # 在打开的窗口中上传文件，并选择第一个文件后，点击保存按钮------------------------------------------------------
    def to_upload_file(self, dirpath, file_type='.jpg'):
        # 切换到iframe
        self.switch_iframe(self.get_element(loc.upload_iframe))
        # 点击上传按钮
        self.click_element(loc.upload_button)
        # 修改照片名称
        locator_and_path = rename_filename_and_get_filepath_locator.get_file_locator_and_path(dirpath, file_type)
        time.sleep(2)
        # 调用BasePage中的upload方法，传入文件
        self.upload(locator_and_path[1])
        # 加入time睡眠几秒
        time.sleep(2)
        # 双击已上传的图片
        self.double_click(locator_and_path[0])
        time.sleep(1)

    def to_upload_file_without_modify_filename(self, dirpath):
        # 切换到iframe
        self.switch_iframe(self.get_element(loc.upload_iframe))
        # 点击上传按钮
        self.click_element(loc.upload_button)
        # 修改照片名称
        locator_and_path = rename_filename_and_get_filepath_locator.get_file_locator_and_path_without_modify_filename(dirpath)
        time.sleep(2)
        # 调用BasePage中的upload方法，传入文件
        self.upload(locator_and_path[1])
        # 加入time睡眠几秒
        time.sleep(2)
        # 双击已上传的图片
        self.double_click(locator_and_path[0])
        time.sleep(1)

    # 获取页面底部“下一页”按钮元素中的onclick的值
    def get_next_page_button_onclick_value(self, attribute='onclick'):
        return self.get_element_attribute(loc.next_page_button, attribute)

    # 判断是否需要点击页面底部“下一页”按钮
    def whether_need_click_next_page_button(self, locator):
        while True:
            if self.wait_eleVisible(locator):
                # 如果在当前页面中，找到了元素，则停止循环
                break
            if self.get_next_page_button_onclick_value():   # 如果当前页面没有找到元素，且“下一页”按钮可点击
                self.click_element(loc.next_page_button)    # 则点击“下一页”按钮，继续循环，在跳转的页面中继续查找是否存在目标元素
            else:
                self.log('已经是最后一页了，下一页按钮不可点击')
                break    # 如果当前页面没有找到目标元素，且“下一页”按钮不可点击，则停止循环


if __name__ == '__main__':
    from selenium import webdriver
    from PageLocators.login_page_locators import LoginPageLocator
    driver = webdriver.Chrome()
    driver.get('http://172.17.46.198:9080/IDRMS')
    hp = HomePage(driver)
    LoginPage(driver).input_text(LoginPageLocator().username_ele, "idrmstest")
    LoginPage(driver).input_text(LoginPageLocator().password_ele, "fu123456")
    time.sleep(10)
    LoginPage(driver).click_element(LoginPageLocator().click_button)
    hp.enter_cabinet_archive_management()
