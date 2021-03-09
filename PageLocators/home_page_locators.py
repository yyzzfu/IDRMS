from selenium.webdriver.common.by import By


class HomePageLocator:

    # -----------------------------------------共用的定位元素--------------------------------------------------------
    # 在首页已默认打开的‘主页’的tab中的X定位
    home_tag_close = (By.XPATH, '//div[@id="jerichotab"]//div[text()="主页"]/following-sibling::div[@class="tab_close"]//a[@title="关闭"]')
    # 新增按钮
    add_button = (By.XPATH, "//*[@id='searchForm']//a[text()='新增']")
    # 所有页面的保存按钮
    submit = (By.XPATH, '//*[@id="btnSubmit"]')

    # ---------------------------------------档案管理----------------------------------------------------------------------------
    # 档案管理一级菜单展开按钮
    open_archive_management = (By.XPATH, "//*[@id='menu-2']/div//*[contains(text(),'配电房档案 ')]/../../../../..")
    # 配电房档案管理
    room_archive_management = (By.XPATH, '//*[@id="menu-2"]//*[contains(text(),"配电房档案")]')
    # 变压器档案管理
    transformer_archive_management = (By.XPATH, '//*[@id="left"]//*[@id="menu-2"]//*[contains(text(),"变压器档案")]')
    # 开关柜档案管理
    cabinet_archive_management = (By.XPATH, '//*[@id="left"]//*[@id="menu-2"]//*[contains(text(),"开关柜档案")]')
    # 监控设备管理
    monitoring_equipment_manage = (By.XPATH, '//*[@id="left"]//*[@id="menu-2"]//*[contains(text(),"监控设备")]')

    # ---------------------------------------测量点管理----------------------------------------------------------------------------
    # 测量点管理一级菜单展开按钮
    open_data_point_manage = (By.XPATH, "//*[@id='menu-2']/div//*[contains(text(),'智能网关测量点')]/../../../../..")
    # 数据节点管理
    data_point_manage = (By.XPATH, '//*[@id="left"]//*[@id="menu-2"]//*[contains(text(),"智能网关测量点")]')
    # 控制节点管理
    control_point_manage = (By.XPATH, '//*[@id="left"]//*[@id="menu-2"]//*[contains(text(),"智能网关控制点 ")]')
    # 智能网关告警设置
    alarm_set = (By.XPATH, '//*[@id="left"]//*[@id="menu-2"]//*[contains(text(),"智能网关告警设置")]')
    # 摄像头节点管理
    camera_manage = (By.XPATH, '//*[@id="left"]//*[@id="menu-2"]//*[contains(text(),"摄像头节点")]')




    iframe = (By.XPATH, '//div[@id="jerichotab_contentholder"]//iframe')

    # 保存成功提示信息
    # success_save_tip = (By.XPATH, '//*[@id="searchForm"]/following-sibling::div[@id="messageBox"]')
    success_save_tip = (By.XPATH, '//div[@id="messageBox"]')
    # 区域分布图保存成功提示信息
    hall_area_bg_success_save_tip = (By.XPATH, '//*[@id="inputForm"]/child::div[@id="messageBox"]')
    # 列表中第一个删除按钮
    delete_button = (By.XPATH, "//*[@id='contentTable']/tbody/tr[1]//a[2]")
    # 列表中最后一个删除按钮
    last_delete_button = (By.XPATH, ".//*[@id='contentTable']/tbody/tr[last()]/td[last()]/a[last()]")
    # 弹出框中确定按钮
    alert_accept_button = (By.XPATH, '//*[@id="jbox-state-state0"]//button[text()="确定"]')
    # 列表中第一个名称定位元素
    list_first_name_text = (By.XPATH, '//*[@id="contentTable"]/child::tbody/tr[1]//td[1]//a[1]')
    # 列表中最后一个名称定位元素
    list_last_name_text = (By.XPATH, './/*[@id="contentTable"]/tbody/tr[last()]/td[1]/a')
    # 上传按钮
    upload_button = (By.XPATH, "//*[@id='cke_9_label']")
    # 已上传的第一张图片定位元素
    the_first_image = (By.XPATH, '//*[@class="files_thumbnails fake no_list"]/a[1]/div')
    # the_first_image = (By.XPATH, '//*[@class="files_thumbnails fake no_list"]//h5[text()='modify(1).jpg']')  ------>之后进行优化，根据上传的图片名称进行定位
    # uploa_iframe定位元素
    upload_iframe = (By.XPATH, '//iframe[@allowtransparency="true"]')

# ---------------------------------------系统管理----------------------------------------------------------------------------
    # 系统管理展开按钮
    open_system_manage = (By.XPATH, "//*[@id='menu-2']/div//*[contains(text(),'用户管理')]/../../../../..")
    # 用户管理
    user_manage = (By.XPATH, '//*[@id="left"]//*[@id="menu-2"]//*[contains(text(),"用户管理")]')
    user_manage_iframe = 'officeContent'  # 用户管理编辑界面需要再切换一次iframe，通过iframe的id方式进行切换
    # 区域管理
    area_manage = (By.XPATH, '//*[@id="left"]//*[@id="menu-2"]//*[contains(text(),"区域管理")]')


# ---------------------------------------系统管理----------------------------------------------------------------------------
    # 页面底部“下一页”按钮
    next_page_button = (By.XPATH, ".//*[@id='dataGridPage']//a[contains(text(),'下一页 ')]")

    # 所有页面中，提示框中的确定按钮
    confirm_button = (By.XPATH, "//*[@id='jbox-states']//button[text()='确定']")


