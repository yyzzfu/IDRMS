import pytest
import allure
from PageObjects.ArchiveManagementPages.monitoring_equipment_manage_page import MonitoringEquipmentManagePage
from PageObjects.home_page import HomePage
from Common import dir_config
from Common.do_excel import DoExcel


@allure.epic('项目名称：配电房平台V1.0')
@pytest.mark.usefixtures('enter_the_homepage')
# @pytest.mark.usefixtures('delete_table_ar_monitor_equipment')
@pytest.mark.usefixtures('refresh')
@allure.feature('档案管理')
@allure.story('监控设备管理')
# @pytest.mark.skip('跳过')
class TestMonitoringEquipmentManage:

    datas = DoExcel('monitoring').get_data(dir_config.archives_data_excel_path)

    @pytest.mark.parametrize('data', datas)
    @allure.title('监控设备管理--新增功能')
    def test_add_monitor(self, data, enter_the_homepage):
        MonitoringEquipmentManagePage(enter_the_homepage).add_monitoring(room=data['room_name'], monitoring_name=data['monitoring_name'],
                                                                         monitoring_type=data['monitoring_type'], mailing_address=data['mailing_address'],
                                                                         network_connection_mode=data['network_connection_mode'], network_ip=data['network_ip'],
                                                                         network_port=data['network_port'], domain_name=data['domainName'],
                                                                         login_username=data['login_username'], login_password=data['login_password'],
                                                                         remark=data['remark'])
        HomePage(enter_the_homepage).switch_iframe_to_new_tab()
        assert "成功" in HomePage(enter_the_homepage).get_success_save_tip()
