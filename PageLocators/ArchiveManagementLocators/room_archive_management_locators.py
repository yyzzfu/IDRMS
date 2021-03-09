from selenium.webdriver.common.by import By


class RoomArchiveManagementLocators:

    # 配电房名称
    room_name = (By.XPATH, "//*[@id='name']")
    # 所属区域
    area_select = (By.XPATH, "//*[@id='areaName']")
    # 所属区域选择界面中的iframe
    # iframe_area = (By.XPATH, '//*[@id="jerichotabmenu"]/following-sibling::div[1]//iframe')
    iframe_area = 'jbox-iframe'

    # 所属区域选择界面中区域名称为“中国”的选项-------------------------后续优化，区域名称参数化
    # area_name = (By.XPATH, "//*[@id='tree']//*[text()='武汉']")
    area_name = (By.XPATH, "//*[@id='tree']//*[text()='replace']")

    # 确定按钮
    confirm_button = (By.XPATH, "//*[@id='jbox-states']//button[text()='确定']")
    # 配电房地址
    room_address = (By.XPATH, "//*[@id='address']")
    # 配电房布局图--选择按钮
    picture_choice_button = (By.XPATH, '//*[@id="inputForm"]//a[text()="选择"]')
    # 备注信息
    remark = (By.XPATH, "//*[@id='remarks']")
    # --------------------------------------------------------配电房布局图----------------------------------------------
    # 配电房布局图添加按钮
    add_mapPic_button = (By.XPATH, "//*[@id='distribuitionRoomMapUrlFilePicker']/div[2]/label")
    # 配电房布局图图片
    mapPic = (By.XPATH, "//*[@id='distribuitionRoomMapThumbnail']/img")
    # 配电房布局图删除按钮
    delete_mapPic_button = (By.XPATH, "//*[@id='mapPicDeleteButton']")
    # --------------------------------------------------------配电房控制图----------------------------------------------
    # 配电房控制图添加按钮
    add_controlPic_button = (By.XPATH, "//div[@id='controlPic']/div[2]")
    # 配电房控制图图片
    controlPic = (By.XPATH, "//*[@id='distribuitionRoomCtrlThumbnail']/img")
    # 配电房控制图删除按钮
    delete_controlPic_button = (By.XPATH, "//*[@id='controlPicDeleteButton']")
    # --------------------------------------------------------配电房一次接线图----------------------------------------------
    # 配电房一次接线图按钮
    add_primaryDiagram_button = (By.XPATH, "//div[@id='primaryDiagram']/div[2]")
    # 配电房一次接线图图片1
    primaryDiagram_1 = (By.XPATH, "//*[@id='arDistributionRoomChartListThumbnail[0]_primaryDiagramView']/img")
    # 配电房一次接线图图片1删除按钮
    delete_primaryDiagram_1_button = (By.XPATH, "//*[@id='chartOneDeleteButton']")
    # 配电房一次接线图图片2
    primaryDiagram_2 = (By.XPATH, "//*[@id='arDistributionRoomChartListThumbnail[1]_primaryDiagramView']/img")
    # 配电房一次接线图图片2删除按钮
    delete_primaryDiagram_2_button = (By.XPATH, "//*[@id='chartTwoDeleteButton']")

    # 列表中修改按钮，将replace替换为对应的配电房名称即可
    modify_button = (By.XPATH, "//table[@id='dataGrid']//td[@title='replace']/..//div[@title='修改']")
    # 列表中删除按钮，将replace替换为对应的配电房名称即可
    delete_button = (By.XPATH, "//table[@id='dataGrid']//td[@title='replace']/..//div[@title='删除']")



