# 封装基本函数：执行日志、遗产处理、失败截图
# 所有页面的公共部分
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime
from Common import dir_config
import time
from Common.my_log import MyLog
from selenium.webdriver.support.select import Select
import win32gui
import win32con
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.log = MyLog()

    # 等待元素可见
    def wait_eleVisible(self, locator, times=6, poll_frequency=0.5, doc=''):
        '''
        :param locator: 元素定位方式，元祖类型，如（BY.XPATH, XPTAH定位表达式）
        :param times: 最长等待时间
        :param poll_frequency: 多长时间查询一次
        :param doc: 操作的具体页面，doc的值传给except中的截图函数
        :return:
        '''
        self.log.info('{0}-->等待元素:{1}可见'.format(doc, locator))
        try:
            start = datetime.datetime.now()
            WebDriverWait(self.driver, times, poll_frequency).until(EC.visibility_of_element_located(locator))
            end = datetime.datetime.now()
            wait_times = (end - start).seconds
            self.log.info('{0}-->元素:{1}-->已可见，等待时长为{2}'.format(doc, locator, wait_times))
            return True
        except:
            self.log.error('等待元素:{}可见失败！'.format(locator))
            # 截图
            # self.save_screen_picture(doc)
            return False

    def wait_eleVisible_without_screen_picture(self, locator, times=20, poll_frequency=0.5, doc=''):
        '''
        :param locator: 元素定位方式，元祖类型，如（BY.XPATH, XPTAH定位表达式）
        :param times: 最长等待时间
        :param poll_frequency: 多长时间查询一次
        :param doc: 操作的具体页面，doc的值传给except中的截图函数
        :return:
        '''
        self.log.info('在首页判断元素:{0}是否可见'.format(locator))
        try:
            start = datetime.datetime.now()
            WebDriverWait(self.driver, times, poll_frequency).until(EC.visibility_of_element_located(locator))
            end = datetime.datetime.now()
            wait_times = (end - start).seconds
            self.log.info('在首页元素:{0}-->已可见，等待时长为{1}------该项已展开'.format(locator, wait_times))
        except:
            self.log.error('在首页等待元素:{}可见失败！------该项未展开'.format(locator))
            # 截图
            # self.save_screen_picture(doc)
            raise

    # 截图
    def save_screen_picture(self, doc):
        '''
        :param doc: 当前操作的页面，如登录页面
        :return: None
        '''
        # 图片名称：页面名称_操作名称_时间.png
        # file_path = dir_config.screenshot_dir
        # file_name = r"G:\PycharmProjects\dmp\Outputs\screenshots\{0}_{1}.png".format(doc, time)
        file_name = dir_config.screenshot_dir + \
                    "/{0}_{1}.png".format(doc, time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time())))
        try:
            self.driver.save_screenshot(file_name)
            self.log.info('截图成功，存放路径为：{}'.format(file_name))
        except:
            self.log.error('截图失败')
            raise

    # 等待元素存在
    def wait_elePresence(self):
        pass

    # 判断元素是否不存在与DOM树里面或不可见
    def invisibility_of_ele(self, locator, times=5, poll_frequency=0.5, doc=''):
        try:
            WebDriverWait(self.driver, times, poll_frequency).until(EC.invisibility_of_element_located(locator))
            self.log.info('{0}元素{1}不存在'.format(doc, locator))
        except:
            self.log.error('元素{}存在'.format(locator))

    # 查找元素--一个
    def get_element(self, locator, doc=''):
        self.wait_eleVisible(locator, doc=doc)
        try:
            return self.driver.find_element(*locator)
        except:
            self.log.error('查找元素:{}失败'.format(locator))
            self.save_screen_picture(doc)
            # raise
            return False

    # 查找元素--一组
    def get_elements(self, locator, doc=''):
        self.wait_eleVisible(locator, doc=doc)
        try:
            return self.driver.find_elements(*locator)
        except:
            self.log.error('查找元素:{}失败'.format(locator))
            self.save_screen_picture(doc)
            raise

    # 点击操作
    def click_element(self, locator, doc=''):
        ele = self.get_element(locator)
        self.log.info('{0}-->点击元素:{1}'.format(doc, locator))
        try:
            ele.click()
        except:
            self.log.error('点击元素:{}失败'.format(locator))
            self.save_screen_picture(doc)
            raise

    # 定位为一组元素时，点击第一个元素
    def click_elements(self, locator, doc=''):
        ele = self.get_elements(locator)
        try:
            ele.click()
            self.log.info('{0}-->点击元素:{1}'.format(doc, locator))
        except:
            self.log.error('点击元素:{}失败'.format(locator))
            self.save_screen_picture(doc)
            raise

    # 通过get_elements获取到的定位元素，进行点击操作，函数中传入的是get_elements获取到的值，而不是元素定位表达式
    def click_ele(self, ele, doc=''):
        try:
            ele.click()
            self.log.info('在{0}点击{1}成功'.format(doc, ele))
        except:
            self.log.error('在{}点击失败'.format(doc))

    # 输入操作
    def input_text(self, locator, text, doc=''):
        ele = self.get_element(locator, doc)
        self.log.info('在{0}-->元素：{1}进行输入操作'.format(doc, locator))
        try:
            ele.send_keys(text)
            self.log.info('在元素{0}上输入的值为-------->>>>>{1}'.format(locator, text))
        except:
            self.log.error('在元素{}上输入失败'.format(locator))
            self.save_screen_picture(doc)
            raise

    # 获取元素的文本内容
    def get_text(self, locator, doc=''):
        ele = self.get_element(locator, doc)
        self.log.info('在{0}中-->获取元素:{1}的文本内容'.format(doc, locator))
        try:
            self.log.info('获取到{0}元素的文本内容为-------->>>>>{1}'.format(locator, ele.text))
            return ele.text
        except:
            self.log.error('获取元素:{}的文本内容失败'.format(locator))
            self.save_screen_picture(doc)
            raise

    # 清空输入框
    def clear_input(self, locator, doc=''):
        ele = self.get_element(locator, doc)
        try:
            self.log.info('在{0}-->清空元素(**输入框**)：{1}中的内容'.format(doc, locator))
            ele.clear()
        except:
            self.log.error('清空{}输入框失败'.format(locator))
            raise

    # 获取title
    def get_title(self, doc=''):
        self.log.info('获取当前页面的title')
        try:
            self.log.info('在当前页面获取到的title是-->{0}'.format(self.driver.title))
            return self.driver.title
        except:
            self.log.error('在当前页面获取title失败！')

    # 获取元素的属性值
    def get_element_attribute(self, locator, attribute):
        self.log.info('获取{}元素中{}属性的属性值'.format(locator, attribute))
        try:
            ele = self.get_element(locator)
            return ele.get_attribute(attribute)
        except:
            self.log.error('在当前页面获取title失败！')
            return False

    # alert处理
    def alert_action(self, action='accept'):
        if action == 'accept':
            self.driver.switch_to_alert().accept()
        else:
            self.driver.switch_to_alert().dismiss()

    # iframe切换
    def switch_iframe(self, iframe_ele_or_name_id):
        self.log.info('准备切换iframe')
        try:
            self.driver.switch_to.frame(iframe_ele_or_name_id)
            self.log.info('已切换到{}iframe'.format(iframe_ele_or_name_id))
        except:
            self.log.error('切换iframe失败')

    # 返回默认iframe
    def back_to_default_content(self):
        self.driver.switch_to.default_content()
        self.log.info("已切回到默认的iframe")

    # 获取当前窗口的句柄
    def get_current_window_handle(self):
        self.log.info('获取当前窗口的句柄')
        try:
            current_window_handle = self.driver.current_window_handle
            self.log.info('获取当前窗口的句柄成功！！！当前窗口句柄为{}'.format(current_window_handle))
            return current_window_handle
        except:
            self.log.error('获取当前窗口的句柄失败！！！')

    # 窗口切换--切换到最新的窗口
    def switch_to_new_window(self, c_window):
        # c_window = self.driver.current_window_handle()
        windows = self.driver.window_handles
        self.log.info('所有窗口的句柄分别为{}'.format(windows))
        try:
            for i in windows:
                if i != c_window:
                    self.driver.switch_to.window(i)
                    self.log.info('已切换到最新的窗口！！！窗口句柄为{}'.format(i))
        except:
            self.log.error('切换到最新的窗口失败！！！')

    # 返回之前的窗口
    def back_to_default_window(self, c_window):
        self.log.info('返回到默认窗口')
        try:
            self.driver.switch_to.window(c_window)
            self.log.info('返回到默认窗口成功！！！窗口句柄为{}'.format(c_window))
        except:
            self.log.error('返回到默认窗口失败！！！')

    # 上传操作
    def upload(self, filePath, browser_type="chrome"):
        '''
        通过pywin32模块实现文件上传的操作
        :param filePath: 文件的绝对路径
        :param browser_type: 浏览器类型（默认值为chrome）
        :return:
        如何使用：
        # 在打开上传弹窗后，直接调用 upload 方法，传需要上传文件的绝对路径即可,upload("文件路径")
        '''
        if browser_type.lower() == "chrome":
            title = "打开"
        elif browser_type.lower() == "firefox":
            title = "文件上传"
        elif browser_type.lower() == "ie":
            title = "选择要加载的文件"
        else:
            title = ""  # 这里根据其它不同浏览器类型来修改
        self.log.info('准备上传文件，文件的路径为{}'.format(filePath))
        try:
            # 找元素
            # 一级窗口"#32770","打开"
            dialog = win32gui.FindWindow("#32770", title)
            # 向下传递
            ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, "ComboBoxEx32", None)  # 二级
            comboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, "ComboBox", None)  # 三级
            # 编辑按钮
            edit = win32gui.FindWindowEx(comboBox, 0, 'Edit', None)  # 四级
            # 打开按钮
            button = win32gui.FindWindowEx(dialog, 0, 'Button', "打开(&O)")  # 二级
            # 输入文件的绝对路径，点击“打开”按钮
            time.sleep(1)
            win32gui.SendMessage(edit, win32con.WM_SETTEXT, None, filePath)  # 发送文件路径
            time.sleep(1)
            win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  # 点击打开按钮
            self.log.info('文件上传成功！！！')
        except:
            self.log.error('文件上传失败！！！')

    # 下拉框选择--一个定位元素定位到了多个下拉框
    def selects(self, locator, m, n, doc=''):
        '''
        :param locator:
        :param m: 选择定位到的第几个元素
        :param n: 选择下拉框中第几个元素
        :param doc: 日志中需输入的msg
        :return:
        '''
        # self.wait_eleVisible(locator)            0807注释
        ele = self.get_elements(locator)[m]
        try:
            Select(ele).select_by_index(n)
            self.log.info('在{0}下拉框中选择第{1}个选项成功'.format(doc, n+1))
        except:
            self.log.error('在{0}下拉框中选择第{1}个选项失败'.format(doc, n+1))
            raise

    # 下拉框选择--一个定位元素定位一个下拉框
    def select(self, locator, n=1):
        ele = self.get_element(locator)
        try:
            Select(ele).select_by_index(n)
            self.log.info('下拉框中选择选项成功')
        except:
            self.log.error('下拉框中选择选项失败')
            raise

    # 下拉框选择--一个定位元素定位一个下拉框
    def select_by_text(self, locator, text):
        ele = self.get_element(locator)
        try:
            # Select(ele).select_by_index(n)
            Select(ele).select_by_visible_text(text)
            self.log.info('下拉框中选择选项成功')
        except:
            self.log.error('下拉框中选择选项失败')
            raise

    # 刷新页面
    def refresh_page(self):
        try:
            self.driver.refresh()
            self.log.info('刷新页面')
        except:
            self.log.error('刷新页面失败')
            raise

    # 鼠标双击操作
    def double_click(self, locator):
        self.log.info('准备执行鼠标双击{}'.format(locator))
        try:
            ele = self.get_element(locator)
            ActionChains(self.driver).double_click(ele).perform()
            self.log.info('执行鼠标双击成功！！！')
        except:
            self.log.error('执行鼠标双击失败！！！')

    # 鼠标悬停到某个元素上
    def move_to_element(self, locator):
        self.log.info('准备将鼠标悬停在{}元素上'.format(locator))
        try:
            ele = self.get_element(locator)
            ActionChains(self.driver).move_to_element(ele).perform()
            self.log.info('准备将鼠标悬停在元素上成功！！！')
        except:
            self.log.error('准备将鼠标悬停在元素上失败！！！')

    # js操作
    def execute_script(self, element):
        self.log.info('准备移除{}元素的readonly属性'.format(element))
        try:
            self.driver.execute_script("arguments[0].removeAttribute('readonly')", element)
            self.log.info('移除{}元素的readonly属性成功！！！'.format(element))
        except:
            self.log.error('移除{}元素的readonly属性失败！！！'.format(element))

    # 输入框输入内容后，点击回车键
    def enter_button(self, locator):
        ele = self.get_element(locator)
        try:
            ele.send_keys(Keys.ENTER)
        except:
            raise