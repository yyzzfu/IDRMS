from Common.basepage import BasePage
from PageObjects.home_page import HomePage
from PageLocators.ArchiveManagementLocators.room_archive_management_locators import RoomArchiveManagementLocators as loc
import time


class RoomArchiveManagementPage(BasePage):

    # 编辑配电房
    def edit_room_archive(self, room_name, area, room_address, map_pic_path, control_pic_path, primary_diagram_path, remark, mode):
        if room_name:
            if mode == '修改':
                self.clear_input(loc.room_name)
            # 输入配电房名称
            self.input_text(loc.room_name, room_name)
        if area:
            # 点击区域选择框
            self.click_element(loc.area_select)
            # 切回到默认的iframe
            self.back_to_default_content()
            # 切换iframe到区域选择界面
            self.switch_iframe(loc.iframe_area)
            time.sleep(1)
            # 双击需要勾选的区域名称
            # 从RoomArchiveManagementLocators类中获取area_name定位元素的值，并将其中的replace替换为函数传入的area
            area_name_replace = str(loc.area_name).replace('replace', area)
            self.double_click(eval(area_name_replace))
            # 切换iframe到档案管理编辑界面
            HomePage(self.driver).switch_iframe_to_new_tab()
        if room_address:
            if mode == '修改':
                self.clear_input(loc.room_address)
            # 输入配电房地址，可为空
            self.input_text(loc.room_address, room_address)
        if map_pic_path:
            if mode == '修改':
                # 将鼠标移动到已上传的“配电房布局图”上
                self.move_to_element(loc.mapPic)
                time.sleep(0.5)
                # 点击删除按钮
                self.click_element(loc.delete_mapPic_button)
                time.sleep(0.5)
            # 点击配电房布局图添加按钮
            self.click_element(loc.add_mapPic_button)
            time.sleep(1)
            self.upload(map_pic_path)
            time.sleep(1)
        # 如果control_pic_path不为空，点击配电房控制图添加按钮
        if control_pic_path:
            if mode == '修改':
                # 将鼠标移动到已上传的“配电房控制图”上
                self.move_to_element(loc.controlPic)
                time.sleep(0.5)
                # 点击删除按钮
                self.click_element(loc.delete_controlPic_button)
                time.sleep(0.5)
            # 点击配电房控制图添加按钮
            self.click_element(loc.add_controlPic_button)
            time.sleep(1)
            self.upload(control_pic_path)
            time.sleep(1)
        # 如果primary_diagram_path不为空，点击配电房一次接线图添加按钮
        if primary_diagram_path:
            primary_diagram_path_list = str(primary_diagram_path).split('|')
            number_of_picture = len(primary_diagram_path_list)
            if mode == '修改':
                if number_of_picture == 1:
                    # 将鼠标移动到已上传的第一张“配电房一次接线图”上
                    self.move_to_element(loc.primaryDiagram_1)
                    time.sleep(0.5)
                    # 点击图片上方的删除按钮
                    self.click_element(loc.delete_primaryDiagram_1_button)
                    time.sleep(0.5)
                if number_of_picture == 2:
                    # 将鼠标移动到已上传的第一张“配电房一次接线图”上
                    self.move_to_element(loc.primaryDiagram_1)
                    time.sleep(0.5)
                    # 点击图片上方的删除按钮
                    self.click_element(loc.delete_primaryDiagram_1_button)
                    time.sleep(0.5)
                    # 将鼠标移动到已上传的第二张“配电房一次接线图”上
                    self.move_to_element(loc.primaryDiagram_2)
                    time.sleep(0.5)
                    # 点击图片上方的删除按钮
                    self.click_element(loc.delete_primaryDiagram_2_button)
                    time.sleep(0.5)
            for i in primary_diagram_path_list:
                self.click_element(loc.add_primaryDiagram_button)
                time.sleep(1)
                self.upload(i)
                time.sleep(1)
        if remark:
            if mode == '修改':
                self.clear_input(loc.remark)
            # 输入备注信息，可为空
            self.input_text(loc.remark, remark)
        # 点击保存按钮
        HomePage(self.driver).click_submit_button()

    # 新增配电房
    def add_room_archive(self, room_name=None, area=None, room_address=None, map_pic_path=None,
                         control_pic_path=None, primary_diagram_path=None, remark=None):
        # 进入配电房档案管理界面
        HomePage(self.driver).enter_room_archive_management()
        # 点击新增按钮
        HomePage(self.driver).click_add_button()
        # 在配电房编辑界面进行输入
        self.edit_room_archive(room_name, area, room_address, map_pic_path, control_pic_path, primary_diagram_path, remark, mode=None)

    # 修改配电房
    def modify_room_archive(self, modify_room, room_name=None, area=None, room_address=None, map_pic_path=None,
                            control_pic_path=None, primary_diagram_path=None, remark=None):
        # 进入配电房档案管理界面
        HomePage(self.driver).enter_room_archive_management()
        # 从配电房列表中--需要修改的配电房--对应的操作栏中，点击修改按钮
        # 如果配电房信息比较多，有多页--而需要修改的配电房不在第一页，则需要翻页
        modify_button_replace = str(loc.modify_button).replace('replace', modify_room)
        HomePage(self.driver).whether_need_click_next_page_button(eval(modify_button_replace))
        # 在对应配电房操作栏中点击修改按钮
        self.click_element(eval(modify_button_replace))
        # 在配电房编辑界面进行输入
        self.edit_room_archive(room_name, area, room_address, map_pic_path, control_pic_path, primary_diagram_path, remark, mode='修改')

    # 删除配电房
    def delete_room_archive(self, delete_room):
        """
        :param delete_room: 需要删除的配电房名称
        :return:
        """
        # 进入配电房档案管理界面
        HomePage(self.driver).enter_room_archive_management()
        # 从配电房列表中--需要修改的配电房--对应的操作栏中，点击删除按钮
        # 如果配电房信息比较多，有多页--而需要删除的配电房不在第一页，则需要翻页
        delete_button_replace = str(loc.delete_button).replace('replace', delete_room)
        HomePage(self.driver).whether_need_click_next_page_button(eval(delete_button_replace))
        # 在对应配电房操作栏中点击删除按钮
        self.click_element(eval(delete_button_replace))
        # 切换到默认iframe
        self.back_to_default_content()
        time.sleep(0.5)
        # 在弹出的提示框中点击确定按钮
        self.click_element(loc.confirm_button)


if __name__ == '__main__':
    from selenium import webdriver
    from PageObjects.login_page import LoginPage
    from PageLocators.login_page_locators import LoginPageLocator as loc_1
    from Common import dir_config
    from Common.do_excel import DoExcel

    driver = webdriver.Chrome()
    driver.maximize_window()
    # url = 'http://www.baidu.com'
    url = 'http://172.17.46.196:8080/IDRMS'
    driver.get(url)
    LoginPage(driver).input_text(loc_1.username_ele, "admin")
    LoginPage(driver).input_text(loc_1.password_ele, "e2020jl")
    time.sleep(10)
    LoginPage(driver).click_element(loc_1.click_button)
    # test_datas = DoExcel('room').get_data(dir_config.archives_data_excel_path)   # 结果为列表
    # RoomArchiveManagementPage(driver).add_room_archive(test_datas[0]['room_name'], test_datas[0]['area'], test_datas[0]['room_address'],
    #                                                    test_datas[0]['map_pic_path'], test_datas[0]['control_pic_path'], test_datas[0]['primary_diagram_path'],
    #                                                    test_datas[0]['remark'])
    # RoomArchiveManagementPage(driver).add_room_archive(room_name='新增配电房002', area='湖北武汉1', room_address='新增地址002',
    #                                                    map_pic_path=r'C:\Users\yyzz\Desktop\图片\IDRMS\布局图.png',
    #                                                    control_pic_path=r'C:\Users\yyzz\Desktop\图片\IDRMS\控制图.png',
    #                                                    primary_diagram_path=r'C:\Users\yyzz\Desktop\图片\IDRMS\接线图1.svg|C:\Users\yyzz\Desktop\图片\IDRMS\乌海一次接线图.svg',
    #                                                    remark='新增备注002')
    # RoomArchiveManagementPage(driver).modify_room_archive(modify_room='新增配电房001', room_name='修改配电房001', area='湖北武汉6', room_address='修改地址001',
    #                                                    map_pic_path=r'C:\Users\yyzz\Desktop\图片\IDRMS\布局图.png',
    #                                                    control_pic_path=r'C:\Users\yyzz\Desktop\图片\IDRMS\控制图.png',
    #                                                    primary_diagram_path=r'C:\Users\yyzz\Desktop\图片\IDRMS\接线图1.svg|C:\Users\yyzz\Desktop\图片\IDRMS\乌海一次接线图.svg',
    #                                                    remark='修改备注001')
    RoomArchiveManagementPage(driver).delete_room_archive('修改配电房001')

