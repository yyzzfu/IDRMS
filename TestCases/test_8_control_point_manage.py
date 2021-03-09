import pytest
import allure
from PageObjects.ArchiveManagementPages.control_point_manage_page import ControlPointManagePage
from PageObjects.home_page import HomePage
from Common import dir_config
from Common.do_excel import DoExcel


@allure.epic('项目名称：配电房平台V1.0')
@pytest.mark.usefixtures('enter_the_homepage')
# @pytest.mark.usefixtures('delete_table_ar_control_point')
@pytest.mark.usefixtures('refresh')
@allure.feature('档案管理')
@allure.story('控制节点管理')
# @pytest.mark.skip('跳过')
class TestDataPointManage:

    datas = DoExcel('control_point').get_data(dir_config.archives_data_excel_path)

    @pytest.mark.parametrize('data', datas)
    @allure.title('控制节点管理--新增功能')
    def test_add_data_point(self, data, enter_the_homepage):
        ControlPointManagePage(enter_the_homepage).add_control_point(room=data['room_name'], monitoring=data['monitoring_name'],
                                                                     data_type=data['data_type'], status_feedback_point=data['status_feedback_point'],
                                                                     control_point_name=data['control_point_name'], channel_number=data['channel_number'])
        assert '成功' in HomePage(enter_the_homepage).get_success_save_tip()
