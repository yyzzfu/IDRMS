import pytest
import allure
from PageObjects.ArchiveManagementPages.transformer_archive_management_page import TransformerArchiveManagePage
from PageObjects.home_page import HomePage
from Common import dir_config
from Common.do_excel import DoExcel


@allure.epic('项目名称：配电房平台V1.0')
@pytest.mark.usefixtures('enter_the_homepage')
# @pytest.mark.usefixtures('delete_table_ar_transformer')
@pytest.mark.usefixtures('refresh')
@allure.feature('档案管理')
@allure.story('变压器档案管理')
# @pytest.mark.skip('跳过')
class TestTransformerArchiveManage:

    datas = DoExcel('transformer').get_data(dir_config.archives_data_excel_path)

    @pytest.mark.parametrize('data', datas)
    @allure.title('变压器档案管理--新增功能')
    def test_add_transformer(self, data, enter_the_homepage):
        TransformerArchiveManagePage(enter_the_homepage).add_transformer(room=data['room_name'], transformer_name=data['transformer_name'],
                                                                         voltage_level_high=data['voltage_level_high'], voltage_level_low=data['voltage_level_low'],
                                                                         capacity=data['capacity'], remark=data['remark'])
        assert "成功" in HomePage(enter_the_homepage).get_success_save_tip()
