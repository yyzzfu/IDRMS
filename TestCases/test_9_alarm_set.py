import pytest
import allure
from PageObjects.ArchiveManagementPages.alarm_set_page import AlarmSetPage
from PageObjects.home_page import HomePage
from Common import dir_config
from Common.do_excel import DoExcel


@allure.epic('项目名称：配电房平台V1.0')
@pytest.mark.usefixtures('enter_the_homepage')
# @pytest.mark.usefixtures('delete_table_ar_control_point')
@pytest.mark.usefixtures('refresh')
@allure.feature('档案管理')
@allure.story('智能网关告警设置')
# @pytest.mark.skip('跳过')
class TestDataPointManage:

    datas = DoExcel('alarm_set').get_data(dir_config.archives_data_excel_path)

    @pytest.mark.parametrize('data', datas)
    @allure.title('智能网关告警设置--新增功能')
    def test_add_alarm_set(self, data, enter_the_homepage):
        AlarmSetPage(enter_the_homepage).add_alarm_set(room=data['room_name'], monitoring=data['monitoring_name'], node_position=data['node_position'],
                                                       cabinet_or_transformer=data['cabinet_or_transformer'], alarm_type=data['alarm_type'],
                                                       alarm_data=data['alarm_data'], value_feedback_point=data['value_feedback_point'],
                                                       upper_limit=data['upper_limit'], remark=data['remark'])
        assert '成功' in HomePage(enter_the_homepage).get_success_save_tip()
