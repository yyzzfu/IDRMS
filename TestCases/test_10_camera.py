import pytest
import allure
from PageObjects.ArchiveManagementPages.camera_manage_page import CameraManage
from PageObjects.home_page import HomePage
from Common import dir_config
from Common.do_excel import DoExcel


@allure.epic('项目名称：配电房平台V1.0')
@pytest.mark.usefixtures('enter_the_homepage')
# @pytest.mark.usefixtures('delete_table_ar_control_point')
@pytest.mark.usefixtures('refresh')
@allure.feature('档案管理')
@allure.story('摄像头节点管理')
# @pytest.mark.skip('跳过')
class TestCameraManage:

    datas = DoExcel('camera').get_data(dir_config.archives_data_excel_path)

    @pytest.mark.parametrize('data', datas)
    @allure.title('摄像头节点--新增功能')
    def test_add_camera(self, data, enter_the_homepage):
        CameraManage(enter_the_homepage).add_camera(room=data['room_name'], NVR=data['NVR'], camera_name=data['camera_name'],
                                                    channel_number=data['channel_number'], whether_control=data['whether_control'])
        assert '成功' in HomePage(enter_the_homepage).get_success_save_tip()
