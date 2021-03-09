import pytest
import allure
from PageObjects.ArchiveManagementPages.cabinet_archive_management_page import CabinetArchiveMmanagementPage
from PageObjects.home_page import HomePage
from Common import dir_config
from Common.do_excel import DoExcel


@allure.epic('项目名称：配电房平台V1.0')
@pytest.mark.usefixtures('enter_the_homepage')
# @pytest.mark.usefixtures('delete_table_ar_switch_cabinet')
@pytest.mark.usefixtures('refresh')
@allure.feature('档案管理')
@allure.story('开关柜档案管理')
# @pytest.mark.skip('跳过')
class TestCabinetArchiveMmanage:

    datas = DoExcel('cabinet').get_data(dir_config.archives_data_excel_path)

    @pytest.mark.parametrize('data', datas)
    @allure.title('开关柜档案管理--新增功能')
    def test_add_cabinet(self, data, enter_the_homepage):
        CabinetArchiveMmanagementPage(enter_the_homepage).add_cabinet(room=data['room_name'], cabinet_name=data['cabinet_name'],
                                                                      cabinet_type=data['cabinet_type'], remark=data['remark'])
        assert "成功" in HomePage(enter_the_homepage).get_success_save_tip()
