import pytest
import allure
from PageObjects.ArchiveManagementPages.data_point_manage_page import DataPointManagePage
from PageObjects.home_page import HomePage
from Common import dir_config
from Common.do_excel import DoExcel


@allure.epic('项目名称：配电房平台V1.0')
@pytest.mark.usefixtures('enter_the_homepage')
# @pytest.mark.usefixtures('delete_table_ar_data_point')
@pytest.mark.usefixtures('refresh')
@allure.feature('档案管理')
@allure.story('数据节点管理')
# @pytest.mark.skip('跳过')
class TestDataPointManage:

    datas = DoExcel('data_point').get_data(dir_config.archives_data_excel_path)

    @pytest.mark.parametrize('data', datas)
    @allure.title('数据节点管理--新增功能')
    def test_add_data_point(self, data, enter_the_homepage):
        DataPointManagePage(enter_the_homepage).add_data_point(room=data['room_name'], monitoring=data['monitoring_name'],
                                                               node_position=data['node_position'], cabinet_or_transformer=data['cabinet_or_transformer'],
                                                               data_type=data['data_type'], signal_type=data['signal_type'], data_point_name=data['data_point_name'],
                                                               channel_number=data['channel_number'], data_unit=data['data_unit'],
                                                               decimal_point_number=data['decimal_point_number'], upper_limit=data['upper_limit'],
                                                               remark=data['remark'])
        assert '成功' in HomePage(enter_the_homepage).get_success_save_tip()
